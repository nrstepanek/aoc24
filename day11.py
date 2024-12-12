
from collections import Counter
import helper


input_file = 'inputs/day11'

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

def blink(stones):
  i = 0
  while i < len(stones):
    if stones[i] == 0:
      stones[i] = 1
    elif len(str(stones[i])) % 2 == 0:
      to_split = str(stones[i])
      stones[i] = int(to_split[:int(len(to_split)/2)])
      stones.insert(i + 1, int(to_split[int(len(to_split)/2):]))
      i += 1
    else:
      stones[i] *= 2024
    i += 1

def part_1():
  line = helper.read_file_as_string(input_file)
  stones = [int(s) for s in line.split()]
  #print(stones)
  for i in range(25):
    print(i)
    blink(stones)
    #print(stones)
  print(len(stones))

def blink_ll(stone_ll):
  cur_stone = stone_ll
  while cur_stone:
    if cur_stone.value == 0:
      cur_stone.value = 1
    elif len(str(cur_stone.value)) % 2 == 0:
      to_split = str(cur_stone.value)
      cur_stone.value = int(to_split[:int(len(to_split)/2)])
      new_stone = Node(int(to_split[int(len(to_split)/2):]))
      new_stone.next = cur_stone.next
      cur_stone.next = new_stone
    else:
      cur_stone.value *= 2024
    cur_stone = cur_stone.next

def part_2():
  line = helper.read_file_as_string(input_file)
  stones = [int(s) for s in line.split()]
  stone_ll = Node(stones[0])
  cur_stone = stone_ll
  for stone in stones[1:]:
    cur_stone.next = Node(stone)
    cur_stone = cur_stone.next
  for i in range(25):
    print(i)
    blink_ll(stone_ll)

def blink_counter(stone_counter):
  new_counter = Counter()
  for stone in stone_counter:
    if stone == 0:
      new_counter[1] += stone_counter[stone]
    elif len(str(stone)) % 2 == 0:
      to_split = str(stone)
      new_counter[int(to_split[:int(len(to_split)/2)])] += stone_counter[stone]
      new_counter[int(to_split[int(len(to_split)/2):])] += stone_counter[stone]
    else:
      new_counter[stone * 2024] += stone_counter[stone]

  return new_counter

def part_2_2():
  line = helper.read_file_as_string(input_file)
  stones = [int(s) for s in line.split()]
  stone_counter = Counter()
  for stone in stones:
    stone_counter[stone] += 1
  print(stone_counter)
  for i in range(75):
    print(i)
    stone_counter = blink_counter(stone_counter)
    print(stone_counter)

  total_stones = 0
  for key, value in stone_counter.items():
    total_stones += value

  print(total_stones)

part_2_2()