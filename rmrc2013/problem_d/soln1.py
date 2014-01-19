import math
import sys

def parents(num):
  parents = []
  while num > 1:
    num = math.floor(num / 2)
    parents.append(num)
  return parents

def children(p, n):
  # Depth: starts at 0
  p_depth = math.floor(math.log2(p))
  start = p * 2**(n - p_depth)
  end   = (p + 1) * 2**(n - p_depth)
  return range(start, end)

def intersection_empty(a, b):
  return len(set(a).intersection(set(b))) == 0

def main():
  input_file = sys.stdin
  n, num_hacked = [int(t) for t in input_file.readline().strip().split()]
  hacked = [int(t) for t in input_file.readline().strip().split()]
  hacked = sorted(hacked)
  assert num_hacked == len(hacked)

  k = []

  for drive in range(2**n, 2**(n + 1)):
    if drive in hacked:
      continue

    par = parents(drive)
    if not intersection_empty(par, k):
      continue

    valid_key = drive
    for p in par:
      child_drives = children(p, n)
      if intersection_empty(child_drives, hacked):
        valid_key = p
        continue
      else:
        k.append(valid_key)
        break

  print(' '.join([str(a) for a in sorted(k)]))

main()
