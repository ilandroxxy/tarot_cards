from aiogram import Bot, Dispatcher, types

from text_handlers_users import *
from text_handlers_admins import *
from inline_handlers import *
from keyboard_handlers import *
from sqlite import *

import asyncio
import os
import dotenv
import random

dotenv.load_dotenv()
API_TOKEN = os.getenv('TOKEN')
admin = int(os.getenv('ADMIN'))

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(text=ForUsers.push_command_stat_hi(user_name))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=open(f'cards/{random.randint(1, 22)}.jpg', 'rb'),
                         caption=ForUsers.push_command_start_caption_card())


async def main():
    # await set_bot_commands(bot)
    # await db_start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())



