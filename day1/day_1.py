
input_file = "input_day1.txt"

def get_sum_of_sliding_windows(array):
    ret = []
    for i in range(0, len(array) - 2):
        add = 0
        for j in range(0, 3):
            add += int(array[i + j])
        ret.append(add)
    return ret

def get_number_of_decreases(array):
    counter = 0
    for i in range(1, len(array)):
        if int(array[i]) > int(array[i-1]):
            counter += 1
    return counter


def part1():
    test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    test_output = 7
    assert get_number_of_decreases(test_input) == test_output
    f = open(input_file, "r").read().splitlines();
    print(get_number_of_decreases(f))


def run():
    part2()


def part2():
    test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    test_window_sum_output = [607, 618, 618, 617, 647, 716, 769, 792]
    actual = get_sum_of_sliding_windows(test_input)
    assert actual == test_window_sum_output
    f = open(input_file, "r").read().splitlines()
    sums = get_sum_of_sliding_windows(f)
    print(get_number_of_decreases(sums))


if __name__ == "__main__":
    run()
