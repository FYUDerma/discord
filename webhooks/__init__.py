# webhooks/__init__.py
from . import github

def webhooks_setup(bot):
    return {
        "github": {
            "path": "/github",
            "handler": github.setup_webhook(bot, channel_id=1361333458147872809)
        }
        # Add more webhooks here
    }

