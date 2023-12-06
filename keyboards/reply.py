from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Konkursda qatnashish 🔴")
    ],
    [
        KeyboardButton(text="🎁 Sovg`alar"),
        KeyboardButton(text="👤 Ballarimni ko'rish")
    ],
    [
        KeyboardButton(text="Top foydalanuvchilar 🏆"),
        KeyboardButton(text="🤝 Shartlar")
    ]
], resize_keyboard=True)

admin = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Konkursda qatnashish 🔴")
    ],
    [
        KeyboardButton(text="🎁 Sovg`alar"),
        KeyboardButton(text="👤 Ballarimni ko'rish")
    ],
    [
        KeyboardButton(text="Top foydalanuvchilar 🏆"),
        KeyboardButton(text="🤝 Shartlar")
    ],
    [
        KeyboardButton(text="Foydalanuvchilarga post jo'natish 📮"),
        KeyboardButton(text="Referral tahrir ✍️")    
    ]
], resize_keyboard=True)