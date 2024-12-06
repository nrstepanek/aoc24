

from collections import defaultdict
import helper


input_file = 'inputs/day5'

def read_input():
  lines = helper.read_file_as_list_of_strings(input_file)
  rules = []
  updates = []
  reading_updates = False
  for line in lines:
    if line == '':
      reading_updates = True
      continue
    if reading_updates:
      updates.append(line)
    else:
      rules.append(line)
  return rules, updates


def part_1():
  rules, updates = read_input()

  behind_rule_map = defaultdict(list)
  for rule in rules:
    parts = rule.split('|')
    behind_rule_map[int(parts[0])].append(int(parts[1]))
  
  middle_correct_pages = []
  invalid_updates = []
  for update in updates:
    page_nums = [int(pn) for pn in update.split(',')]
    correct = True
    seen_pages = []
    for page_num in page_nums:
      # Check if the current page needs to have been before any page we've already seen
      for cannot_have_seen in behind_rule_map[page_num]:
        if cannot_have_seen in seen_pages:
          correct = False
          break
      seen_pages.append(page_num)
    if correct:
      middle_correct_pages.append(page_nums[len(page_nums) // 2])
    else:
      invalid_updates.append(update)
      print('Invalid update:', update)

  print(middle_correct_pages)
  print(sum(middle_correct_pages))
  return behind_rule_map, invalid_updates

def part_2(behind_rule_map, invalid_updates):

  middle_nums = []
  for update in invalid_updates:
    print(update)
    seen_page_index_map = {}
    page_nums = [int(pn) for pn in update.split(',')]
    i = 0
    while i < len(page_nums):
      page_num = page_nums[i]
      nums_to_be_behind = behind_rule_map[page_num]
      for num_to_be_behind in nums_to_be_behind:
        if num_to_be_behind in seen_page_index_map:
          print('Swapping', page_num, 'and', num_to_be_behind)
          page_nums[i], page_nums[seen_page_index_map[num_to_be_behind]] = page_nums[seen_page_index_map[num_to_be_behind]], page_nums[i]
          i = -1
          seen_page_index_map = {}
          break
      if i != -1:
        seen_page_index_map[page_num] = i
      i += 1

    print(page_nums)
    middle_nums.append(page_nums[len(page_nums) // 2])
  print(sum(middle_nums))
    
    

behind_rule_map, invalid_updates = part_1()
print(behind_rule_map)
part_2(behind_rule_map, invalid_updates)