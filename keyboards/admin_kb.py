from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



#button admin
load = KeyboardButton('/Загрузить')
delete = KeyboardButton('/удалить')
adminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(load, delete)