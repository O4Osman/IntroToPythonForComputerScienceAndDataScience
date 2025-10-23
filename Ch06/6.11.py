# fig04_02.py
"""Simulating the dice game Craps."""
import random
import sys

"""Dictionaries to store rolls for wins and losses"""
wins = {}
losses = {}

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')

def update_wins(counter):
    if counter in wins:
        wins[counter] += 1
    else:
        wins[counter] = 1

def update_losses(counter):
    if counter in losses:
        losses[counter] += 1
    else:
        losses[counter] = 1

for _ in range(int(sys.argv[1])):
    counter = 1
    die_values = roll_dice()  # first roll
    # display_dice(die_values)
    
    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)
    
    if sum_of_dice in (7, 11):  # win
        game_status = 'WON'
        update_wins(counter)
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
        update_losses(counter)
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        # print('Point is', my_point)
    
    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        # display_dice(die_values)
        sum_of_dice = sum(die_values)

        counter +=1 
        
        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
            update_wins(counter)
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'
            update_losses(counter)
    
    # display "wins" or "loses" message
    # if game_status == 'WON':
    #     print('Player wins')
    # else:
    #     print('Player loses')

wins_total = sum(wins.values())
losses_total = sum(losses.values())

wins_percentage = wins_total / int(sys.argv[1]) * 100
losses_percentage = losses_total / int(sys.argv[1]) * 100

print(f'Percentage of wins: {wins_percentage:.1f}%')
print(f'Percentage of losses: {losses_percentage:.1f}%')
print('Percentage of wins/losses based on total number of rolls')
all_rolls = sorted(wins.keys() | losses.keys())
print('Rolls\t\t% Resolved on this roll\t\tCumulative % of games resolved')
total_games = 0
for roll in all_rolls:
    total_wins_losses = 0
    if roll in wins:
        total_wins_losses += wins[roll]
    if roll in losses:
        total_wins_losses += losses[roll]
    total_games += total_wins_losses
    roll_percentage = total_wins_losses/int(sys.argv[1]) * 100
    total_percentage = total_games/int(sys.argv[1]) * 100
    print(f'{roll:>5}\t\t{roll_percentage:>23.2f}%\t\t{total_percentage:>20.2f}%')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
