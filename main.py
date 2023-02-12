import random


def get_choices():
    options = ['rock', 'scissors', 'paper']

    player_choice = input('Enter a choice [rock, paper, scissors]\n')
    computer_choice = random.choice(options)

    selected_choices = {
        'player': player_choice,
        'computer': computer_choice
    }

    return selected_choices


choices: dict = get_choices()
print(choices)
