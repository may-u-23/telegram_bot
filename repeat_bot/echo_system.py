#!python3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram_bot import TelegramBot

class EchoSystem:
    def __init__(self):
        pass

    def initial_message(self, input):
        return {'utt': 'こんにちは。あなたの発言を繰り返します。話しかけてください。', 'end': False}
    
    def reply(self, input):
        return {'utt': input['utt'], 'end': False}

if __name__ == '__main__':
    system = EchoSystem()
    bot = TelegramBot(system)
    bot.run()