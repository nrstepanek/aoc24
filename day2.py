

import helper


input_file = 'inputs/day2'

def part_1():
  lines = helper.read_file_as_list_of_strings(input_file)
  safe_count = 0
  for line in lines:
    safe = True
    nums = [int(x) for x in line.split()]

    if len(nums) < 2:
      safe_count += 1
      continue
    if len(nums) == 2:
      if abs(nums[0] - nums[1]) <= 3 and nums[0] != nums[1]:
        safe_count += 1
      continue

    increasing = nums[0] < nums[1]

    i = 0
    while i < len(nums) - 1:
      if abs(nums[i] - nums[i + 1]) > 3 or nums[i] == nums[i + 1] or ((nums[i + 1] > nums[i]) != increasing):
        safe = False
        break
      i += 1

    if safe:
      safe_count += 1

  print(safe_count)

def part_2():
  lines = helper.read_file_as_list_of_strings(input_file)
  safe_count = 0
  for line in lines:
    nums = [int(x) for x in line.split()]
    nums_to_check = [nums[0:i] + nums[i+1:len(nums)] for i in range(0, len(nums))]

    for n in nums_to_check:
      safe = True
      increasing = n[0] < n[1]

      i = 0
      while i < len(n) - 1:
        if abs(n[i] - n[i + 1]) > 3 or n[i] == n[i + 1] or ((n[i + 1] > n[i]) != increasing):
          safe = False
          break
        i += 1

      if safe:
        safe_count += 1
        break

  print(safe_count)

part_1()
part_2()