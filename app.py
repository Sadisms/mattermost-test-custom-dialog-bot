import sentry_sdk

from bot import start_bot
from config import config

sentry_sdk.init(
    dsn=config['sentry']['dsn'],
)

if __name__ == '__main__':
    start_bot()
