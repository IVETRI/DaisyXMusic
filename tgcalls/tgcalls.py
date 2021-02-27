from pyrogram import Client
from pytgcalls import PyTgCalls

from sira import is_empty, get, task_done
import config


client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(1512, False)


@pytgcalls.on_stream_end()
def on_stream_end(chat_id: int) -> None:
    task_done(chat_id)

    if is_empty(chat_id):
        pytgcalls.leave_group_call(chat_id)
    else:
        pytgcalls.change_stream(chat_id, get(chat_id)["file_path"])


def run():
    pytgcalls.run(client)
