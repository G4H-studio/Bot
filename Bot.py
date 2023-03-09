import logging

from aiogram import Bot, Dispatcher, executor, types

print("""
    ____        __ 
   / __ )____  / /_
  / __  / __ \\/ __/
 / /_/ / /_/ / /_  
/_____/\\____/\\__/  
                   
""")

API_TOKEN = '5823132945:AAHhg09waAa_7ZnpeTm7-v2vb2Ix17WIjMI'

Text = input("Введите сообщение: ")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("+ - + - + - +\n| G | 4 | H |\n+ - + - + - +")



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(Text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)