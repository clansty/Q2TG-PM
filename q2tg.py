from mirai import FriendMessage, Friend, Plain
import config
from appmgr import updater


def msg(friend: Friend, message: FriendMessage):
    if config.q2tg[friend.id]:
        # if(message.messageChain.hasComponent(Plain)):
        # texts=message.messageChain.getAllofComponent(Plain)
        # text=""
        # for i in texts:
        updater.bot.send_message(chat_id=config.q2tg[friend.id], text=message.toString())
