# AI Agents & MCP: Plug ChatGPT, Claude, or Codex Into ViralWave

ViralWave Studio exposes a secure MCP (Model Context Protocol) server. Connect your favorite AI assistant once, and you can manage your content from inside a chat: check your brand voice, review drafts, generate posts, even schedule — without opening the dashboard.

## The one URL

```
https://viralwavestudio.com/mcp
```

That's it. No API keys to create, copy, or store. Compatible assistants discover ViralWave's OAuth server, open a consent page in your browser, and securely handle tokens from there. You approve exactly what the assistant can access.

You can revoke access anytime from **Workspace → AI Agents** in your ViralWave dashboard.

## Connect Codex

In Codex, go to **Settings → MCP servers → Add custom MCP**:

| Field | Value |
|---|---|
| Name | `ViralWave` |
| Type | `Streamable HTTP` |
| URL | `https://viralwavestudio.com/mcp` |

Save, select **Authenticate**, sign in to ViralWave, and approve the connection.

In Codex CLI, add to your config:

```toml
[mcp_servers.viralwave]
url = "https://viralwavestudio.com/mcp"
default_tools_approval_mode = "writes"
tool_timeout_sec = 60
```

Then:

```text
codex mcp login viralwave
```

Start with a read-only check:

```text
Use ViralWave to read my account context and summarize my brand voice
and connected platforms. Do not create or schedule anything.
```

## Connect ChatGPT

On ChatGPT web:

1. Enable **Developer mode** under **Settings → Apps → Advanced Settings**
2. Choose **Create app** and provide `https://viralwavestudio.com/mcp`
3. Select OAuth authentication, scan tools, sign in to ViralWave, approve access

Note: full create and scheduling actions through ChatGPT currently depend on an eligible ChatGPT Business, Enterprise, or Edu workspace and its administrator settings.

## Connect Claude

1. Open **Customize → Connectors**
2. Choose **Add custom connector**, name it `ViralWave`
3. Paste `https://viralwavestudio.com/mcp`, select **Connect**
4. Sign in to ViralWave and approve access

## What your assistant can do

| Tool | Permission | What it does |
|---|---|---|
| `get_account_context` | read | Your brand voice, connected platforms, balances |
| `list_posts` | read | Drafts, scheduled posts, history, failures |
| `get_post` | read | Read one post by ID |
| `get_content_summary` | read | Delivery and content-mix metrics |
| `create_drafts` | drafts | Save your own draft text (no token cost) |
| `generate_campaign_drafts` | drafts | Generate new AI drafts (one token per post) |
| `update_draft` | drafts | Edit private drafts |
| `schedule_post` | schedule | Queue a post (asks for your confirmation first) |
| `cancel_scheduled_post` | schedule | Pull a scheduled post back to draft |
| `generate_video` | video | Generate AI video (uses one video credit) |
| `check_video_status` | video | Check on a video job |

Read-only access grants the read tools. Approving creator access adds drafts, scheduling, and video. **Scheduling always asks for explicit confirmation inside the chat** — your assistant can't post without you saying so.

Two platform notes: X/Twitter isn't available for agent scheduling yet, and TikTok is excluded until its commercial-content disclosures can be handled safely in the agent flow.

## Example prompts to try

```text
Summarize my ViralWave brand voice and tell me which platforms I'm
publishing to this month.
```

```text
Show me my scheduled posts for next week. Flag any that look off-brand.
```

```text
Generate 5 draft posts for my upcoming sale. Save them as drafts —
don't schedule anything.
```

```text
Which of my posts performed best last month, and what pattern do you see?
```

## Manual key fallback

If your client can't do browser-based OAuth, the **AI Agents** page in your dashboard can generate a revocable `vws_mcp_...` key. Treat it like a password: store it as an operating-system environment variable and reference the variable name in your client config — never paste the key itself.

---

**[→ Connect your assistant at viralwavestudio.com](https://viralwavestudio.com)**

Next: [07 — Plans & pricing](07-plans-and-pricing.md).
