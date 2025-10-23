"""Simulating the dice game Craps."""
from matplotlib import animation
import random
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import statistics

winning_rolls = [0] * 13
loosing_rolls = [0] * 13
twelve_plus_wins = 0 
twelve_plus_looses = 0 
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

def play_game():
    global twelve_plus_wins, twelve_plus_looses
    counter = 1
    die_values = roll_dice()  # first roll
    # display_dice(die_values)

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
        # print('Point is', my_point)

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        # display_dice(die_values)
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
    # if game_status == 'WON':
    #     print('Player wins')
    # else:
    #     print('Player loses')

def update(frame_number, number_of_games):
    """Configures bar plot contents for each animation frame."""
    global twelve_plus_wins, twelve_plus_looses

    for _ in range(number_of_games):
        play_game()
        
    values = []    # roll number
    frequencies = []    # frequncy of win and lose at each roll number
    counter = 1
    # Preparing values and frequencies for barplot
    for t in zip(winning_rolls[1:],loosing_rolls[1:]):
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
    
    # reconfigure plot for updated die frequencies
    plt.cla()  # clear old contents of current Figure
    title = f'Rolling a Die {sum(frequencies):,} Times For Dice Game Craps'
    axes = sns.barplot(x=frequencies, y=values, orient='horizontal')  # create bars
    axes.set_title(title)  # set graph title
    axes.set(xlabel='Frequeny', ylabel='Die Roll Value')  # label the axes
    
    # # scale x-axis by 10% to make room for text above bars
    axes.set_xlim(0,  max(frequencies) * 1.3)
    
    # display frequency & percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_width()
        text_y = bar.get_y()
        text = f'{frequency:,} - {frequency / sum(frequencies):.1%}'
        axes.text(text_x, text_y, text, 
                  fontsize=11, ha='left', va='top')

# read command-line arguments for number of frames and rolls per frame
number_of_frames = int(sys.argv[1])  
games_per_frame = int(sys.argv[2])

sns.set_style('whitegrid')  # white background with gray grid lines
figure = plt.figure('Dice Game Craps')  # Figure for animation

# configure and start animation that calls function update
die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames - 1, interval=33,
    fargs=(games_per_frame,))


plt.show()  # display graph 

del winning_rolls[0]    # Becuase 0th index will always be null 0 and we don't need that in our program
del loosing_rolls[0]    # Becuase 0th index will always be null 0 and we don't need that in our program

# # Finding Mean, Median and Mode of winning games
temp_winning = []
for index, value in enumerate(winning_rolls):
    temp_winning += [index+1] * value

temp_winning += [13] * twelve_plus_wins

print(f'Winning Mean: {statistics.mean(temp_winning)}')
print(f'Winning Median: {statistics.median(temp_winning)}')
print(f'Winning Mode: {statistics.mode(temp_winning)}')

# # Finding Mean, Median and Mode of loosing games
temp_loosing = []
for index, value in enumerate(loosing_rolls):
    temp_loosing += [index+1] * value

temp_loosing += [13] * twelve_plus_looses

print(f'Loosing Mean: {statistics.mean(temp_loosing)}')
print(f'Loosing Median: {statistics.median(temp_loosing)}')
print(f'Loosing Mode: {statistics.mode(temp_loosing)}')

# # Winning/Loosing Percentage
total_wins = sum(winning_rolls) + twelve_plus_wins
total_losses = sum(loosing_rolls) + twelve_plus_looses
total_games = int(sys.argv[1]) * int(sys.argv[2])

print(f'Winning Percentage: {(total_wins / total_games) * 100:.2f}')
print(f'Loosing Percentage: {(total_losses / total_games) * 100:.2f}')

