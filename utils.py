from functools import lru_cache

import requests

from config import  config


@lru_cache
def get_webhook_address() -> str:
    response = requests.get(
        url=f"{config['webhook']['url']}/get-global-address/{config['webhook']['token']}"
    )

    if response.status_code == 200:
        return f'{response.text}/hooks/{config["webhook"]["token"]}/{config["webhook"]["bot_name"]}'

    return ""
