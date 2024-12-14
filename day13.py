
import helper
import numpy as np

input_file = 'inputs/day13'

def parse_input():
  lines = helper.read_file_as_list_of_strings(input_file)
  i = 0
  machines = []
  while i < len(lines):
    words = lines[i].split()
    x_diff = int(words[2].split('+')[1][:-1])
    y_diff = int(words[3].split('+')[1])
    a_button = (x_diff, y_diff)

    words = lines[i+1].split()
    x_diff = int(words[2].split('+')[1][:-1])
    y_diff = int(words[3].split('+')[1])
    b_button = (x_diff, y_diff)

    words = lines[i+2].split()
    x_goal = int(words[1].split('=')[1][:-1])
    y_goal = int(words[2].split('=')[1])
    goal = (x_goal, y_goal)

    machines.append((a_button, b_button, goal))
    i += 4

  return machines

def calculate_min_tokens(a_button, b_button, goal):
  goal_tokens_map = {}
  for a_presses in range(1, 101):
    for b_presses in range(1, 101):
      if a_button[0] * a_presses + b_button[0] * b_presses == goal[0] and a_button[1] * a_presses + b_button[1] * b_presses == goal[1]:
        goal_tokens_map[a_presses*3 + b_presses] = (a_presses, b_presses)
  if len(goal_tokens_map) == 0:
    return 0
  return min(goal_tokens_map.keys())
                        

def part_1():
  machines = parse_input()
  min_tokens = 0
  for machine in machines:
    a_button, b_button, goal = machine
    tokens = calculate_min_tokens(a_button, b_button, goal)
    min_tokens += tokens

  print(min_tokens)

def gaussians_elimination(coefficients, constants):
  n = len(coefficients)
  for i in range(n):
    max_index = i
    for j in range(i+1, n):
      if abs(coefficients[j][i]) > abs(coefficients[max_index][i]):
        max_index = j
    coefficients[i], coefficients[max_index] = coefficients[max_index], coefficients[i]
    constants[i], constants[max_index] = constants[max_index], constants[i]

    for j in range(i+1, n):
      ratio = coefficients[j][i] / coefficients[i][i]
      for k in range(i, n):
        coefficients[j][k] -= ratio * coefficients[i][k]
      constants[j] -= ratio * constants[i]

  x = [0] * n
  for i in range(n-1, -1, -1):
    x[i] = constants[i] / coefficients[i][i]
    for j in range(i):
      constants[j] -= coefficients[j][i] * x[i]

  return x

def part_2():
  machines = parse_input()
  min_tokens = 0
  for machine in machines:
    a_button, b_button, goal = machine
    goal = (goal[0] + 10000000000000, goal[1] + 10000000000000)
    print(gaussians_elimination([[a_button[0], b_button[0]], [a_button[1], b_button[1]]], [goal[0], goal[1]]))
    a = np.array([[a_button[0], b_button[0]], [a_button[1], b_button[1]]])
    b = np.array([goal[0], goal[1]])
    x = np.linalg.solve(a, b)
    a_presses = float(x[0])
    b_presses = float(x[1])
    int_a_presses = int(a_presses)
    int_b_presses = int(b_presses)
    if int_a_presses * a_button[0] + int_b_presses * b_button[0] == goal[0] and int_a_presses * a_button[1] + int_b_presses * b_button[1] == goal[1]:
      print(int(a_presses), int(b_presses))
      min_tokens += int(a_presses)*3 + int(b_presses)
    else:
      print('No solution found')

  print(min_tokens)

part_2()