from collections import defaultdict


SIZE = 1000
FABIRC_ARR = [[0 for _ in range(SIZE)] for _ in range(SIZE)]


def read_input():
    with open('input_3','r') as f:
        inp = f.read()
        inp_lst = inp.split('\n')
    return list(filter(None, inp_lst))


def get_id_coords_and_size(s,
                        coords_sep='@',
                        coords_split=',',
                        size_sep=':',
                        size_split='x'):

    coords_sep_idx = s.find(coords_sep)
    size_sep_idx = s.find(size_sep)

    id_s = s[1:coords_sep_idx-1].split(size_split)
    id_val = int(id_s[0])

    coords_s =  s[coords_sep_idx + 1:size_sep_idx].split(coords_split)
    coords_vals = [int(s) for s in coords_s]

    size_s = s[size_sep_idx + 1:].split(size_split)
    size_vals = [int(s) for s in size_s]

    return {'id': id_val,
            'coords': coords_vals,
            'size': size_vals}


def place_on_fabric(id, coords, size):

    x_shift, y_shift = coords
    x_size, y_size = size

    for i in range(y_size):
        for j in range(x_size):
            if FABIRC_ARR[y_shift+i][x_shift+j] == 0:
                FABIRC_ARR[y_shift+i][x_shift+j] = id
            else:
                FABIRC_ARR[y_shift + i][x_shift + j] = 'x'

def main():
    inp = read_input()
    for s in inp:
        id_coords_size_dct = get_id_coords_and_size(s)
        place_on_fabric(**id_coords_size_dct)

    cnt_dct = defaultdict(int)
    for i in range(SIZE):
        for j in range(SIZE):
            cnt_dct[FABIRC_ARR[i][j]] += 1

    non_overlapping = -1
    for s in inp:
        id_coords_size_dct = get_id_coords_and_size(s)
        id = id_coords_size_dct['id']
        area = id_coords_size_dct['size'][0] * id_coords_size_dct['size'][1]
        cnt = cnt_dct[id]
        if cnt == area:
            non_overlapping = id

    return non_overlapping, cnt_dct['x']


if __name__ == '__main__':
    print(main())
    with open('test_out.txt', 'w') as f:
        f.write(str(FABIRC_ARR))
