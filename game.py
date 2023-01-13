start_total = 150
game = False

def get_total():
    global total
    return total

def take_candies(take: int):
    global total
    total -= take
    return total

def check_game():
    global game
    return game

def new_game():
    global game
    global total
    if game:
        game = False
    else:
        game = True
        total = start_total


