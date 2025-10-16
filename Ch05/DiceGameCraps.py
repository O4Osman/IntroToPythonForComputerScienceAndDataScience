"""Simulating the dice game Craps."""
import random
import matplotlib.pyplot as plt
import numpy as np
import random 
import seaborn as sns
import sys
import statistics

winning_rolls = [0] * 13
loosing_rolls = [0] * 13
twelve_plus_wins = 0 
twelve_plus_looses = 0 
counter = 1

for _ in range(int(sys.argv[1])):
    counter = 1
    def roll_dice():
        """Roll two dice and return their face values as a tuple."""
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        return (die1, die2)  # pack die face values into a tuple

    def display_dice(dice):
        """Display one roll of the two dice."""
        die1, die2 = dice  # unpack the tuple into variables die1 and die2
        print(f'Player rolled {die1} + {die2} = {sum(dice)}')

    die_values = roll_dice()  # first roll
    display_dice(die_values)

    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11):  # win
        winning_rolls[counter] += 1
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        loosing_rolls[counter] += 1
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        print('Point is', my_point)

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        display_dice(die_values)
        sum_of_dice = sum(die_values)
    
        counter += 1
    
        if sum_of_dice == my_point:  # win by making point
            if counter > 12:
                twelve_plus_wins += 1
            else:
                winning_rolls[counter] += 1
            game_status = 'WON'
        elif sum_of_dice == 7:  # lose by rolling 7
            if counter > 12:
                twelve_plus_looses += 1
            else:
                loosing_rolls[counter] += 1
            game_status = 'LOST'

    # display "wins" or "loses" message
    if game_status == 'WON':
        print('Player wins')
    else:
        print('Player loses')
        
del winning_rolls[0]    # Becuase 0th index will always be null 0 and we don't need that in our program
del loosing_rolls[0]    # Becuase 0th index will always be null 0 and we don't need that in our program


# Finding Mean, Median and Mode of winning games
temp_winning = []
for index, value in enumerate(winning_rolls):
    temp_winning += [index+1] * value

temp_winning += [13] * twelve_plus_wins

print(f'Winning Mean: {statistics.mean(temp_winning)}')
print(f'Winning Median: {statistics.median(temp_winning)}')
print(f'Winning Mode: {statistics.mode(temp_winning)}')

# Finding Mean, Median and Mode of loosing games
temp_loosing = []
for index, value in enumerate(loosing_rolls):
    temp_loosing += [index+1] * value

temp_loosing += [13] * twelve_plus_looses

print(f'Loosing Mean: {statistics.mean(temp_loosing)}')
print(f'Loosing Median: {statistics.median(temp_loosing)}')
print(f'Loosing Mode: {statistics.mode(temp_loosing)}')

# Winning/Loosing Percentage
print(f'Winning Percentage: {(sum(winning_rolls, twelve_plus_wins )/int(sys.argv[1])) * 100}')
print(f'Loosing Percentage: {(sum(loosing_rolls, twelve_plus_looses)/int(sys.argv[1])) * 100}')

values = []    # roll number
frequencies = []    # frequncy of win and lose at each roll number
counter = 1

# Preparing values and frequencies for barplot
for t in zip(winning_rolls,loosing_rolls):
    values += [f'W: {counter}']
    frequencies += [t[0]]
    values += [f'L: {counter}']
    frequencies += [t[1]]
    counter += 1

# Adding Value and frequency of winning and loosing after 12+ dice rolls
values += [f'W: 12+']
values += [f'L: 12+']
frequencies += [twelve_plus_wins]
frequencies += [twelve_plus_looses]


title = f'Rolling a Die {int(sys.argv[1]):,} Times For Dice Game Craps'
sns.set_style('whitegrid')  # white backround with gray grid lines
axes = sns.barplot(x=frequencies, y=values, palette='bright', orient='horizontal')  # create bars
axes.set_title(title)  # set graph title
axes.set(xlabel='Frequeny', ylabel='Die Roll Value')  # label the axes

# # scale y-axis by 10% to make room for text above bars
axes.set_xlim(0,  max(frequencies) * 1.10)

# display frequency & percentage above each patch (bar)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_width()
    text_y = bar.get_y()
    text = f'{frequency:,} - {frequency / int(sys.argv[1]):.0%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='left', va='top')

plt.show()  # display graph 