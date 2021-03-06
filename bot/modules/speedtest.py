from speedtest import Speedtest
import bot

from bot.helper.telegram_helper.filters import CustomFilters
from bot import dispatcher, AUTHORIZED_CHATS
from bot.helper.telegram_helper.bot_commands import BotCommands
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackContext, Filters, CommandHandler

def speedtest(update, context):
    message = update.effective_message
    ed_msg = message.reply_text("Running Speed Test . . . đš ")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    path = (result['share'])
    string_speed = f'''
<b>đ„ïž Server :- đ€</b>

<b>đł Name : {result['server']['name']}</b>
<b>âłïž Country : {result['server']['country']}, {result['server']['cc']}</b>
<b>đ Sponsor : {result['server']['sponsor']}</b>
    
<b>âĄïž Internet Speed Meter :- đ€</b>

<b>đșU : {speed_convert(result['upload'])} = {speed_convert(result['upload'] / 8)}</b>
<b>đ»D : {speed_convert(result['download'])} = {speed_convert(result['download'] / 8)}</b>
<b>đ PING : {result['ping']}</b>
<b>đą ISP : {result['client']['isp']}</b>
'''
    ed_msg.delete()
    try:
        update.effective_message.reply_photo(path, string_speed, parse_mode=ParseMode.HTML)
    except:
        update.effective_message.reply_text(string_speed, parse_mode=ParseMode.HTML)

def speed_convert(size):
    """Hi human, you can't read bytes?"""
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "MB/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


SPEED_HANDLER = CommandHandler(BotCommands.SpeedCommand, speedtest, 
                                                  filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(SPEED_HANDLER)