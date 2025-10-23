# RollDie.py
"""Graphing frequencies of die rolls with Seaborn."""
from matplotlib import animation
import matplotlib.pyplot as plt
import random 
import seaborn as sns
import sys

def update(frame_number, rolls, faces, frequencies):
    """Configures bar plot contents for each animation frame."""
    
    # roll die and update frequencies
    for i in range(rolls):
        roll1 = random.randrange(1, 7)
        roll2 = random.randrange(1, 7)
        frequencies[(roll1 + roll2) - 2] += 1
    
    # reconfigure plot for updated die frequencies
    plt.cla()  # clear old contents of current Figure
    
    title = f'Rolling a Six-Sided Die {sum(frequencies):,} Times'
    axes = sns.barplot(x=frequencies, y=values, palette='bright', orient='horizontal')  # create bars
    axes.set_title(title)  # set graph title
    axes.set(xlabel='Frequency', ylabel='Die Value')  # label the axes
    
    # scale x-axis by 10% to make room for text above bars
    axes.set_xlim(0,  max(frequencies) * 1.10)
    
    # display frequency & percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_width()
        text_y = bar.get_y()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, 
                  fontsize=11, ha='left', va='top')
number_of_frames = int(sys.argv[1])  
rolls_per_frame = int(sys.argv[2])

sns.set_style('whitegrid')  # white background with gray grid lines
figure = plt.figure('Rolling Two Six-Sided Die')  # Figure for animation
values = list(range(2, 13))  # die faces for display on x-axis
frequencies = [0] * 11  #eleven-element list of die frequencies


# configure and start animation that calls function update
die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames - 1, interval=33,
    fargs=(rolls_per_frame, values, frequencies))


plt.show()  # display graph 