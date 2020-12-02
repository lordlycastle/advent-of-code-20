import runner
import re
import helper

raw = runner.get_data(2)

class InputCodec:
  def __init__(self, codec):
    self.codec = codec
    matches = re.match(r'([0-9]+)-([0-9]+) ([\w]{1}): ([\w]+)', codec)
    self.min_count = int(matches.group(1))
    self.max_count = int(matches.group(2))
    self.char = matches.group(3)
    self.psswd = matches.group(4)

    self.char_count = self.psswd.count(self.char)
    self.p1_valid = False
    self.p2_valid = False
    
  def __str__(self):
    return f'/ {str(self.valid):5} / {self.char_count:2} => Count: {self.min_count:2} - {self.max_count:2} of {self.char} in self{self.psswd}'


argv = [InputCodec(x) for x in helper.str_to_array(raw)]


def part1(data):
    for i in argv:
        if i.char_count >= i.min_count and i.char_count <= i.max_count:
            i.p1_valid = True
        else:
            i.p1_valid = False

    return len([x for x in argv if x.p1_valid])


def part2(data):
    for i in argv:
        if (i.psswd[i.min_count-1] == i.char) != (i.psswd[i.max_count-1] == i.char):
            i.p2_valid = True
        else:
            i.p2_valid = False
    return len(list(filter(lambda x: x.p2_valid, argv)))