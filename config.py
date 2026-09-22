# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

api_id = int(os.environ.get("API_ID", "22419126"))
api_hash = os.environ.get("API_HASH", "4749a270cca7829cfc86564fbde48a3f")
bot_token = os.environ.get("BOT_TOKEN", "8341190833:AAHgS4MoRVSxp4sDSXsnpb5VW9D71HGuxdU")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "5585132028").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")

# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
