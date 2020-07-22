from telegram.ext import MessageHandler, Filters, CommandHandler
import config
from mirai import Mirai, Plain, MessageChain, Friend, Group, Member, FriendMessage, GroupMessage, TempMessage, Image, MemberJoinEvent
import asyncio
from appmgr import app
import logging
import tg2q
import q2tg
from start import start
from appmgr import updater

dispatcher=updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text & Filters.user(config.userid) &(~Filters.command),tg2q.text))
dispatcher.add_handler(MessageHandler(Filters.photo & Filters.user(config.userid),tg2q.photo))

@app.receiver("FriendMessage")
async def event_gm(friend: Friend, message: FriendMessage):
    q2tg.msg(friend, message)
    
updater.start_polling()
app.run()