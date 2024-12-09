
import helper


input_file = 'inputs/day7'
operators = ['+', '*']

def find_operators(goal, nums, operators):
  if len(operators) < len(nums) - 1:
    return find_operators(goal, nums, operators + ['+']) or find_operators(goal, nums, operators + ['*'])
  else:
    total = nums[0]
    for i in range(1, len(nums)):
      if operators[i-1] == '+':
        total += nums[i]
      else:
        total *= nums[i]
    return total == goal

def part_1():
  lines = helper.read_file_as_list_of_strings(input_file)
  calibration_total = 0
  for line in lines:
    parts = line.split(':')
    goal = int(parts[0])
    nums = [int(n) for n in parts[1].split()]
    result = find_operators(goal, nums, [])
    if result:
      calibration_total += goal
  print(calibration_total)

def find_operators_2(goal, nums, operators):
  if len(operators) < len(nums) - 1:
    return find_operators_2(goal, nums, operators + ['+']) or find_operators_2(goal, nums, operators + ['*']) or find_operators_2(goal, nums, operators + ['||'])
  else:
    total = nums[0]
    for i in range(1, len(nums)):
      if operators[i-1] == '+':
        total += nums[i]
      elif operators[i-1] == '*':
        total *= nums[i]
      else:
        total = int(str(total) + str(nums[i]))
    return total == goal

def part_2():
  lines = helper.read_file_as_list_of_strings(input_file)
  calibration_total = 0
  for line in lines:
    parts = line.split(':')
    goal = int(parts[0])
    nums = [int(n) for n in parts[1].split()]
    result = find_operators_2(goal, nums, [])
    if result:
      calibration_total += goal
  print(calibration_total)

part_1()
part_2()