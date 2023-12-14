import matplotlib.pyplot as plt
import numpy as np

# Sample data for two sets of histograms
data_set1 = np.random.normal(0, 1, 1000)  # Generating 1000 random samples from a normal distribution
data_set2 = np.random.normal(3, 1, 1000)  # Generating 1000 random samples from another normal distribution

# Creating histograms with overlay
plt.hist(data_set1, bins=30, alpha=0.5, label='Set 1', color='blue')
plt.hist(data_set2, bins=30, alpha=0.5, label='Set 2', color='green')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram with Overlay')

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()
