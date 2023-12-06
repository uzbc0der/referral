from aiogram.fsm.state import State, StatesGroup

class StepsForm(StatesGroup):
    GET_NAME = State()
    GET_PHONE = State()
    GET_ADRESS = State()
    GET_POST = State()
    EDIT_REFERRAL = State()
    EDIT_REFERRAL_COUNT = State()