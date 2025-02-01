import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")
PREVIEW_IMAGE_APP_URL = os.getenv("PREVIEW_IMAGE_APP_URL")

dp = Dispatcher()


@dp.message()
async def handle_all_messages(message: Message):
    keyboard = InlineKeyboardBuilder()
    text = ("<b>Buy TRX for USDT</b>\n"
            "Even if you don't have any TRX right now.")
    keyboard.button(
        text="Buy TRX",
        web_app=WebAppInfo(
            url=WEB_APP_URL + f"?telegram-mini-app/{message.from_user.username}",
        ),
    )
    await message.bot.send_photo(
        chat_id=message.chat.id,
        caption=text,
        photo=PREVIEW_IMAGE_APP_URL,
        reply_markup=keyboard.as_markup(),
        parse_mode=ParseMode.HTML,
    )


async def main() -> None:
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
