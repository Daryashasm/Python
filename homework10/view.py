from aiogram import types
from create_bot import bot

async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, Привет! Сегодня поиграем с конфетками :)'
                                                 f'Если ты сейчас введешь:'
                                                 f'\n/play - то, начнется игра с параметрами: '
                                                 f'\nlevel: easy, всего конфет - 150, можно брать максимум - 28.'
                                                 f'\nЕсли ты хочешь изменить какой-либо параметр, то сначала выполни настройки, '
                                                 f'используя следующие команды:'                                                 
                                                 f'\n/set N - изменить количество конфет, где N - задаваемое число;'
                                                 f'\n/take L - изменить количество конфет,'
                                                 f' которые можно взять ход, где L - задаваемое число;'
                                                 f'\n/level A - туровень сложности, где А - 1: hard, 0: easy.')  