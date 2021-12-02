def check_directions(li):
    x = 0
    y = 0
    for command in li:
        command = command[:-1] if "\n" in command else command
        direction = command[:-2]
        points = int(command[-1])
        if direction == "forward":
            x += points
        elif direction == "up":
            y -= points
        elif direction == "down":
            y += points
    print(f'Part One: horizontal = {x}, depth = {y}')
    return x * y


def check_directions_aim(li):
    x = 0
    y = 0
    aim = 0
    for command in li:
        command = command[:-1] if "\n" in command else command
        direction = command[:-2]
        points = int(command[-1])
        if direction == "forward":
            x += points
            y += aim * points
        elif direction == "up":
            aim -= points
        elif direction == "down":
            aim += points
    print(f'Part Two: horizontal = {x}, depth = {y}')
    return x * y


with open('day2_data.txt', 'r') as my_file:
    my_list = my_file.readlines()
    print(f'Part One result: {check_directions(my_list)}')
    print(f'Part Two result: {check_directions_aim(my_list)}')
