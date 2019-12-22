INPUT_PATH = 'input_5'


def read_input():
    with open(INPUT_PATH,'r') as f:
        return f.read().strip('\n')


def transform(inp):
    result = []
    for idx, char in enumerate(inp):
        if not result:
            result.append(char)
        elif all([char != result[-1], char.capitalize() == result[-1].capitalize()]):
            result.pop()
        else:
            result.append(char)
    return len(result), ''.join(result)


def find_shortest(inp):
    results = {}
    letters = set(inp.lower())
    for i in letters:
        inp_replaced = inp
        inp_replaced = inp_replaced.replace(i, '')
        inp_replaced = inp_replaced.replace(i.upper(), '')
        cnt, _ = transform(inp_replaced)
        results[i] = cnt

    return min(results, key=results.get), min(results.values())


if __name__ == '__main__':
    inp = read_input()
    result_len, result_s = transform(inp)
    shortest = find_shortest(inp)
    print(result_len, shortest)
