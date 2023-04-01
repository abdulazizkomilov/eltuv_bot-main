from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='🍔 Buyurtma berish')
            ],
            [
                KeyboardButton(text='🛒 Korzina'),
                KeyboardButton(text='📦 Buyurtmalarim'),
            ],
            [
                KeyboardButton(text='⚙ Sozlamalar'),
                KeyboardButton(text='ℹ Biz haqimizda')
            ]
        ],
        resize_keyboard=True
    )

menu_rus = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='🍔 Заказать')
            ],
            [
                KeyboardButton(text='🛒 Корзина'),
                KeyboardButton(text='📦 Мои заказы'),
            ],
            [
                KeyboardButton(text='⚙ Настройки'),
                KeyboardButton(text='ℹ О нас')
            ]
        ],
        resize_keyboard=True
    )