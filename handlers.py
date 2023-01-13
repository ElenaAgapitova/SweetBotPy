from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from infrastructure import dp
import random
import text
import game
import player
import bot_raccon
import game_over


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    name = message.from_user.first_name
    await message.answer(text=f'{name}{text.greetings}')


@dp.message_handler(commands=['rules_game'])
async def rules_game(message: Message):
    name = message.from_user.first_name
    await message.answer(text=f'{name}{text.rules}')


@dp.message_handler(commands=['new_game'])
async def start_new_game(message: Message):
    game.new_game()
    await message.answer(f'На столе лежит {game.get_total()} конфет. Погнали!')
    if game.check_game():
        toss = random.randint(0, 1)
        if toss:
            await player.player_turn(message)
        else:
            await bot_raccon.bot_turn(message, random.randint(1, 28))


@dp.message_handler()
async def take(message: Message):
    name = message.from_user.first_name
    if game.check_game():
        if message.text.isdigit():
            take = int(message.text)
            if (game.get_total() - take) < 0:
                await message.answer(f'{name} хочет взять {take}, но на столе всего - '
                                     f'{game.get_total()}. \n\nВозьми поменьше, не жадничай!:).')
            elif take <= 0:
                await message.answer("Что-то тут не то! Введи число конфет от 1 до 28!")
            elif 0 < take < 29:
                game.take_candies(take)
                if await game_over.check_win(message, take, 'player'):
                    return
                await message.answer(f'{name} взял(а) - {take}, и на столе осталось - '
                                     f'{game.get_total()}. Ходит Енот.')
                await bot_raccon.bot_turn(message, take)
            else:
                await message.answer("Что-то много! Можно брать не более 28.")
        else:
            await message.answer("Что-то тут не то! Введи число конфет от 1 до 28!")
    else:
        await message.answer(f"{name}, \nЕнот хочет поиграть с тобой:)\n\n{text.menu}")
