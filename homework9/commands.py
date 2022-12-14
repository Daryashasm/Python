import asyncio
import random

import view
from create_bot import dp
from aiogram import types

import model
from create_bot import bot

async def start(message: types.Message):
    player = message.from_user
    model.set_player(player)
    await view.hello(message)
    await asyncio.sleep(3)
    dp.register_message_handler(player_turn)
    first_turn = random.randint(0,1)
    if first_turn:
        await await_player(player)
    else:
        await enemy_turn(player)

async def player_turn(message: types.Message):
    player = message.from_user
    model.set_player(player)
    if (message.text).isdigit():
        if 0 < int(message.text) < 29:
            total_count = model.get_total_candies()
            player_take = int(message.text)
            total = total_count - player_take
            await bot.send_message(player.id, f'{player.first_name} взял(а) {player_take} конфет, '
                                              f'и на столе осталось {total}')
            if model.check_win(total):
                await bot.send_message(player.id, f'Ура! Ты {player.first_name} сегодня съешь все конфеты!')
                return
            model.set_total_candies(total)
            await enemy_turn(player)

        else:
            await bot.send_message(message.from_user.id, 'Хм, можно взять любое количество конфет от 1 до 28 включительно, попробуй еще раз!')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, '
                                                     f'количество измеряется в цифрах, попробуй еще раз.')

async def enemy_turn(player):
    total_count = model.get_total_candies()
    if total_count < 29:
        enemy_take = total_count
    else:
        enemy_take = (total_count - 1)%28
    total = total_count - enemy_take
    await bot.send_message(player.id, f'Бот взял {enemy_take} конфет, '
                                      f'и на столе осталось {total}.')
    if model.check_win(total):
        await bot.send_message(player.id, f'{player.first_name}, Бот победил, '
                                          f'а тебе повезет в любви <3')
        return
    model.set_total_candies(total)
    await asyncio.sleep(1)
    await await_player(player)

async def await_player(player):
    max_take = model.get_max_take()
    await bot.send_message(player.id,
                           f'{player.first_name}, бери конфеты, но не больше {max_take}')

