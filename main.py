# Repl.it AOC Python Runner
import runner
import helper

d1 = helper.load_mod(1)
d2 = helper.load_mod(2)
d3 = helper.load_mod(3)

# Instructions:
# For each day, create a new python file and a puzzle input file consisting
#  of the day number and then the extension .py or .txt.
# So for day 20 you would create "20.py" and "20.txt"
# Don't forget to put a 0 before days 1-9 (so day 5 becomes "05.py") but not on
# any other days. This ensures the days are sorted properly in the files view.

# Each day in the python file, all you have to do is write a part1(prompt)
#  method and paste your puzzle input in the text file.
# You can also return a value and it will be printed out.
# The input will be read and passed to your code automatically.
# Add a part2() method when you're ready.
# Look at 01.py for an example

# Update the day in runner.run() each day to change which day is run.
# Your code will be automatically timed.

# For a menu where users can select a day, use this
# max_day is optional, remove it for no limit
# day = runner.get_day(max_day=5)

upto_day = 3
for i in range(1, upto_day+1):
    print('-'*20)
    runner.run(day=i)
    print('*'*20)