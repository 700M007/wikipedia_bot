import wikipedia

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6258316576:AAEqtMCz1xOxgRiRm_C9o_-_Tq0DHJ6uD_8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /start kommandasi uchun handler
@dp.message_handler(commands="boshlash")
async def select_start(message:types.Message):
    await message.answer(f"Assalomu alaykum @{message.from_user.username} mening botimga hush kelibsiz")

# /help kommandasi uchun handler
@dp.message_handler(commands="help")
async def select_help(message:types.Message):
    await message.answer("Salom men Muhammadning botiman sizga nima yordam kerak")


# To'tiqush handler
wikipedia.set_lang("uz")
@dp.message_handler()
async def echo_handler(message:types.Message):
    try:
        javob=wikipedia.summary(message)
        await message.answer(javob)
    except:
        await  message.answer("🤷‍♂️Bunday ma'lumot yopilmadi boshqa xabar yozing")





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)