from bot_config import dp, bot
from aiogram import types
import speaker
import re

@dp.message_handler(commands=['start'])
async def start_bot(messege: types.Message):
    await bot.send_message(messege.from_id, text=f'{messege.from_user.first_name}'
                                                 f' привет, напиши мне что нибудь, '
                                                 f'а я скажу тебе это голосом')


@dp.message_handler()
async def speaker_bot(messege: types.Message):
    if re.findall(r'[А-я]+', messege.text):
        speaker.string_to_speak_ru(messege.text)
        await bot.send_audio(messege.from_id, open('speak.mp3', 'rb'))
    elif re.findall(r'[A-z]+', messege.text):
        speaker.string_to_speak_en(messege.text)
        await bot.send_audio(messege.from_id, open('speak.mp3', 'rb'))




