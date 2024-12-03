

import re
import helper


input_file = 'inputs/day3'

def part_1():
  line = helper.read_file_as_string(input_file)
  matches = re.findall(r'mul\(\d+,\d+\)', line)
  sum = 0
  for match in matches:
    match = match[4:len(match) - 1]
    nums = [int(x) for x in match.split(',')]
    sum += nums[0] * nums[1]
  print(sum)

def part_2():
  line = helper.read_file_as_string(input_file)
  matches = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)
  sum = 0
  enabled = True
  for match in matches:
    if match == 'do()':
      enabled = True
    elif match == 'don\'t()':
      enabled = False
    else:
      if enabled:
        match = match[4:len(match) - 1]
        nums = [int(x) for x in match.split(',')]
        sum += nums[0] * nums[1]

  print(sum)

part_1()
part_2()