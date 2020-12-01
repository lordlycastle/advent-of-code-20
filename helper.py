import numpy as np

import runner


def load_mod(day):
    return __import__(runner.format_filename(day))


def str_to_array(data):
    return np.array([int(i) for i in data.split('\n')])


def sort(np_array):
    return np.sort(np_array)


def unique(np_array):
    return np.unique(np_array)


def sort_unique(np_array):
    return sort(unique(np_array))
