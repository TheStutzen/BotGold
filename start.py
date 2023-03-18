from aiogram.utils import executor
from create_bot import dp
from base import sqlite_dp
async def on_startup(_):
    print('Бот онлайн')
    sqlite_dp.sql_start()


from handlers import client, admin

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)