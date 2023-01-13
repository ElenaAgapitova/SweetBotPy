from aiogram.types import Message

async def player_turn(message: Message):
    name = message.from_user.first_name
    await message.answer(f'\n{name}, твой ход! Сколько конфет возьмешь?')