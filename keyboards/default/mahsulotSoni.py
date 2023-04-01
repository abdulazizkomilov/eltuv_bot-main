from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = []
keyboard_2 = []
keyboard_3 = []

for i in range(1, 10):
    if i == 1 or i == 2 or i == 3:
        keyboard.append(
            KeyboardButton(text=f'{i}')
        )
    elif i == 4 or i == 5 or i == 6:
        keyboard_2.append(
            KeyboardButton(text=f'{i}')
        )
    elif i == 7 or i == 8 or i == 9:
        keyboard_3.append(
            KeyboardButton(text=f'{i}')
        )


mah_miqdori = ReplyKeyboardMarkup(
    keyboard=[
        keyboard,
        keyboard_2,
        keyboard_3,
        [
            KeyboardButton(text='🛒 Korzina'),
            KeyboardButton(text='🏠 Bosh menyu')
        ]
    ],
    resize_keyboard=True,
    row_width=2

)


mah_miqdori_rus = ReplyKeyboardMarkup(
    keyboard=[
        keyboard,
        keyboard_2,
        keyboard_3,
        [
            KeyboardButton(text='🛒 Корзина'),
            KeyboardButton(text='🏠 Главное меню')
        ]
    ],
    resize_keyboard=True,
    row_width=2

)