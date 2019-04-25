import sys

INPUT_ARRAY = [10, 15, 3, 7]
K = 17

for idx in range(len(INPUT_ARRAY)):
    cur_pos = 0
    for pos in range(len(INPUT_ARRAY)):
        if pos == cur_pos:
            continue

        if INPUT_ARRAY[cur_pos] + INPUT_ARRAY[pos] == K:
            print("True!")
            sys.exit(0)

print("False")
