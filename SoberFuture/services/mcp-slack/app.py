"""
SoberFuture Build Bot — persistent Socket Mode listener.
Treats Slack messages from the owner as first-class commands,
identical to direct CLI interaction.
"""
import os
import subprocess
import sys
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env.local"))

BOT_TOKEN      = os.environ["SLACK_BOT_TOKEN"]
SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
APP_TOKEN      = os.environ["SLACK_APP_TOKEN"]
BOT_USER_ID    = "U0AS5DAU5CK"

CHANNELS = {
    "build":        "C0ASFCL4012",
    "approvals":    "C0ASBG9JGAJ",
    "alerts":       "C0AT7S4RUJC",
    "architecture": "C0AT7S6JADN",
}

app = App(token=BOT_TOKEN, signing_secret=SIGNING_SECRET)
client = WebClient(token=BOT_TOKEN)


def post(channel_key: str, text: str):
    client.chat_postMessage(channel=CHANNELS[channel_key], text=text)


def post_to(channel_id: str, text: str):
    client.chat_postMessage(channel=channel_id, text=text)


# ── Core message dispatcher ───────────────────────────────────────────────────
def dispatch(text: str, channel: str, user: str, say):
    """Route a message to the appropriate handler."""
    t = text.strip().lower()

    if t in ("status", "!status"):
        say(_status_report())

    elif t.startswith("!run "):
        cmd = text.strip()[5:]
        say(f"⚙️ Running: `{cmd}`")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        output = (result.stdout + result.stderr).strip()[:3000] or "(no output)"
        say(f"```{output}```")

    elif t.startswith("!approve "):
        say(f"✅ Approval recorded for: `{text[9:]}`")
        post("approvals", f"✅ Approved via Slack by <@{user}>: `{text[9:]}`")

    elif t.startswith("!deny "):
        say(f"❌ Denial recorded for: `{text[6:]}`")
        post("approvals", f"❌ Denied via Slack by <@{user}>: `{text[6:]}`")

    elif t in ("!help", "help"):
        say(_help_text())

    elif t in ("!servers", "servers"):
        say(_server_status())

    else:
        # Echo back anything unrecognised so you know it was received
        say(f"📨 Received: `{text}`\n\nType `help` for available commands.")


def _status_report() -> str:
    return (
        "*📊 SoberFuture Build Bot — Status*\n\n"
        "• mcp-slack: ✅ running\n"
        "• mcp-github: 🔧 needs GITHUB_TOKEN\n"
        "• mcp-browser: 🔧 needs `playwright install`\n"
        "• mcp-aws-docs: 🔧 ready\n"
        "• mcp-repo-context: 🔧 ready\n"
        "• mcp-package-docs: 🔧 ready\n"
        "• mcp-adr: 🔧 ready\n\n"
        "_Chain 1 (ADRs) is next._"
    )


def _server_status() -> str:
    import json, pathlib
    reg = pathlib.Path(__file__).parent.parent.parent / "mcp-registry.json"
    data = json.loads(reg.read_text())
    lines = ["*🗂 MCP Registry*\n"]
    for s in data["servers"]:
        icon = "✅" if s["status"] == "active" else "🔧"
        lines.append(f"{icon} *{s['name']}* v{s['version']} — {s['status']}")
    return "\n".join(lines)


def _help_text() -> str:
    return (
        "*SoberFuture Build Bot — Commands*\n\n"
        "`status` — current system status\n"
        "`servers` — MCP registry overview\n"
        "`!run <cmd>` — run a shell command and return output\n"
        "`!approve <item>` — record an approval\n"
        "`!deny <item>` — record a denial\n"
        "`help` — this message\n\n"
        "_You can also just talk — anything sent here is received and logged._"
    )


# ── Event handlers ────────────────────────────────────────────────────────────

@app.event("app_mention")
def handle_mention(event, say):
    text = event.get("text", "").replace(f"<@{BOT_USER_ID}>", "").strip()
    dispatch(text, event["channel"], event["user"], say)


@app.event("message")
def handle_message(event, say):
    # Ignore bot messages and message edits
    if event.get("bot_id") or event.get("subtype"):
        return
    text = event.get("text", "").strip()
    if not text:
        return
    dispatch(text, event["channel"], event.get("user", ""), say)


# ── Approval button handlers ──────────────────────────────────────────────────

@app.action("approve")
def handle_approve(ack, body, client):
    ack()
    user = body["user"]["name"]
    original = body["message"]["blocks"][0]["text"]["text"]
    client.chat_postMessage(channel=CHANNELS["approvals"], text=f"✅ Approved by @{user}")
    print(f"[APPROVAL] Approved by {user}")


@app.action("deny")
def handle_deny(ack, body, client):
    ack()
    user = body["user"]["name"]
    client.chat_postMessage(channel=CHANNELS["approvals"], text=f"❌ Denied by @{user}")
    print(f"[APPROVAL] Denied by {user}")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("⚡ mcp-slack: Socket Mode listener starting...")
    post("build", "🔄 *Build Bot restarted* — Socket Mode listener is active. Send `help` for commands.")
    handler = SocketModeHandler(app, APP_TOKEN)
    handler.start()
