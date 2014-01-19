import cProfile
import math
import sys

def is_leaf(d, n):
  return math.floor(math.log2(d)) == n

def leaves(d, n):
  # d_depth: starts at 0
  d_depth = math.floor(math.log2(d))
  start = d       * 2**(n - d_depth)
  end   = (d + 1) * 2**(n - d_depth)
  return (start, end)

def are_leaves_unhacked(d, n, hacked):
  l_start, l_end = leaves(d, n)

  if hacked[-1] < l_start or hacked[0] >= l_end:
    return True

  for h in hacked:
    if h >= l_start and h < l_end:
      return False
  return True

def unhacked(d, n, hacked_list):
  if is_leaf(d, n):
    if d in hacked_list:
      return []
    else:
      return [d]

  l, r = 2*d, 2*d + 1
  l_unhacked = are_leaves_unhacked(l, n, hacked_list)
  r_unhacked = are_leaves_unhacked(r, n, hacked_list)

  if l_unhacked and r_unhacked:
    return [d]
  elif l_unhacked:
    return [l] + unhacked(r, n, hacked_list)
  elif r_unhacked:
    return unhacked(l, n, hacked_list) + [r]
  else:
    return unhacked(l, n, hacked_list) + unhacked(r, n, hacked_list)
 
def main():
  input_file = sys.stdin
  n, num_hacked = [int(t) for t in input_file.readline().strip().split()]
  hacked = [int(t) for t in input_file.readline().strip().split()]
  hacked = sorted(hacked)
  assert num_hacked == len(hacked)

  good = unhacked(1, n, hacked)
  print(' '.join([str(g) for g in sorted(good)]))

if '-d' in sys.argv:
  cProfile.run('main()')
else:
  main()
