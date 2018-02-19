import telebot

from Modules.Common.helper import LogClass, Failure
from Modules.Common.logger import Logger
from Configurations import config

class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(config.token)
        self.bot_logger = Logger(name='Bot logger', log_class=LogClass.Info, log_to_file=True,
                                 log_script_information=True,
                                 log_name='bot_log.txt')

        @self.bot.message_handler(content_types=['text'])
        def handle_messages(message):
            self.bot_logger.log_string(LogClass.Trace, 'Got message at {}: {}'.format(message.chat.id, message.text))
            self.bot.send_message(message.chat.id, message.text)
            log_string = 'Sent message: {message_to_send}'.format(message_to_send=message.text)
            self.bot_logger.log_string(LogClass.Info, log_string)



    def start_bot(self):
        self.bot.polling(none_stop=True)

    def stop_bot(self):
        self.bot.stop_polling()


def main():
    bot = TelegramBot()
    bot.start_bot()