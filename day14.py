
import helper


input_file = 'inputs/day14'

def parse_input():
  lines = helper.read_file_as_list_of_strings(input_file)
  guards = []
  for line in lines:
    parts = line.split(' ')
    start_coords = parts[0][2:].split(',')
    start_coords = (int(start_coords[0]), int(start_coords[1]))
    velocity = parts[1][2:].split(',')
    velocity = (int(velocity[0]), int(velocity[1]))
    guards.append((start_coords, velocity))

  return [g[0] for g in guards], [g[1] for g in guards]

def score_quadrants(end_guard_locs, grid_width, grid_height):
  scores = [0, 0, 0, 0]
  for loc in end_guard_locs:
    if loc[0] < int(grid_width / 2) and loc[1] < int(grid_height / 2):
      scores[0] += 1
    elif loc[0] > int(grid_width / 2) and loc[1] < int(grid_height / 2):
      scores[1] += 1
    elif loc[0] < int(grid_width / 2) and loc[1] > int(grid_height / 2):
      scores[2] += 1
    elif loc[0] > int(grid_width / 2) and loc[1] > int(grid_height / 2):
      scores[3] += 1

  return scores

def safety_factor(scores):
  return scores[0] * scores[1] * scores[2] * scores[3]



def part_1():
  guards = parse_input()
  grid_width = 11
  grid_height = 7
  seconds = 100
  end_guard_locs = []
  for guard in guards:
    start_coords, velocity = guard
    x = start_coords[0] + velocity[0] * seconds
    y = start_coords[1] + velocity[1] * seconds
    x = x % grid_width
    y = y % grid_height
    end_guard_locs.append((x, y))

  scores = score_quadrants(end_guard_locs, grid_width, grid_height)
  print(scores)
  print(scores[0] * scores[1] * scores[2] * scores[3])

def part_2():
  guard_locs, velocities = parse_input()
  grid_width = 101
  grid_height = 103
  print(guard_locs)
  min_safety_factor = 99999999999
  min_safety_factor_seconds = 0
  for seconds in range(1, 10000):
    for i in range(len(guard_locs)):
      guard_locs[i] = ((guard_locs[i][0] + velocities[i][0]) % grid_width, (guard_locs[i][1] + velocities[i][1]) % grid_height)

    scores = score_quadrants(guard_locs, grid_width, grid_height)
    safety_factor_val = safety_factor(scores)
    print('safety factor after seconds %d: %d' % (seconds, safety_factor_val))
    if safety_factor_val < min_safety_factor:
      min_safety_factor = safety_factor_val
      min_safety_factor_seconds = seconds

  print(min_safety_factor_seconds)
  print(min_safety_factor)


part_2()
