import random


def get_choices():
    options = ['rock', 'scissors', 'paper']

    player_choice: str = input('Enter a choice [rock, paper, scissors]\n')
    computer_choice: str = random.choice(options)

    selected_choices: dict = {
        'player': player_choice,
        'computer': computer_choice
    }

    return selected_choices


def check_win(player: str, computer: str):
    if player == computer:
        return 'It\'s a tie!'
    elif player == 'rock':
        if computer == 'scissors':
            print(f'{player.capitalize()} smashes {computer.capitalize()}. Player wins!')
        else:
            print(f'{computer.capitalize()} covers {player.capitalize()}. Player lose!')
    elif player == 'paper':
        if computer == 'scissors':
            print(f'{computer.capitalize()} cuts {player.capitalize()}. Player lose!')
        else:
            print(f'{player.capitalize()} covers {computer.capitalize()}. Player wins!')
    elif player == 'scissors':
        if computer == 'paper':
            print(f'{player.capitalize()} cuts {computer.capitalize()}. Player wins!')
        else:
            print(f'{computer.capitalize()} smashes {player.capitalize()}. Player lose!')


choices: dict = get_choices()
player: str = choices['player']
computer: str = choices['computer']

check_win(player, computer)
