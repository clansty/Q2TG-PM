from mirai import FriendMessage, Friend, Plain, Image
import config
from appmgr import updater


def msg(friend: Friend, message: FriendMessage):
    if config.q2tg[friend.id]:
        if message.messageChain.hasComponent(Plain) :
            texts=message.messageChain.getAllofComponent(Plain)
            text=""
            for i in texts:
                text+=i.toString()
                text+=' '
            text=text.strip()
            updater.bot.send_message(chat_id=config.q2tg[friend.id], text=message.toString())
        if message.messageChain.hasComponent(Image):
            images=message.messageChain.getAllofComponent(Image)
            for image in images:
                updater.bot.send_message(chat_id=config.q2tg[friend.id], text=image.url)
