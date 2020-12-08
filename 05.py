import runner
import re
import helper
import numpy as np
import math

raw = runner.get_data(5)


class SeatCode:
    def __init__(self, encoded):
        self.raw = encoded
        if len(self.raw) != 10:
            print(f'Expected to have 10 characters. Expectation were disappointed: {encoded}')
            return
        self.code_row = encoded[:7]
        self.code_col = encoded[-3:]
        self.row = None
        self.col = None

    @property
    def coord(self):
        return self.row, self.col

    def __str__(self): return f'{self.coord} => {self.code_row} + {self.code_col}'

    def __repr__(self): return str(self)


argv = [SeatCode(x) for x in helper.str_to_array(raw)]
seats = np.zeros((128, 8))


def decode(lower_char: str, upper_char: str, lower_idx: int, upper_idx: int, code: str, debug: bool = True) -> int:
    if code.replace(upper_char, '').replace(lower_char, '') != '':
        raise ValueError(
            f'Unexpected char: {code.replace(upper_char, "").replace(lower_char, "")} in code: {code}. '
            f'Expected only `{upper_char}` or `{lower_char}`.')
    # elif (upper_idx - lower_idx) % 2 != 0:
    #     raise ValueError(f'Expected even number length. U:{upper_idx} L:{lower_idx}')

    if code == '':
        if upper_idx != lower_idx:
            raise ValueError(f'Odd number. Cannot split. U:{upper_idx} L:{lower_idx}')
        else:
            return upper_idx

    char = code[0]
    diff = upper_idx - lower_idx +1
    if char == upper_char:
        d = lower_idx
        lower_idx = math.floor(upper_idx - diff / 2)
        if debug: print(f'🔻 {char}: ({lower_idx}, {upper_idx}) => L: {d} => {lower_idx}')
    else:
        d = upper_idx
        upper_idx = math.ceil(lower_idx + diff / 2)
        if debug: print(f'🔺 {char}: ({lower_idx}, {upper_idx}) => L: {d} => {upper_idx}')

    return decode(lower_char, upper_char, lower_idx, upper_idx, code[1:], debug)


def part1(data):
    print(argv)
    # return argv
