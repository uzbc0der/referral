from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import sqlite3
from keyboards.inline import channel
from keyboards.reply import buttons, admin
from utils.states import StepsForm


db = sqlite3.connect('my_database.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id int, username text, name text, referral_count integer DEFAULT 0, phone text, adress text)')
cursor.execute('CREATE TABLE IF NOT EXISTS ids (user_id int)')

async def get_start(message: Message, bot: Bot, state: FSMContext):
    global text
    text = message.text
    global user_id
    user_id = message.from_user.id
    global username
    username = message.from_user.username
    global name
    name = message.from_user.first_name
    cursor.execute('SELECT * FROM ids WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()

    if result is None:
        cursor.execute('INSERT INTO ids VALUES (?)', (user_id,))
        db.commit()

    member1 = await bot.get_chat_member(chat_id="@Azizbek_Sharifboyev", user_id=user_id)
    member2 = await bot.get_chat_member(chat_id="@Wegroup_uz", user_id=user_id)
    member3 = await bot.get_chat_member(chat_id="@Tomchikitoblari", user_id=user_id)
    admin_id = 1567764330
    admin_id1 = 5769116402
    if message.from_user.id == admin_id or message.from_user.id == admin_id1:
        await message.answer("<b>🤗 Assalomu aleykum\n\n📚 ”Ilmga Sodiq Insonlar”</b> nomi ostidagi <b>manfaatli konkursga</b> qatnashish uchun <b>hush kelibsiz!</b>", reply_markup=admin, parse_mode="HTML")
    else: 
        if member3.status == "left":
            await message.answer("<b>🤗 Assalomu aleykum\n\n📚 ”Ilmga Sodiq Insonlar”</b> nomi ostidagi <b>manfaatli konkursga</b> qatnashish uchun <b>hush kelibsiz! </b>\n\nBotdan foydalanish uchun kanalga azo' bo'ling 👇", reply_markup=channel, parse_mode="HTML")
        else :                
            await message.answer("<b>🤗 Assalomu aleykum\n\n📚 ”Ilmga Sodiq Insonlar”</b> nomi ostidagi <b>manfaatli konkursga</b> qatnashish uchun <b>hush kelibsiz!</b>", parse_mode="HTML")
            if len(text) > 10:
                referral = text[-10:]
                cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
                result = cursor.fetchone()
                if result is not  None:
                    await message.answer(f"<b>Quyidagi menudan kerakli bo`limni tanlang 👇</b>", reply_markup=buttons, parse_mode="HTML")
                else :
                    await message.answer(f"😊 Ism-familiyangizni kiriting")
                    await state.set_state(StepsForm.GET_NAME)
                    cursor.execute('SELECT * FROM users WHERE user_id = ?', (referral,))
                    result = cursor.fetchone()

                    if result is None:
                        pass
                    else :
                        cursor.execute('UPDATE users SET referral_count = referral_count + 1 WHERE user_id = ?', (referral,))
                        cursor.execute('INSERT INTO users (user_id, username, name, referral_count) VALUES (?, ?, ?, ?,?,?)', (user_id, username, None, 0,None,None))

                db.commit()
            else:
                cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
                result = cursor.fetchone()
                if result is None:
                    cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?,?,?)', (user_id, username, None, 0,None,None))
                    db.commit()
                    await message.delete()
                    await message.answer(f"😊 Ism-familiyangizni kiriting")
                    await state.set_state(StepsForm.GET_NAME)
                else:
                    await message.delete()
                    await message.answer(f"Quyidagi menudan kerakli bo`limni tanlang 👇", reply_markup=buttons)


async def callback_handler(call: CallbackQuery, bot: Bot, state: FSMContext):
    member1 = await bot.get_chat_member(chat_id="@Azizbek_Sharifboyev", user_id=user_id)
    member2 = await bot.get_chat_member(chat_id="@Wegroup_uz", user_id=user_id)
    member3 = await bot.get_chat_member(chat_id="@Tomchikitoblari", user_id=user_id)
    if member1.status == "left" and member2.status == "left" and member3.status == "left":
        await call.message.delete()
        await call.message.answer("Ilitmos kanalga a'zo boling!", reply_markup=channel)
    else:        
        if len(text) > 10:
            referral = text[-10:]
            cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            if result is not None:
                await call.message.delete()
                await call.message.answer(f"Quyidagi menudan kerakli bo`limni tanlang 👇", reply_markup=buttons)
            else :
                await call.message.answer(f"😊 Ism-familiyangizni kiriting")
                await state.set_state(StepsForm.GET_NAME)
                cursor.execute('SELECT * FROM users WHERE user_id = ?', (referral,))
                result = cursor.fetchone()

                if result is None:
                    pass
                else :
                    cursor.execute('UPDATE users SET referral_count = referral_count + 1 WHERE user_id = ?', (referral,))
                    cursor.execute('INSERT INTO users (user_id, username, name, referral_count) VALUES (?, ?, ?, ?,?,?)', (user_id, username, None, 0,None,None))

            db.commit()
        else:
            cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            if result is None:
                cursor.execute('INSERT INTO users VALUES (?,?,?,?)', (user_id, username, None, 0))
                db.commit()
                await call.message.delete()
                await call.message.answer(f"😊 Ism-familiyangizni kiriting")
                await state.set_state(StepsForm.GET_NAME)
            else:
                await call.message.delete()
                await call.message.answer(f"Quyidagi menudan kerakli bo`limni tanlang 👇", reply_markup=buttons)

async def get_name(message: Message, state: FSMContext):
    text = message.text
    if " " in text:
        cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (text, message.from_user.id,))
        db.commit()
        await message.answer("☎️ Telefon raqamingizni kiriting")
        await state.set_state(StepsForm.GET_PHONE)
    else : 
        await message.answer(f"Ism va familiyangizni kiriting. Misol <i>Pavel Durov</i>", parse_mode="HTML")

async def get_phone(message: Message, state: FSMContext):
    phone = message.text
    if phone[4:].isdigit() or phone.isdigit() and len(phone) == 13 or len(phone)==9:
        cursor.execute("UPDATE users SET phone = ? WHERE user_id = ?", (phone, message.from_user.id,))
        db.commit()
        await message.answer("🏢 Manzilingizni kiriting")
        await state.set_state(StepsForm.GET_ADRESS)
    else:
        await message.answer("Raqam kiriting. Misol <i>+998881234567 yoki 881234567</i>", parse_mode="HTML")

async def get_adress(message: Message, state: FSMContext):
    adress = message.text
    cursor.execute("UPDATE users SET adress = ? WHERE user_id = ?", (adress, message.from_user.id,))
    db.commit()
    await message.answer(f"<b>🚀 Tabriklaymiz!\n\n🫵 Siz konkursga mufaqqiyatli ro’yxatdan o’tdingiz</b>", parse_mode="HTML")
    await message.answer(f"Quyidagi menudan kerakli bo`limni tanlang 👇", reply_markup=buttons)