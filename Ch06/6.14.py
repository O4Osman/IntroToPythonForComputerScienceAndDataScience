from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns

def update(frame_number, flips, faces, frequencies):
    """Configures bar plot contents for each animation frame."""

    for i in range(flips):
        frequencies[random.randrange(0, 2)] += 1


    # reconfigure plot for updated coin frequencies
    plt.cla() # clear old contents of current Figure
    
    # Title for bar plot
    title = f'Flipping a coin {sum(frequencies):,} Times'
    
    # initializing bar plot
    axes = sns.barplot(x=values, y=frequencies, palette='bright')
    
    #setting the title
    axes.set_title(title)
    
    # setting x and y labels
    axes.set(xlabel='Coin Faces (1=Head, 2=Tail)', ylabel='Frequency')
    
    # increasing y-axis range so the our y-axies values show properly
    axes.set_ylim(top=max(frequencies) * 1.10)
    
    # setting numbers and percentage of flips over each bar
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

number_of_frames = 1999
flips_per_frame = 100

sns.set_style('whitegrid') # white background with gray grid lines
figure = plt.figure('Flipping a coin') # Figure for animation
values = [1, 2] # die faces for display on x-axis
frequencies = [0] * 2 # eleven-element list of die frequencies

# configure and start animation that calls function update
coin_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=33,
    fargs=(flips_per_frame, values, frequencies))
plt.show()  # display window