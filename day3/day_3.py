from typing import List


def get_gamma_rate(bits_array):
    gamma_rate_bits = ''
    for i in range(0, len(bits_array[0])):
        count_0 = 0
        count_1 = 0
        for bits in bits_array:
            if bits[i] == '1':
                count_1 += 1
            if bits[i] == '0':
                count_0 += 1
        if count_0 > count_1:
            gamma_rate_bits += '0'
        else:
            gamma_rate_bits += '1'
    out = 0
    for bit in gamma_rate_bits:
        out = (out << 1) | int(bit)
    return out


def get_epsilon_rate(bits_array):
    epsilon_rate_bits = ''
    for i in range(0, len(bits_array[0])):
        count_0 = 0
        count_1 = 0
        for bits in bits_array:
            if bits[i] == '1':
                count_1 += 1
            if bits[i] == '0':
                count_0 += 1
        if count_0 > count_1:
            epsilon_rate_bits += '1'
        else:
            epsilon_rate_bits += '0'
    return bits_to_int(epsilon_rate_bits)


def bits_to_int(bits):
    out = 0
    for bit in bits:
        out = (out << 1) | int(bit)
    return out


def o2_filter(bits_array: List[List[str]]):
    i = 0
    while len(bits_array) > 1:
        for i in range(0, len(bits_array[0])):
            ret = []
            count_0 = 0
            count_1 = 0
            for bits in bits_array:
                if bits[i] == '1':
                    count_1 += 1
                if bits[i] == '0':
                    count_0 += 1
            if count_0 > count_1:
                for bits in bits_array:
                    if bits[i] == '0':
                        ret.append(bits)
            else:
                for bits in bits_array:
                    if bits[i] == '1':
                        ret.append(bits)
            bits_array = ret
    return bits_to_int(bits_array[0])


def co2_filter(bits_array: List[List[str]]):
    i = 0
    while len(bits_array) > 1:
        for i in range(0, len(bits_array[0])):
            ret = []
            count_0 = 0
            count_1 = 0
            for bits in bits_array:
                if bits[i] == '1':
                    count_1 += 1
                if bits[i] == '0':
                    count_0 += 1
            if count_0 < count_1 or count_0 == count_1:
                for bits in bits_array:
                    if bits[i] == '0':
                        ret.append(bits)
            else:
                for bits in bits_array:
                    if bits[i] == '1':
                        ret.append(bits)
            if len(ret) == 0:
                break
            bits_array = ret
    return bits_to_int(bits_array[0])



if __name__ == '__main__':
    test_bits_array = open("test_input.txt", "r").read().splitlines()
    bits_array = open("input_day3.txt", "r").read().splitlines()
    expected_gamma = 22
    expected_epsilon = 9

    actual_gamma = get_gamma_rate(bits_array)
    # assert actual_gamma == expected_gamma
    actual_epsilon = get_epsilon_rate(bits_array)
    # assert actual_epsilon == expected_epsilon

    print(actual_epsilon * actual_gamma)

    o2_rating_expected = 23
    o2_rating_actual = o2_filter(bits_array)
    # assert o2_rating_expected == o2_rating_expected

    co2_rating_expected = 10
    co2_rating_actual = co2_filter(bits_array)
    # assert co2_rating_expected == co2_rating_actual

    print(co2_rating_actual * o2_rating_actual)
