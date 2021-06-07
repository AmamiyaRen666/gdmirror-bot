from telegram.ext import CommandHandler
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot.helper.telegram_helper.message_utils import *
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.bot_utils import new_thread
from bot import dispatcher

def cloneNode(update,context):
    args = update.message.text.split(" ",maxsplit=1)
    if update.message.from_user.username:
        uname = f"@{update.message.from_user.username}"
    else:
        uname = f'<a href="tg://user?id={update.message.from_user.id}">{update.message.from_user.first_name}</a>'
    if uname is not None:
            cc = f'\n✅ <b>Status :- Successfully Cloned</b>\n\n🙎🏻‍♂️ <b>By :- {uname}</b> ✨'
    if len(args) > 1:
        link = args[1]
        msg = sendMessage(f"😁 <b>Cloning File :</b> <code>{link}</code>",context.bot,update)
        gd = GoogleDriveHelper()
        result, button = gd.clone(link)
        deleteMessage(context.bot,msg)
        if button == "":
            sendMessage(result,context.bot,update)
        else:
            sendMarkup(result + cc,context.bot,update,button)
    else:
        sendMessage("🚫 Send Me Google Drive Shareable Link to Clone 🚫",context.bot,update)
clone_handler = CommandHandler(BotCommands.CloneCommand,cloneNode,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(clone_handler)
