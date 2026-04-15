#!/usr/bin/env bash
# deploy-ec2.sh — Deploy SoberFuture services to EC2 dev instance
# Usage: ./infra/scripts/deploy-ec2.sh
# Requires: SSH key configured, EC2 instance running

set -euo pipefail

EC2_HOST="52.54.162.129"
EC2_USER="ec2-user"
DEPLOY_DIR="/opt/soberfuture"
REPO_DIR="/home/arnieai/soberfuture"

echo "==> Deploying to $EC2_HOST"

# 1. Sync code (exclude secrets, venvs, node_modules)
rsync -avz --progress \
  --exclude='.git' \
  --exclude='**/.venv' \
  --exclude='**/node_modules' \
  --exclude='**/__pycache__' \
  --exclude='**/.env.local' \
  --exclude='**/.env.production' \
  --exclude='**/uv.lock' \
  "$REPO_DIR/" \
  "$EC2_USER@$EC2_HOST:$DEPLOY_DIR/"

echo "==> Code synced"

# 2. Remote setup
ssh "$EC2_USER@$EC2_HOST" bash << 'REMOTE'
set -euo pipefail

DEPLOY_DIR="/opt/soberfuture"
export PATH="$HOME/.local/bin:$PATH"

# Install uv if not present
if ! command -v uv &>/dev/null; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Install nginx if not present
if ! command -v nginx &>/dev/null; then
  sudo dnf install -y nginx
fi

# MCP Gateway
echo "==> Setting up mcp-gateway"
cd "$DEPLOY_DIR/services/mcp-gateway"
uv sync --no-dev

# Core API
echo "==> Setting up api"
cd "$DEPLOY_DIR/services/api"
uv sync --no-dev

# Nginx config
sudo cp "$DEPLOY_DIR/infra/nginx/soberfuture.conf" /etc/nginx/conf.d/soberfuture.conf
sudo nginx -t && sudo systemctl enable nginx && sudo systemctl restart nginx

# Systemd services
sudo cp "$DEPLOY_DIR/services/mcp-gateway/mcp-gateway.service" /etc/systemd/system/
sudo cp "$DEPLOY_DIR/services/api/soberfuture-api.service" /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable mcp-gateway soberfuture-api
sudo systemctl restart mcp-gateway soberfuture-api

echo "==> Services started"
sudo systemctl status mcp-gateway --no-pager
sudo systemctl status soberfuture-api --no-pager
REMOTE

echo "==> Deploy complete"
echo "    MCP Gateway: http://$EC2_HOST:8100"
echo "    Core API:    http://$EC2_HOST:8000"
echo "    MCP endpoint: http://$EC2_HOST:8100/mcp"
