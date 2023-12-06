from aiogram import Bot, types
from aiogram.types import Message, InputFile
import sqlite3

db = sqlite3.connect('my_database.db')
cursor = db.cursor()

async def get_referral(message: Message, bot: Bot):
    info = await bot.get_me()
    photo = types.input_file.FSInputFile('logo.jpg')
    referral_link = f"https://t.me/{info.username}?start={message.from_user.id}"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=f"<b>🚀 Dunyoda ilk bor MANFAATLI  KONKURS 🎉 </b>\n\n💰 Ko’plab hamkorliklar bilan tashkil etilgan, <b>”Ilmga Sodiq Insonlar”</b> nomi ostidagi <b>manfaatli konkursga</b> start berildi!\n\n🥇1-o’rin-10 ta kitoblar to’plami\n🥈2-o’rin-7 ta kitoblar to’plami\n🥉3-o’rin-5 ta kitoblar to’plami\n🎗4-o’rin-3 ta kitoblar to’plami\n🎗5-o’rin-2 ta kitoblar to’plami\n🎗6-o’rin-1 ta kitoblar to’plami\n\n<b>🏆 Konkursda qatnashish uchun quyidagi havola ustiga bosing👇</b>\n\n{referral_link}", parse_mode="HTML")
    await message.answer(f"👆 Yuqoridagi sizning <b>link/havolangiz.</b> Uni koʼproq tanishlaringizga ulashing. Omad!", parse_mode="HTML")

async def get_condition(message: Message):
    await message.answer("<b>📣 Konkursda qatnashish shartlari bilan tanishing:</b>\n\n1) 🚀 Sizga maxsus havoladan iborat bo’lgan habar yuboriladi\n\n2) 🫵 Siz bu habarni do’stlaringizga yuborasiz\n\n3) 👥 Ulardan bu konkursga qatnashishlarini so’raysiz\n\n4) ✅ So’ng ular ro’yxatdan o’tishsa xar bir ro’yxatdan o’tgan do’stingiz uchun sizga 1ball beriladi\n\n5) 💡 Keyin yana siz do’stlaringizni taklif etishda davom etasiz\n\n6) 🤫 Hamda konkurs 1 oy davom etadi va 1 oydan so’ng eng ko’p ball yig’gan top 6 ta kishiga  sovg’alar ulashiladi!\n\n<b>😉 Shular halos</b>", parse_mode="HTML")

async def get_gifts(message: Message, bot: Bot):
    photo = types.input_file.FSInputFile('logo.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption="<b>🚀 Dunyoda ilk bor MANFAATLI  KONKURS 🎉 </b>\n\n💰 Ko’plab hamkorliklar bilan tashkil etilgan, <b>”Ilmga Sodiq Insonlar”</b> nomi ostidagi <b>manfaatli konkursga</b> start berildi!\n\n🥇1-o’rin-10 ta kitoblar to’plami\n🥈2-o’rin-7 ta kitoblar to’plami\n🥉3-o’rin-5 ta kitoblar to’plami\n🎗4-o’rin-3 ta kitoblar to’plami\n🎗5-o’rin-2 ta kitoblar to’plami\n🎗6-o’rin-1 ta kitoblar to’plami", parse_mode="HTML")

async def get_statistic(message: Message, bot: Bot):
    user_id = message.from_user.id
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    res = cursor.fetchone()
    try: 
        await message.answer(f"📌Sizda {res[3]} ball mavjud.")
    except: 
        await message.answer(f"📌Sizda 0 ball mavjud.")
    db.commit()

async def get_all_statictic(message: Message, bot: Bot):
    userid = message.from_user.id
    admin_id = 1567764330
    admin2_id = 5769116402
    if userid == admin_id or userid == admin2_id:
        cursor.execute('SELECT user_id, username, name, referral_count FROM users ORDER BY referral_count DESC')
        result = cursor.fetchall()
        formatted_results = []
        for i, results in enumerate(result, start=1):
            formatted_results.append(f"{i}) Ism: {results[2]} - {results[0]}\nJalb qilgan odamlar soni🧮 - {results[3]}")

        response = '\n\n'.join(formatted_results)
        await message.answer(f"🏆Top foydalanuvchilar:\n\n{response}")
        db.commit()

    else :
        cursor.execute('SELECT user_id, username, name, referral_count FROM users ORDER BY referral_count DESC')
        result = cursor.fetchall()
        formatted_results = []
        for i, results in enumerate(result, start=1):
            formatted_results.append(f"{i}) Ism: {results[2]}\nJalb qilgan odamlar soni🧮 - {results[3]}")
        response = '\n\n'.join(formatted_results)
        await message.answer(f"🏆Top foydalanuvchilar:\n\n{response}")
        
        db.commit()


