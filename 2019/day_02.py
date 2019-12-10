from enum import IntEnum


class OpCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99


def process(array, noun, verb):
    array[1] = noun
    array[2] = verb
    curr_pos = 0
    while True:
        op_code = array[curr_pos]
        if op_code == OpCode.HALT:
            break
        in1, in2, out = array[curr_pos + 1 : curr_pos + 4]
        if op_code == OpCode.ADD:
            result = array[in1] + array[in2]
        if op_code == OpCode.MULTIPLY:
            result = array[in1] * array[in2]
        array[out] = result
        curr_pos += 4
    return array[0]


def solve1(input):
    array = list(map(int, input.split(",")))
    return process(array, noun=12, verb=2)


def solve2(input):
    array = list(map(int, input.split(",")))
    for noun in range(0, 100):
        for verb in range(0, 100):
            output = process(array[:], noun, verb)
            if output == 19690720:
                return 100 * noun + verb


input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,1,9,27,31,1,31,10,35,2,13,35,39,1,39,10,43,1,43,9,47,1,47,13,51,1,51,13,55,2,55,6,59,1,59,5,63,2,10,63,67,1,67,9,71,1,71,13,75,1,6,75,79,1,10,79,83,2,9,83,87,1,87,5,91,2,91,9,95,1,6,95,99,1,99,5,103,2,103,10,107,1,107,6,111,2,9,111,115,2,9,115,119,2,13,119,123,1,123,9,127,1,5,127,131,1,131,2,135,1,135,6,0,99,2,0,14,0"

if __name__ == "__main__":
    print(solve2(input))
