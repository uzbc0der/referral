from aiogram import Bot, Dispatcher, F
import asyncio
from utils.states import StepsForm
from Handlers.start import *
from Handlers.statistic import *
from Handlers.post import *



async def start():
    bot = Bot(token="6472012771:AAGb5k5V8ZiXA0GflfO8vZ-iTk124UpgnoA")
    dp = Dispatcher()
    dp.message.register(get_start, F.text.startswith('/start') )
    dp.message.register(get_referral, F.text.startswith('Konkursda qatnashish 🔴'))
    dp.message.register(get_gifts, F.text=="🎁 Sovg`alar")
    dp.message.register(get_statistic, F.text.startswith("👤 Ballarimni ko'rish"))
    dp.message.register(get_all_statictic, F.text.startswith('Top foydalanuvchilar 🏆'))
    dp.message.register(get_condition, F.text=="🤝 Shartlar")
    dp.message.register(get_post, F.text=="Foydalanuvchilarga post jo'natish 📮")
    dp.message.register(edite_referral, F.text=="Referral tahrir ✍️")
    dp.message.register(send_post, StepsForm.GET_POST)
    dp.message.register(edit_referral, StepsForm.EDIT_REFERRAL)
    dp.message.register(edit_referral_count, StepsForm.EDIT_REFERRAL_COUNT)
    dp.message.register(get_name, StepsForm.GET_NAME)
    dp.message.register(get_phone, StepsForm.GET_PHONE)
    dp.message.register(get_adress, StepsForm.GET_ADRESS)
    dp.callback_query.register(callback_handler, F.data == "subscribed")
    await dp.start_polling(bot)

asyncio.run(start() )