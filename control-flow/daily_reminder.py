# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
reminder = f"Reminder: '{task}' is a {priority} priority task"

match priority:
    case "high":
        reminder += " that requires immediate attention"
    case "medium":
        reminder += " that should be done soon"
    case "low":
        reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered. Please enter high, medium, or low."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " today!"

# Print the customized reminder
print(reminder)
