import random
import sys

def main():
  n, num_hacked = [int(t) for t in sys.argv[1:3]]
  r = range(2**n, 2**(n + 1))
  hacked = [str(random.choice(r)) for l in range(num_hacked)]
  print('%s %s' % (n, num_hacked))
  print(' '.join(hacked))

main()
