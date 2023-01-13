from aiogram.types import Message
import game
import random
import player
import game_over


async def bot_turn(message: Message, take: int):
    total = game.get_total()
    if 29 < total <= 57:
        take = total-29
    elif total <= 28:
        take = total
    else:
        take = random.randint(1, 28)
    await message.answer(f'Енот взял - {take}, конфет осталось - {game.take_candies(take)}')
    if await game_over.check_win(message, take, 'Енот'):
        return
    await player.player_turn(message)