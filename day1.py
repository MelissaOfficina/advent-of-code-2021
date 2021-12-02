from day1_my_list import my_list


def check_previous(some_list):
    counter = 0
    previous = False
    for el in some_list:
        if previous is not False and el > previous:
            counter += 1
        previous = el
    return counter


def check_previous_extended(some_list):
    counter = 0
    previous = False
    length = len(some_list)
    for key, el in enumerate(some_list):
        if key != (length - 1) and key != (length - 2):
            sum_ = el + some_list[key + 1] + some_list[key + 2]
        elif key == (length - 2):
            sum_ = el + some_list[key + 1]
        elif key == (length - 1):
            sum_ = el
        if previous is not False and sum_ > previous:
            counter += 1
        previous = sum_
    return counter


print(f'Sonar Sweep result: {check_previous(my_list)}')
print(f'Sonar Sweep Part Two result: {check_previous_extended(my_list)}')
