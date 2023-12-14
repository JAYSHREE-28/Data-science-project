# 1.3.	Importing Packages Python
# Example 1: Importing a specific module from a package
import math

# Using functions from the math module
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

# Example 2: Importing the entire module
import random

# Using functions from the random module
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

# Example 3: Importing a module with an alias
import datetime as dt

# Using functions from the datetime module with the alias
current_time = dt.datetime.now()
print("Current time:", current_time)

# Example 4: Importing specific items from a module
from os import path, listdir

# Using functions from the os module
current_directory = path.abspath('.')
print("Current directory:", current_directory)
print("Files in the current directory:", listdir(current_directory))
