import matplotlib.pyplot as plt
import numpy as np

# Sample data for two sets of bars
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values_set1 = [20, 35, 30, 25]
values_set2 = [15, 28, 32, 20]

# Bar width and positions
bar_width = 0.35
bar_positions_set1 = np.arange(len(categories))
bar_positions_set2 = bar_positions_set1 + bar_width

# Creating the bar graph with overlay
plt.bar(bar_positions_set1, values_set1, width=bar_width, label='Set 1')
plt.bar(bar_positions_set2, values_set2, width=bar_width, label='Set 2')

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph with Overlay')
plt.xticks(bar_positions_set1 + bar_width / 2, categories)
plt.legend()

# Displaying the plot
plt.show()
