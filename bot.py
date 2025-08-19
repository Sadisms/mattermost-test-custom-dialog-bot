import asyncio

from loguru import logger
from mmpy_bot import Bot, Settings
from config import config
from plugin import TestPlugin



bot = Bot(
    settings=Settings(
        MATTERMOST_URL=config['mattermost']['url'],
        MATTERMOST_PORT=int(config['mattermost']['port']),
        BOT_TOKEN=config['mattermost']['token'],
        WEBHOOK_HOST_ENABLED=True,
        WEBHOOK_HOST_URL=f'http://{config["webhook"]["bot_name"]}',
        SSL_VERIFY=False,
    ),
    plugins=[
        TestPlugin(logger)
    ]
)

loop = asyncio.get_event_loop()


def start_bot():
    bot.run()
