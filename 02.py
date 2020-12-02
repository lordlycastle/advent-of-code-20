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

    self.count = self.psswd.count(self.char)
    if self.count >= self.min_count and self.count <= self.max_count:
        self.valid = True
    else:
        self.valid = False

  def __str__(self):
    return f'/ {str(self.valid):5} / {self.count:2} => Count: {self.min_count:2} - {self.max_count:2} of {self.char} in self{self.psswd}'


argv = [InputCodec(x) for x in helper.str_to_array(raw)]


def part1(data):
  return len([x for x in argv if x.valid])