import os

from telegram import ParseMode, ChatAction
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import speechToText as sTT

TELEGRAM_TOKEN = "SEU_TELEGRAM_TOKEN"
BING_TOKEN = "SEU_BING_SPEECH_TOKEN"


def start(bot, update):
    user_id = update['message']['chat']['id']
    first_name = update['message']['chat']['first_name']
    bot.sendChatAction(chat_id=user_id, action=ChatAction.TYPING)
    message_text = """<b>Olá {}!</b>

Fui criado com o intuito de transformar seus áudios em textos. 

Vamos começar?

Envie um audio para que eu possa transforma-lo em texto!""".format(first_name)
    bot.send_message(chat_id=user_id, text=message_text, parse_mode=ParseMode.HTML)


def speech_to_text(bot, update):
    user_id = update['message']['chat']['id']
    first_name = update['message']['chat']['first_name']
    file_name = str(user_id) + '_' + str(update.message.from_user.id) + str(update.message.message_id) + '.ogg'
    update['message']['voice'].get_file().download(file_name)

    try:
        message_text = "{}, você disse “{}”.".format(first_name, sTT.recognize_bing(file_name, key=BING_TOKEN, language="pt-BR"))
    except sTT.UnknownValueError:
        message_text = "{}, não consegui entender o que você falou.".format(first_name)
    except sTT.RequestError:
        message_text = "{}, não consegui processar seu audio. Que tal enviar outro?".format(first_name)
    os.remove(file_name)

    bot.send_message(chat_id=user_id, text=message_text, parse_mode=ParseMode.HTML)


def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.voice, speech_to_text))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
