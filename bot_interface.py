from telegram import *
from telegram.ext import *
from decouple import config
SECRET_KEY=config('SECRET_KEY')
bot=Bot(SECRET_KEY) 

# print(bot.get_me())
updater=Updater(SECRET_KEY,use_context=True)
dispatcher : Dispatcher=updater.dispatcher


keyword=''
chat_id=''
def test1(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="working",
        parse_mode=ParseMode.HTML
    )

def showkeyboard(update:Update,context:CallbackContext):
    keyboard=[[
        InlineKeyboardButton('CS 44',callback_data='CS 44'),
        InlineKeyboardButton('CS 55',callback_data='CS 55'),
        InlineKeyboardButton('IT 61',callback_data='IT 61')
    ]]
    reply_markup=InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Hi Juitian,\nSelect Batch ',reply_markup=reply_markup)

def button_click(update:Update,context:CallbackContext):
    global keyword,chat_id

    query:CallbackQuery=update.callback_query
    if query.data=="CS 44":
        bot.send_message(
        chat_id=update.effective_chat.id,
        text="Please Join This Channel For all Upcoming Notifications Regarding Time Table \nhttps://t.me/joinchat/V--DcdP1J8nDMlJV",
        parse_mode=ParseMode.HTML
        )
    
    if query.data=="CS 55":
        bot.send_message(
        chat_id=update.effective_chat.id,
        text="Please Join This Channel For all Upcoming Notifications  Regarding Time Table \nhttps://t.me/joinchat/SM1RQQqKwxhHmmpj",
        parse_mode=ParseMode.HTML
        )

    if query.data=="IT 61":
        bot.send_message(
        chat_id=update.effective_chat.id,
        text="Please Join This Channel For all Upcoming Notifications  Regarding Time Table \nhttps://t.me/joinchat/V-O3ljcRjYkHge3I",
        parse_mode=ParseMode.HTML
        )


dispatcher.add_handler(MessageHandler(Filters.text,showkeyboard))
dispatcher.add_handler(CallbackQueryHandler(button_click))
updater.start_polling()
