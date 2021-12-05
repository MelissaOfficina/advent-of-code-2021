class Graph:
    def __init__(self, filename):
        self.numbers = []
        self.splits = []
        self.coordinates = {}
        with open(filename, 'r') as my_file:
            self.lines = my_file.readlines()
        for line in self.lines:
            self.numbers.append(line.strip("\n").split("->"))

    def splitting(self):
        self.splits = []
        self.coordinates = {}
        for key, arr in enumerate(self.numbers):
            self.splits.append([])
            for k, num in enumerate(arr):
                self.splits[key].append(num.strip(" ").split(","))

    def calculations(self):
        self.splitting()
        for arr in self.splits:
            if arr[0][0] == arr[1][0]:
                range_ = sorted([int(arr[0][1]), int(arr[1][1])])
                for num in range(range_[0], range_[1] + 1):
                    key = arr[0][0] + ':' + str(num)
                    self.update_coordinates(key)
            elif arr[0][1] == arr[1][1]:
                range_ = sorted([int(arr[0][0]), int(arr[1][0])])
                for num in range(range_[0], range_[1] + 1):
                    key = str(num) + ':' + arr[0][1]
                    self.update_coordinates(key)

    def calculations_extended(self):
        self.splitting()
        for arr in self.splits:
            if arr[0][0] == arr[1][0]:
                range_ = sorted([int(arr[0][1]), int(arr[1][1])])
                for num in range(range_[0], range_[1] + 1):
                    key = arr[0][0] + ':' + str(num)
                    self.update_coordinates(key)
            elif arr[0][1] == arr[1][1]:
                range_ = sorted([int(arr[0][0]), int(arr[1][0])])
                for num in range(range_[0], range_[1] + 1):
                    key = str(num) + ':' + arr[0][1]
                    self.update_coordinates(key)
            elif (int(arr[0][0]) + int(arr[0][1])) > (int(arr[1][0]) + int(arr[1][1])):
                while int(arr[0][0]) + int(arr[0][1]) >= int(arr[1][0]) + int(arr[1][1]):
                    key = str(arr[0][0]) + ':' + str(arr[0][1])
                    self.update_coordinates(key)
                    arr[0][0] = int(arr[0][0])
                    arr[0][1] = int(arr[0][1])
                    arr[0][0] -= 1
                    arr[0][1] -= 1
            elif (int(arr[0][0]) + int(arr[0][1])) < (int(arr[1][0]) + int(arr[1][1])):
                while int(arr[0][0]) + int(arr[0][1]) <= int(arr[1][0]) + int(arr[1][1]):
                    key = str(arr[0][0]) + ':' + str(arr[0][1])
                    self.update_coordinates(key)
                    arr[0][0] = int(arr[0][0])
                    arr[0][1] = int(arr[0][1])
                    arr[0][0] += 1
                    arr[0][1] += 1
            elif int(arr[0][0]) >= int(arr[1][0]):
                while int(arr[0][0]) >= int(arr[1][0]):
                    key = str(arr[0][0]) + ':' + str(arr[0][1])
                    self.update_coordinates(key)
                    arr[0][0] = int(arr[0][0])
                    arr[0][1] = int(arr[0][1])
                    arr[0][0] -= 1
                    arr[0][1] += 1
            else:
                while int(arr[0][0]) <= int(arr[1][0]):
                    key = str(arr[0][0]) + ':' + str(arr[0][1])
                    self.update_coordinates(key)
                    arr[0][0] = int(arr[0][0])
                    arr[0][1] = int(arr[0][1])
                    arr[0][0] += 1
                    arr[0][1] -= 1

    def check_result(self, type_=1):
        if type_ == 2:
            self.calculations_extended()
        else:
            self.calculations()
        counter = 0
        for k, v in self.coordinates.items():
            if v >= 2:
                counter += 1
        return counter

    def update_coordinates(self, key):
        if key in self.coordinates:
            self.coordinates[key] += 1
        else:
            self.coordinates.update({key: 1})


graph = Graph('input.txt')
print(f'Part One result: {graph.check_result(1)}')
print(f'Part Two result: {graph.check_result(2)}')
