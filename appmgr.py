from mirai import Mirai
import config
from telegram.ext import Updater


app = Mirai(f"mirai://{config.mirai_api_http_locate}?authKey={config.authKey}&qq={config.qq}")
updater = Updater(token=config.token, use_context=True, request_kwargs={'proxy_url': config.proxy})
