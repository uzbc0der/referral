from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import StepsForm
from keyboards.reply import admin
import sqlite3


db = sqlite3.connect('my_database.db')
cursor = db.cursor()

async def get_post(message: Message, bot: Bot, state: FSMContext):
    admin_id = 1567764330
    main_admin = 5769116402
    if message.from_user.id == admin_id or message.from_user.id == main_admin:
        await message.answer("Iltimos, foydalanuvchilarga yubormoqchi bo'lgan postni jo'nating")   
        await state.set_state(StepsForm.GET_POST)

async def send_post(message: Message, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM ids")
    user_ids = [row[0] for row in cursor.fetchall()]
    for n in user_ids:
        if message.text:
            await bot.send_message(chat_id = n, text=message.text)
        if message.voice:
            await bot.send_audio(chat_id=n, audio=message.voice.file_id, caption=message.caption)
        if message.video:
            await bot.send_video(chat_id=n, video=message.video.file_id, caption=message.caption)
        if message.photo:
            await bot.send_photo(chat_id=n, photo=message.photo[-1].file_id, caption=message.caption)
        if message.video_note:
            await bot.send_video_note(chat_id=n, video_note=message.video_note.file_id)
        if message.document:
            await bot.send_video(chat_id=n, video=message.document.file_id, caption=message.caption)
        if message.audio:
            await bot.send_audio(chat_id=n, audio=message.audio.file_id, caption=message.caption)

    await state.clear()

async def edite_referral(message: Message, state: FSMContext):
    await message.answer("Iltimos referral balini o'zgartirmoqchi bo'lgan foydalanuvchini ID sini kiriting. U 10 xonalik sondan iborat bo'lishi kerak 😉")
    await state.set_state(StepsForm.EDIT_REFERRAL)

async def edit_referral(message: Message, state: FSMContext):
    global text_id
    text_id = message.text
    if text_id.isdigit and len(text_id) == 10:
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (text_id,))
        res = cursor.fetchone()
        if res is None:
            await message.answer("Bunday foydalanuvchi topilmadi. Iltimos ID ni to'g'ri kiriting❕")
        else:
            await message.answer("Referral balini nechchiga teng qilishni hohlaysiz. Iltimos raqamda kiriting 😉")
            await state.set_state(StepsForm.EDIT_REFERRAL_COUNT)
    else:
        await message.answer("Iltimos faqat 10 xonalik son kiriting❕")

async def edit_referral_count(message: Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        cursor.execute("UPDATE users SET referral_count = ? WHERE user_id = ?", (text, text_id))
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (text_id,))
        resul = cursor.fetchone()
        db.commit()
        await message.answer(f"Foydalanuvchi {resul[0]} {resul[2]}ning referral bali {text} ga o'zgartirildi✍️", reply_markup=admin)
        await state.clear()
    else:
        await message.answer("Iltimos faqat raqam kiriting❕")