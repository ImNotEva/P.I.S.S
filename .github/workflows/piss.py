import os, requests

handle = os.getenv("BSKY_HANDLE")           # comes from your GitHub secret
discord_webhook = os.getenv("DISCORD_WEBHOOK")

# Get the author feed (public Bluesky API, no login required)
url = f"https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor={handle}&limit=1"
resp = requests.get(url)

if resp.status_code != 200:
    raise Exception(f"Failed to fetch feed for {handle}: {resp.text}")

feed = resp.json()
if not feed.get("feed"):
    print("No posts found.")
    exit()

post = feed["feed"][0]["post"]["record"].get("text", "(no text)")

# Send to Discord
message = f"💦 New P.I.S.S drop from **{handle}**:\n{post}"
requests.post(discord_webhook, json={"content": message})
