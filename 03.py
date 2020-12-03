import runner
import helper
import numpy as np

raw = runner.get_data(3)
argv = helper.str_to_array(raw)
maze = np.array([list(x) for x in argv])


def part1(data):
    print(f'{maze.shape}')
    slope = [3, 1]
    print(f'Check passed: {check_can_end(maze.shape, slope)}')

    return find_num_of_trees(slope)


def part2(data):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]
    counts = [find_num_of_trees(x) for x in slopes]
    result = 1
    for i in counts:
        result = result * i
    return result, counts


def check_can_end(maze_size, slope):
    return (maze_size[0] % slope[1]) == 0


def get_start_point(maze):
    idx = [0, 0]
    current_char = maze[idx[0], idx[1]]
    # print(current_char)
    while current_char != '.':
        idx[0] = idx[0] + 1
        current_char = maze[idx]
    print(f'Starting point: {idx}')
    return idx


def find_num_of_trees(slope):
    start_coord = get_start_point(maze)
    chars = []
    current_coord = start_coord
    print(f'Check passed: {check_can_end(maze.shape, slope)}')
    while current_coord[1] != maze.shape[0]:
        chars.append(maze[current_coord[1], current_coord[0]])
        current_coord[0] = (current_coord[0] + slope[0]) % maze.shape[1]
        current_coord[1] = (current_coord[1] + slope[1])
        # This condition is in the wrong place for when slope.y == 1.
        # There's an over-the-fence error. 🙄
        if current_coord[1] > maze.shape[0]:
            diff = maze.shape[0] - current_coord[1]
            print(f'Over stepped: shifting back by: {diff}')
            return len([x for x in chars if x == '#'])
    return len([x for x in chars if x == '#'])
