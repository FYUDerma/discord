from aiohttp import web

def setup_webhook(bot, channel_id):
    async def handle_github_webhook(request):
        data = await request.json()
        event = request.headers.get('X-GitHub-Event')

        if event == "push":
            repo = data["repository"]["name"]
            pusher = data["pusher"]["name"]
            commits = data["commits"]
            messages = "\n".join([f"- {c['message']}" for c in commits])

            msg = f"📦 **{pusher}** pushed to **{repo}**:\n{messages}"
            channel = bot.get_channel(channel_id)
            if channel:
                await channel.send(msg)

        return web.Response(text="GitHub Webhook received.")

    return handle_github_webhook
