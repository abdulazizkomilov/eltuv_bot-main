import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from keyboards.default.mahsulotSoni import mah_miqdori, mah_miqdori_rus
from keyboards.default.newkeyboards import menu, menu_rus
from keyboards.default.orderkeyboards import but, but_rus
from states.orderState import OrderData
from loader import dp, bot
from save import save_korzina
from handlers.users.start import users
from data.config import ADDRES

@dp.message_handler(state=OrderData.category)
async def products(message: types.Message, state: FSMContext):
    lang = users[message.from_user.id].get('lang', '-')
    if message.text == '🏠 Bosh menyu' or message.text == '🏠 Главное меню':
        if lang == 'rus':
            await message.answer('🏠 Главное меню', reply_markup=menu_rus)
        else:
            await message.answer('🏠 Bosh menu', reply_markup=menu)
        await state.finish()

    elif message.text == '⬅️ Orqaga' or message.text == '⬅️ Назад':
        if lang == 'rus':
            await message.answer('🏠 Главное меню', reply_markup=menu_rus)
        else:
            await message.answer('🏠 Bosh menu', reply_markup=menu)
        await state.finish()
    try:
        data = requests.get(f'{ADDRES}category/{message.text}').json()
        keyboard_2 = []
        keyboard_3 = []
        keyboard_4 = []
        keyboard_5 = []
        keyboard_6 = []
        keyboard_7 = []
        keyboard_8 = []
        keyboard_9 = []
        keyboard_10 = []
        keyboard_11 = []
        keyboard_12 = []
        keyboard_13 = []
        keyboard_14 = []
        keyboard_15 = []
        keyboard_16 = []
        if data:
            for x in data:
                keyboard_2.append(KeyboardButton(text=f"{x['title']}"))
                if len(keyboard_2) > 2 and keyboard_2:
                    keyboard_3.append(keyboard_2.pop())
                if len(keyboard_3) > 2 and keyboard_3:
                    keyboard_4.append(keyboard_3.pop())
                if len(keyboard_4) > 2 and keyboard_4:
                    keyboard_5.append(keyboard_4.pop())
                if len(keyboard_5) > 2 and keyboard_5:
                    keyboard_6.append(keyboard_5.pop())
                if len(keyboard_6) > 2 and keyboard_6:
                    keyboard_7.append(keyboard_6.pop())
                if len(keyboard_7) > 2 and keyboard_7:
                    keyboard_8.append(keyboard_7.pop())
                if len(keyboard_8) > 2 and keyboard_8:
                    keyboard_9.append(keyboard_8.pop())
                if len(keyboard_9) > 2 and keyboard_9:
                    keyboard_10.append(keyboard_9.pop())
                if len(keyboard_10) > 2 and keyboard_10:
                    keyboard_11.append(keyboard_10.pop())
                if len(keyboard_11) > 2 and keyboard_11:
                    keyboard_12.append(keyboard_11.pop())
                if len(keyboard_12) > 2 and keyboard_12:
                    keyboard_13.append(keyboard_12.pop())
                if len(keyboard_13) > 2 and keyboard_13:
                    keyboard_14.append(keyboard_13.pop())
                if len(keyboard_14) > 2 and keyboard_14:
                    keyboard_15.append(keyboard_14.pop())
                if len(keyboard_15) > 2 and keyboard_15:
                    keyboard_16.append(keyboard_15.pop())
                prod_key = ReplyKeyboardMarkup(
                    keyboard=[
                            keyboard_2, keyboard_3, keyboard_4, keyboard_5, keyboard_6, keyboard_7, keyboard_8, keyboard_9, keyboard_10,
                            keyboard_11, keyboard_12, keyboard_13, keyboard_14, keyboard_15, keyboard_16,
                            [
                                KeyboardButton(text='🏠 Bosh menyu'),
                                KeyboardButton(text='⬅️ Orqaga')
                            ],
                    ],
                    resize_keyboard=True,
                    row_width=2
                )
                prod_key_rus = ReplyKeyboardMarkup(
                    keyboard=[
                        keyboard_2, keyboard_3, keyboard_4, keyboard_5, keyboard_6, keyboard_7, keyboard_8, keyboard_9, keyboard_10,
                        keyboard_11, keyboard_12, keyboard_13, keyboard_14, keyboard_15, keyboard_16,
                        [
                            KeyboardButton(text='🏠 Главное меню'),
                            KeyboardButton(text='⬅️ Назад')
                        ],
                    ],
                    resize_keyboard=True,
                    row_width=2
                )
            await bot.send_chat_action(message.chat.id, 'typing')
            if lang == 'rus':
                await message.answer('Продукты', reply_markup=prod_key_rus)
            else:
                await message.answer('Mahsulotlar', reply_markup=prod_key)
            await OrderData.products.set()
    except:
        pass


@dp.message_handler(state=OrderData.products)
async def products_detail(message: types.Message, state: FSMContext):
    lang = users[message.from_user.id].get('lang', '-')
    detail_prod = requests.get(f'{ADDRES}product/?q={message.text}').json()
    if message.text == '🏠 Bosh menyu' or message.text == '🏠 Главное меню':
        if lang == 'rus':
            await message.answer('🏠 Главное меню', reply_markup=menu_rus)
        else:
            await message.answer('🏠 Bosh menu', reply_markup=menu)
        await state.finish()

    elif message.text == '⬅️ Orqaga' or message.text == '⬅️ Назад':
        if lang == 'rus':
            await message.answer('Категории', reply_markup=but_rus)
        else:
            await message.answer('Categories', reply_markup=but)
        await OrderData.category.set()

    for y in detail_prod:
        if str(message.text) == str(y['title']):
            photo = f"{y['image']}"
            print(photo)
            text = f"{y['title']}\n{y['description']}\n {y['price']:,}sum"
            await message.answer_photo(photo=photo, caption=text)
            if lang == 'rus':
                await message.answer('Выберите или введите сумму', reply_markup=mah_miqdori_rus)
            else:
                await message.answer('Miqdorini tanlang yoki kiriting', reply_markup=mah_miqdori)
            await OrderData.detail.set()
            await state.update_data(
                {
                    "title": y['title'],
                    "price": y['price']
                }
            )


@dp.message_handler(state=OrderData.detail)
async def products_detail(message: types.Message, state: FSMContext):
    lang = users[message.from_user.id].get('lang', '-')
    try:
        if message.text == '🏠 Bosh menyu' or message.text == '🏠 Главное меню':
            if lang == 'rus':
                await message.answer('🏠 Главное меню', reply_markup=menu_rus)
            else:
                await message.answer('🏠 Bosh menu', reply_markup=menu)
            await state.finish()

        elif message.text == '🛒 Korzina' or message.text == '🛒 Корзина':
            if lang == 'rus':
                await message.answer('🏠 Главное меню', reply_markup=menu_rus)
            else:
                await message.answer('🏠 Bosh menu', reply_markup=menu)
            await state.finish()
        elif int(message.text):
            data = await state.get_data()
            save_korzina(message, data.get("title"), data.get("price"), message.text)
            if lang == 'rus':
                await message.answer('Товар добавлен в корзину, что нибудь еще?', reply_markup=but_rus)
            else:
                await message.answer('Mahsulot savatchaga qoshildi, davom etamizmi?', reply_markup=but)
            await OrderData.category.set()
    except:
        if lang == 'rus':
            await message.answer('ошибка')
        else:
            await message.answer('Siz noto\'g\'ri malimot kiritdingiz. Miqdorini tanlang yoki kiriting!')
