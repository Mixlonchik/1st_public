import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='1138058936:AAHPrXC5ZIzzoH5zx18PKbPejfSubjhazBA')
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = 'Ебаный айограмм, блять'
    await  bot.send_message(chat_id=chat_id, text=text)




executor.start_polling(dp)



# bot.get_updates()



# def print_hi(name):
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
