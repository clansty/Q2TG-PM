# Q2TG
适用与私聊的 QQ 消息与 Telegram 互转

## 配置文件
```py
token='tg机器人token'
proxy='代理服务器'
qq=机器人QQ
authKey = 'miraihttp key'
mirai_api_http_locate = 'localhost:8080/ws'
userid=你的 tguid

q2tg={
    qq号: tguid,
    qq号: tguid
}

tg2q={    #（上面的反过来写）
    tguid: qq号,
    tguid: qq号,
}
```