# 1.5.	Saving Output Python
# Importing necessary modules
import math
import random
import datetime as dt
import csv

# Saving output to a text file
output_file_path = 'output.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write("Hello, this is some text that we're saving to a file.\n")
    output_file.write(f"Square root of 16: {math.sqrt(16)}\n")

# Saving output to a CSV file
csv_file_path = 'output.csv'
data_to_save = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'San Francisco'],
]

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_to_save)

# Saving output to a log file with timestamps
log_file_path = 'log.txt'
current_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log_entry = f"{current_time}: This is a log entry.\n"

with open(log_file_path, 'a') as log_file:
    log_file.write(log_entry)

# Displaying output on the console
print("Output saved to files:")
print(f"- Text file: {output_file_path}")
print(f"- CSV file: {csv_file_path}")
print(f"- Log file: {log_file_path}")
