from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

channel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="1-kanalga obuna bo'lish", url="https://t.me/Azizbek_Sharifboyev")],
    [InlineKeyboardButton(text="2-kanalga obuna bo'lish", url="https://t.me/Wegroup_uz")],
    [InlineKeyboardButton(text="3-kanalga obuna bo'lish", url="https://t.me/Tomchikitoblari")],
    [InlineKeyboardButton(text="Obuna bo'ldim ✅", callback_data="subscribed")]
])