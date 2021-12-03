def actual_count(items):
    counter_ = {}
    for item in items:
        for key, num in enumerate(item.strip("\n")):
            if key not in counter_:
                counter_[key] = {"0": 0, "1": 0}
            counter_[key][num] += 1
    return counter_


def count_values(lines_data):
    count_data = actual_count(lines_data)
    value_gamma = []
    value_epsilon = []
    for key, item in count_data.items():
        if item['0'] > item['1']:
            value_gamma.insert(key, "0")
            value_epsilon.insert(key, "1")
        else:
            value_gamma.insert(key, "1")
            value_epsilon.insert(key, "0")
    value_gamma = ''.join(value_gamma)
    value_epsilon = ''.join(value_epsilon)
    return int(value_gamma, 2) * int(value_epsilon, 2)


def o2_co2_checker(data, type_var, key=0):
    try:
        count_data = actual_count(data)
        item = count_data[key]
        if item['0'] == item['1'] or item['1'] > item['0']:
            search = "0"
            if type_var == "o2":
                search = "1"
        elif item['0'] > item['1']:
            search = "1"
            if type_var == "o2":
                search = "0"
        data = list(filter(lambda var: var[key] == search, data))
        if len(data) == 1:
            return data[0]
        search_var = o2_co2_checker(data, type_var, key + 1)
        return search_var
    except:
        print('Something wrong :(( ')


def filter_values(lines_data):
    o2 = lines_data[:]
    co2 = lines_data[:]
    o2 = o2_co2_checker(o2, 'o2')
    co2 = o2_co2_checker(co2, 'co2')
    return int(o2, 2) * int(co2, 2)


with open('day3_data.txt', 'r') as my_file:
    lines = my_file.readlines()
    print(f'Part One result: {count_values(lines)}')
    print(f'Part Two result: {filter_values(lines)}')
