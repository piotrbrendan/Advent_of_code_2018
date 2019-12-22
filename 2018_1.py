def repl_mapped(s, map_dct):

    for k, i in map_dct.items():
        s = s.replace(k, i)
    return s

def get_twice(input_lst):
    current_freq = 0
    seen_freq = {current_freq}

    while True:
        for item in input_lst:
            current_freq += item
            if current_freq in seen_freq and len(seen_freq) > 1:
                return current_freq
            seen_freq.add(current_freq)


if __name__ =='__main__':
    with open('input_1', 'r') as f:
        inpt = f.readlines()

    input_lst = [int(repl_mapped(i, {'+': '', '\n': ''})) for i in inpt]
    answ_1a = sum(input_lst)
    answ_1b = get_twice(input_lst)
    print(answ_1a, answ_1b)

