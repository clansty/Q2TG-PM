from appmgr import app
import config, asyncio
# from mirai import Image as qqimg
# from uuid import uuid4
# from PIL import Image
# import io

def text(update, context):
    if config.tg2q[update.message.chat.id]:
        asyncio.run(app.sendFriendMessage(config.tg2q[update.message.chat.id], update.message.text))

def photo(update, context):
    pass
    # todo 图裂了
    # if config.tg2q[update.message.chat.id]:
    #     photo=update.message.photo[len(update.message.photo)-1]
    #     print(photo)
    #     file=photo.get_file()
        # path=f"/tmp/{uuid4()}"
        # file.download(custom_path=path)
        # print(path)
        # asyncio.run(app.sendFriendMessage(config.tg2q[update.message.chat.id], [Image.fromFileSystem(path)]))
        # imgarray=file.download_as_bytearray()
        # img=Image.open(io.BytesIO(imgarray))
        # imgio=io.BytesIO()
        # img.save(imgio,format="PNG")
        # imgbytes=imgio.read()
        # asyncio.run(app.sendFriendMessage(config.tg2q[update.message.chat.id], [qqimg.fromBytes(imgbytes)]))
        