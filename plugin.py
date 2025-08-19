from mm_tools.plugins.base_plugin import BasePlugin
from mmpy_bot.wrappers import  Message, DialogEvent
from mmpy_bot.function import listen_to, listen_submit_dialog, listen_update_dialog_ellemnt

from config import config
from dialogs import create_custom_dialog


CALLBACK_ON_SUBMIT = "submit_dialog"
CALLBACK_ON_UPDATE = "update_dialog"


class TestPlugin(BasePlugin):
    @listen_to("test")
    async def test_handler(self, message: Message) -> None:
        user_id = message.user_id

        self.driver.create_custom_dialog(
            plugin_base_url=config['mattermost']['plugin_url'],
            dialog_data=create_custom_dialog(
                user_id=user_id,
                callback_on_submit=CALLBACK_ON_SUBMIT,
                callback_on_update=CALLBACK_ON_UPDATE,
            )
        )

    @listen_submit_dialog(CALLBACK_ON_SUBMIT)
    async def submit_dialog_handler(self, event: DialogEvent) -> None:
        print(event.body)


    @listen_update_dialog_ellemnt(CALLBACK_ON_UPDATE)
    async def update_dialog_handler(self, event: DialogEvent) -> None:
        print(event.body)
