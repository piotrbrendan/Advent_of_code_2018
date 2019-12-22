from collections import defaultdict
from functools import reduce

INPUT_PATH = 'input_2'


def read_input():
    with open(INPUT_PATH, 'r') as f:
        inp = f.read()
    return inp.split('\n')


def cnt_check(id):

    #check cnt is a list of counts of pairs and trios
    check_cnt = [0,0]
    cnt_dct = defaultdict(int)
    for letter in id:
        cnt_dct[letter] += 1

    vals = set(cnt_dct.values())
    if 2 in vals:
        check_cnt[0] += 1
    if 3 in vals:
        check_cnt[1] += 1

    return check_cnt


def cnt_letters():
    inp = read_input()
    check_sum = []

    for i in inp:
        check_sum.append(cnt_check(i))

    #transpose pure python method:
    check_sum_tansposed = [[0 for _ in check_sum] for _ in check_sum[0]]
    for idx1, row in enumerate(check_sum):
        for idx2, j in enumerate(row):
            check_sum_tansposed[idx2][idx1] = check_sum[idx1][idx2]

    #reduce results (multiply)
    check_sum_mult = reduce(lambda x, y: x * y, [sum(item) for item in check_sum_tansposed])
    return check_sum_mult


def find_common_letters():
    inp = read_input()
    start_idx = 1
    for s in inp:
        s_set = set(s)
        for idx in range(start_idx, len(inp)):
            comp_set = s_set.symmetric_difference(set(inp[idx]))
            if len(comp_set) <= 1 and len(s) == len(inp[start_idx]):
                # detailed comparison for those sets with 1 or 0 different distinct characters:
                comp_char_lst = [s[sub_idx] == inp[idx][sub_idx] for sub_idx in range(len(s))]
                comp_detailed = len(s) - sum(comp_char_lst)
                if comp_detailed == 1:
                    return ''.join([char for idx, char in enumerate(s) if comp_char_lst[idx]])

        if start_idx < len(inp):
            start_idx += 1
        else:
            return -1


if __name__ == '__main__':
    print(cnt_letters())
    x = find_common_letters()
    print(x)