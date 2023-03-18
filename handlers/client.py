from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import client_kb as nav
from base import sqlite_dp


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в наш сервисный центр iPachino, выбери устройство:'. format(message.from_user), reply_markup = nav.mainMenu)

#----- Test Values -----
async def menu_chuse(message: types.Message):
    await sqlite_dp.sql_read(message)

async def apple_chuse(message: types.Message):
    if message.text == 'Apple':
        await bot.send_message(message.from_user.id,'Выбери тип устройства:', reply_markup = nav.apple_menu)

async def android_chuse(message: types.Message):   
    if message.text == 'Android':
        await bot.send_message(message.from_user.id,'Выбери бренд:', reply_markup = nav.android_menu)

async def laptop_chuse(message: types.Message):
    if message.text == 'Ноутбук':
        await bot.send_message(message.from_user.id,'Выбери поломку:', reply_markup = nav.laptop_menu)

async def pc_chuse(message: types.Message):
    if message.text == 'Компьютер':
        await bot.send_message(message.from_user.id,'Выбери поломку:', reply_markup = nav.pc_menu)

async def ip_chuse(message: types.Message):
    if message.text == 'iPhone':
        await bot.send_message(message.from_user.id,'У тебя с Кнопкой Home (Touch ID) или без Кнопки Home (Face ID)?', reply_markup = nav.id_menu)

async def home_chuse(message: types.Message):
    if message.text == 'Touch ID':
        await bot.send_message(message.from_user.id,'Выбери свой iPhone:', reply_markup = nav.touch_menu)

async def face_chuse(message: types.Message):
    if message.text == 'Face ID':
        await bot.send_message(message.from_user.id,'Выбери свой iPhone:', reply_markup = nav.face_menu)

async def samsung_chuse(message: types.Message):
    if message.text == 'Samsung':
        await bot.send_message(message.from_user.id,'Выбери поломку:', reply_markup = nav.sam_menu)

async def xiaomi_chuse(message: types.Message):
    if message.text == 'Xiaomi':
        await bot.send_message(message.from_user.id,'Выбери поломку:', reply_markup = nav.xia_menu)

async def honor_chuse(message: types.Message):
    if message.text == 'Honor':
        await bot.send_message(message.from_user.id,'Выбери поломку:', reply_markup = nav.hon_menu)

async def huawei_chuse(message: types.Message):
    if message.text == 'Huawei':
        await bot.send_message(message.from_user.id,'Выбери поломку:', reply_markup = nav.hua_menu)

async def realme_chuse(message: types.Message):
    if message.text == 'Realme':
        await bot.send_message(message.from_user.id,'Выбери поломку:', reply_markup = nav.rea_menu)

async def game_chuse(message: types.Message):
    if message.text == 'Игровая консоль':
        await bot.send_message(message.from_user.id,'Что нужно сделать?', reply_markup = nav.sx_menu)      

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(apple_chuse, text=['Apple'])
    dp.register_message_handler(android_chuse, text=['Android'])
    dp.register_message_handler(laptop_chuse, text=['Ноутбук'])
    dp.register_message_handler(pc_chuse, text=['Компьютер'])
    dp.register_message_handler(ip_chuse, text=['iPhone'])
    dp.register_message_handler(home_chuse, text=['Touch ID'])
    dp.register_message_handler(face_chuse, text=['Face ID'])
    dp.register_message_handler(samsung_chuse, text=['Samsung'])
    dp.register_message_handler(xiaomi_chuse, text=['Xiaomi'])
    dp.register_message_handler(honor_chuse, text=['Honor'])
    dp.register_message_handler(huawei_chuse, text=['Huawei'])
    dp.register_message_handler(realme_chuse, text=['Realme'])
    dp.register_message_handler(game_chuse, text=['Игровая консоль'])
    dp.register_message_handler(menu_chuse, text=['Меню'])