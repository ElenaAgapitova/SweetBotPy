from aiogram.types import Message
import game
import random
import player
import game_over


async def bot_turn(message: Message):
    total = game.get_total()
    if total <= 28:
        take = total
    elif total % 29:
        take = total % 29
    else:
        take = random.randint(1, 28)
    await message.answer(f'Енот взял - {take}, конфет осталось - {game.take_candies(take)}')
    if await game_over.check_win(message, take, 'Енот'):
        return
    await player.player_turn(message)
