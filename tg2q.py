from appmgr import app
import config, asyncio

def text(update, context):
    if config.tg2q[update.message.chat.id]:
        asyncio.run(app.sendFriendMessage(config.tg2q[update.message.chat.id], update.message.text))
