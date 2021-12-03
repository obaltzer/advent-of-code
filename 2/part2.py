# Initialize state variables
horizontal = 0
vertical = 0
aim = 0

# Interpret commands one by one
for command, value in [l.strip().split() for l in open('input.txt', 'r').readlines()]:
    value = int(value)
    if command == "forward":
        horizontal += value
        vertical += aim * value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value

print(horizontal * vertical)
