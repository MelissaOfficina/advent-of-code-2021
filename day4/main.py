import copy


def check_board_line(board_line):
    for item in board_line:
        if 'x' in item and item.count("x") == len(item):
            return True
    return False


def check_board_column(board_column):
    turned_list = copy.deepcopy(board_column)
    for key, item in enumerate(board_column):
        for k, value in enumerate(item):
            turned_list[key][k] = board_column[k][key]
    return check_board_line(turned_list)


def count_points(board):
    counter = 0
    for item in board:
        for n in item:
            if n != 'x':
                counter += int(n)
    return counter


class Bingo:
    def __init__(self, filename):
        self.filename = filename
        self.first_win = False
        with open(filename, 'r') as my_file:
            self.lines = my_file.readlines()
            self.numbers = self.lines[0].strip("\n").split(',')
            self.lines.pop(0)
            self.boards = self.prepare_boards()

    def start(self, first_win=False):
        self.first_win = first_win
        self.check_winner()

    def prepare_boards(self):
        boards_ = []
        key = 0
        for line in self.lines:
            if line == "\n":
                if len(boards_) > 0:
                    key += 1
                boards_.append([])
            else:
                boards_[key].append(list(line.split()))
        return boards_

    def find_number_in_boards(self, number):
        for_delete = []
        result = False
        for key, board in enumerate(self.boards):
            for k, item in enumerate(board):
                if number in item:
                    self.boards[key][k][item.index(number)] = 'x'
            if check_board_line(board) or check_board_column(board):
                result = count_points(board) * int(number)
                for_delete.append(key)
                if self.first_win:
                    return result

        for_delete.reverse()
        for del_ in for_delete:
            self.boards.pop(del_)
        return result

    def check_winner(self):
        for number in self.numbers:
            if len(self.boards) and (res := self.find_number_in_boards(number)):
                if self.first_win:
                    print(f'Part one result: {res}')
                    return
        print(f'Part two result: {res}')


my_game = Bingo('input.txt')
my_game.start(True)  # first win board
my_game.start()  # last win board
