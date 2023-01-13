from aiogram.types import Message
import game

async def check_win(message: Message, take: int, player: str):
    name = message.from_user.first_name
    if game.get_total() == 0:
        if player == 'player':
            await message.answer(f'{name} взял(а) {take}. Конфет больше нет!'
                                 f'\n\n{name} одержал(а) победу и забирает все конфеты!'
                                 f'\n\nЕнот просит реванш:) => /new_game')
        else:
            await message.answer(f'\nЕнот победил и забирает все конфеты!'
                                 f'\n\nЕще разок? => /new_game')
        game.new_game()
        return True
    else:
        return False