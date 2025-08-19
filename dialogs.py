from mm_tools.dialogs.custom_dialogs import (
    CustomDialog,
    TextElement
)

from utils import get_webhook_address


def create_custom_dialog(
    user_id: str,
    callback_on_submit: str,
    callback_on_update: str,
) -> dict:
    url = get_webhook_address()

    url_on_update = url.rstrip('/') + f'/{callback_on_update}'
    url_on_submit = url.rstrip('/') + f'/{callback_on_submit}'

    return CustomDialog(
        title="Test custom dialog",
        user_id=user_id,
        callback_url_on_submit=url_on_submit,
        callback_url_on_update=url_on_update,
        elements=[
            TextElement(
                name="kak_dela",
                label="Как дела?",
                on_update=True,
                required=True
            )
        ]
    ).to_dict()
