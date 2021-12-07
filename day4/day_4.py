import copy


class BingoBoard:
    card = []
    marked = [
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]
    ]

    def check_board(self):
        for row in self.marked:
            if self.check_row(row):
                return True

        for i in range(0, 5):
            if self.check_column(i):
                return True

        if self.check_up_down_diagonal():
            return True

        return self.check_down_up_diagonal();

    def check_row(self, row):
        return not False in row

    def check_column(self, column_num):
        for row in self.marked:
            if not row[column_num]:
                return False
        return True

    def check_up_down_diagonal(self):
        i = 0
        while i < 5:
            if not self.marked[i][i]:
                return False
            i += 1
        return True

    def check_down_up_diagonal(self):
        i = 4
        while i > -1:
            if not self.marked[i][i]:
                return False
            i -= 1
        return True

    def mark(self, number):
        for i in range(0, 5):
            for j in range(0, 5):
                if self.card[i][j] == number:
                    self.marked[i][j] = True
                    return

    def sum_unmarked(self):
        ret = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if self.marked[i][j] == False:
                    ret += int(self.card[i][j])
        return ret


def get_boards(text_input_array):
    ret = []
    length_of_input = len(text_input_array)

    i = 2
    while i < length_of_input:
        board = BingoBoard()
        board.card = []
        board.marked = [
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]
    ]

        for j in range(0, 5):
            board.card.append(text_input_array[i].replace("  ", " ").strip().split(" "))
            i += 1
            if i > length_of_input - 1:
                break
        ret.append(board)
        i += 1
    return ret


if __name__ == '__main__':
    # splitlines = open("text_input.txt", "r").read().splitlines()
    splitlines = open("input.txt", "r").read().splitlines()
    bingo_calls = splitlines[0].split(",")
    boards = get_boards(splitlines)
    for call in bingo_calls:
        for board in boards:
            board.mark(call)
            if board.check_board():
                i = board.sum_unmarked() * int(call)
                print(i)
                exit(0)


