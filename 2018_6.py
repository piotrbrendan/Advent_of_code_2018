import numpy as np

INPUT_PATH = 'input_6'


def read_input():
    with open(INPUT_PATH) as f:
         inp = [line.strip('\n') for line in f.readlines()]
         inp = [[int(s) for s in coords_s.split(', ')]
                        for coords_s in inp]

    return np.array(inp)


def calc_manhattan_dits(p1, p2):
    """ Calcs manhattan distances between all points from p1 and p2
    p1 and p2 must have 2 dimentions. Returns np.array of values of
    shape nxm, where
     n represents each point from p1 and
     m represents each point from p2."""

    return np.sum(np.abs(p1 - p2[:,np.newaxis]), axis=2).T


def filter_ties(board):
    min_distances = np.min(board, axis=1)
    tie_locations = (board.T == min_distances).sum(axis=0) > 1
    return board[~tie_locations]


def get_board_distances(inp_arr):
    board_shape = np.max(inp_arr)
    board_arr = np.array([(x, y) for x in range(board_shape + 1) for y in range(board_shape + 1)])
    board_enlarged_arr = np.array([(x, y) for x in range(-1, board_shape + 2) for y in range(-1, board_shape + 2)])

    board_distances = calc_manhattan_dits(board_arr, inp_arr)
    board_enlarged_distances = calc_manhattan_dits(board_enlarged_arr, inp_arr)

    return board_distances, board_enlarged_distances


def find_biggest_area(board_distances, board_enlarged_distances):
    board_distances_fltr = filter_ties(board_distances)
    board_enlarged_distances_fltr = filter_ties(board_enlarged_distances)

    nearest_points = np.argmin(board_distances_fltr, axis=1)
    nearest_enlarged_points = np.argmin(board_enlarged_distances_fltr, axis=1)

    nearest_enlarged_points_cnt = np.bincount(nearest_enlarged_points.ravel())
    nearest_points_cnt = np.bincount(nearest_points.ravel())
    constant_size_cndt = nearest_enlarged_points_cnt == nearest_points_cnt

    return sorted(nearest_points_cnt[constant_size_cndt])[-1]


def part_2(board_distances):
    return np.sum(np.sum(board_distances, axis=1) < 10000)


if __name__ == '__main__':
    inp_arr = read_input()
    board_distances, board_enlarged_distances = get_board_distances(inp_arr)
    print(find_biggest_area(board_distances, board_enlarged_distances))
    print(part_2(board_distances))






