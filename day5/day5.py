TEST_INPUT="test_input.txt"
INPUT="input.txt"
def get_input(input_file_name):
    ret = []
    lines = open(input_file_name, "r").readlines()
    for line in lines:
        line = line.strip()
        start_and_end = line.split(" -> ")
        if len(start_and_end) != 2:
            continue
        print(start_and_end)
        start = start_and_end[0]
        end = start_and_end[1]
        start_coord = start.split(",")
        end_coord = end.strip().split(",")
        if start_coord[0] != end_coord[0] and start_coord[1] == end_coord[1]:
            print(start_coord)
            incrementer = 0
            if int(start_coord[0]) > int(end_coord[0]):
                incrementer = -1
            else:
                incrementer = 1
            i = int(start_coord[0])
            while i != int(end_coord[0]) + incrementer:
                ret.append((i, int(end_coord[1])))
                i += incrementer
        if start_coord[1] != end_coord[1] and start_coord[0] == end_coord[0]:
            incrementer = 0
            if int(start_coord[1]) > int(end_coord[1]):
                incrementer = -1
            else:
                incrementer = 1
            i = int(start_coord[1])
            while i != int(end_coord[1]) + incrementer:
                ret.append((int(start_coord[0]), i))
                i += incrementer
    return ret


def run():
    array = [[0]*1000 for _ in range(1000)]
    #  coordinates = get_input(TEST_INPUT)

    coordinates = get_input(INPUT)
    for coor in coordinates: print(coor)
    for coordinate in coordinates:
        y = coordinate[1]
        x = coordinate[0]
    #      while y >= len(array) - 1:
    #          array.append([])
    #
    #      while x >= len(array[y]) - 1:
    #          array[y].append(0)
        array[y][x] += 1
    output = 0
    for row in array:
        print(row)
        for col in row:
            if col > 1:
                output += 1
    
    print(output)


if __name__ == "__main__":
    run()
