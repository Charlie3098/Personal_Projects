#This program will be a game where you have to guess the card
#that the computer (name not yet decided) has picked

import random

card_list = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']

print('Welcome traveler. I am The Game Master!\n')
print('For today we have a simple guessing game.\n')
print('Pick the correct card and you WIN !\n')
player_choice = input('Simply type the letter/ number of the card and the Suit, eg. AS / 2D:\n')

#GM_turn
def gm_turn():
    gm_choice = random.choice(card_list)
    print(f"I chose {gm_choice}")
    if player_choice == gm_choice:
        print('You Win !!')
    else:
        print('As expected. Better luck next time')

gm_turn()

input('Press enter to exit the game')
