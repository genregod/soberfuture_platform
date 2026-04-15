#!/usr/bin/env bash
set -euo pipefail

SECRET_NAME="${SECRET_NAME:-KIRO_API_KEY}"
AWS_REGION="${AWS_REGION:-${AWS_DEFAULT_REGION:-us-east-1}}"

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1" >&2
    return 1
  }
}

mask_secret() {
  local s="${1:-}"
  local n=${#s}
  if (( n <= 8 )); then
    printf '%s\n' '********'
  else
    printf '%s\n' "${s:0:4}****${s:n-4:4}"
  fi
}

prompt_if_missing() {
  local var_name="$1"
  local prompt_text="$2"
  local secret="${3:-false}"

  if [[ -z "${!var_name:-}" ]]; then
    if [[ "$secret" == "true" ]]; then
      read -rsp "$prompt_text" "$var_name"
      echo
    else
      read -rp "$prompt_text" "$var_name"
    fi
    export "$var_name"
  fi
}

require_cmd aws
require_cmd jq

# Fix the exact problem you hit: partial AWS creds in env.
prompt_if_missing AWS_ACCESS_KEY_ID "AWS_ACCESS_KEY_ID: "
prompt_if_missing AWS_SECRET_ACCESS_KEY "AWS_SECRET_ACCESS_KEY: " true

# Optional for temporary creds only.
if [[ -n "${AWS_SESSION_TOKEN:-}" ]]; then
  export AWS_SESSION_TOKEN
else
  read -rp "Using temporary STS credentials? [y/N]: " USE_STS
  if [[ "${USE_STS:-N}" =~ ^[Yy]$ ]]; then
    prompt_if_missing AWS_SESSION_TOKEN "AWS_SESSION_TOKEN: " true
  fi
fi

echo "Checking AWS identity..."
AWS_ARN="$(
  aws sts get-caller-identity \
    --query Arn \
    --output text \
    --region "$AWS_REGION"
)"
AWS_ACCOUNT="$(
  aws sts get-caller-identity \
    --query Account \
    --output text \
    --region "$AWS_REGION"
)"
echo "AWS auth OK."
echo "AWS account: $AWS_ACCOUNT"
echo "AWS ARN: $AWS_ARN"

# Kiro key still has to come from Kiro account settings.
prompt_if_missing KIRO_API_KEY "Paste Kiro API key: " true

if [[ -z "${KIRO_API_KEY:-}" ]]; then
  echo "No KIRO_API_KEY provided. Exiting." >&2
  return 1 2>/dev/null || exit 1
fi

echo "Checking whether secret '${SECRET_NAME}' exists in region '${AWS_REGION}'..."
if aws secretsmanager describe-secret \
  --secret-id "$SECRET_NAME" \
  --region "$AWS_REGION" >/dev/null 2>&1; then

  echo "Secret exists. Updating current value..."
  aws secretsmanager put-secret-value \
    --secret-id "$SECRET_NAME" \
    --secret-string "$KIRO_API_KEY" \
    --region "$AWS_REGION" >/dev/null
else
  echo "Secret does not exist. Creating it..."
  aws secretsmanager create-secret \
    --name "$SECRET_NAME" \
    --description "Kiro headless API key" \
    --secret-string "$KIRO_API_KEY" \
    --region "$AWS_REGION" >/dev/null
fi

echo "Retrieving secret back from AWS Secrets Manager..."
export KIRO_API_KEY="$(
  aws secretsmanager get-secret-value \
    --secret-id "$SECRET_NAME" \
    --query SecretString \
    --output text \
    --region "$AWS_REGION"
)"

echo
echo "Done."
echo "Secret name: $SECRET_NAME"
echo "Region: $AWS_REGION"
echo "Exported KIRO_API_KEY in current shell."
echo "Masked Kiro key: $(mask_secret "$KIRO_API_KEY")"
echo
echo "Headless test:"
echo 'kiro-cli chat --no-interactive "say hello"'
