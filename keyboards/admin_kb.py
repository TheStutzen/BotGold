from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



#button admin
load = KeyboardButton('Добавить')
delete = KeyboardButton('Удалить')
adminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(load, delete)