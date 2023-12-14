# 1.2.	Executing Commands Python
import subprocess

# Example 1: Run a shell command and capture the output
command_output = subprocess.check_output(["ls", "-l"])
print("Command Output:")
print(command_output.decode("utf-8"))

# Example 2: Run a command with arguments
file_name = "example.txt"
subprocess.run(["touch", file_name])
print(f"Created file: {file_name}")

# Example 3: Run a command with user input
user_input = input("Enter a command: ")
subprocess.run(user_input, shell=True)
