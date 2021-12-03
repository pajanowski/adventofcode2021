INPUT_PATH = "input_day2.txt"

FORWARD = "forward"
DOWN = "down"
UP = "up"
def get_position_product_from_movements_with_aim(movements):
    x = 0
    aim = 0
    depth = 0
    for movement in movements:
        split = movement.split(" ")
        direction = split[0]
        magnitude = int(split[1])

        if direction == FORWARD:
            x += magnitude
            depth += aim * magnitude
        elif direction == DOWN:
            aim += magnitude
        elif direction == UP:
            aim -= magnitude

    return x * depth


def get_position_product_from_movements(movements):
    x = 0
    depth = 0

    for movement in movements:
        split = movement.split(" ")
        direction = split[0]
        magnitude = int(split[1])

        if direction == FORWARD:
            x += magnitude
        elif direction == DOWN:
            depth += magnitude
        elif direction == UP:
            depth -= magnitude

    return x * depth



if __name__ == '__main__':
    movements = open(INPUT_PATH, "r").read().splitlines()
    print(get_position_product_from_movements_with_aim(movements))