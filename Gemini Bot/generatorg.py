import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import google.generativeai as genial

from config import TG_BOT_TOKEN
from config import GEMINI_API_KEY

# Вставьте свои ключи
TG_BOT_TOKEN =TG_BOT_TOKEN 
GEMINI_API_KEY = GEMINI_API_KEY

# Инициализация бота и диспетчера
bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()

# Настройка Gemini AI
genial.configure(api_key=GEMINI_API_KEY)

PROMPT = "Ты ассистент который отвечает на вопросы компаний Mature AI, мы компания по созданию ИИ ассистентов, ассистент которая работает 24/7,когда они напишут свое имя то ты через каждое сообщение ставишь там их имя но не говори им что ты так будешь обращаться через каждое сообщение,Только если тебя спросят как связаться с нами то отправь им так для связи наш Instagram:@mature__ai"

# Обработчик команд (например, /start)
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Здраствуйте! Меня зовут Айсұлтан,я Ассистент компаний Mature AI. Как можно к вам обращаться?")

# Обработчик сообщений
@dp.message()
async def chat_with_gemini(message: Message):
    model = genial.GenerativeModel("gemini-2.5-pro-exp-03-25")
    response = model.generate_content(PROMPT + "\n" + message.text)

    if response and response.candidates:
        answer = response.candidates[0].content.parts[0].text
        await message.answer(answer)
    else:
        await message.answer("Извините, я не смог сформулировать ответ.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())