"""Various ways of generating prime numbers."""

import argparse
from pdb import set_trace


LIMIT = 1e15


def gen_primes(limit=LIMIT, primes=None):
  """Generate primes.

  Args:
    index: Index of prime number to generate, 1st one being 2.

    primes: List of already known primes, also used as divisors.

  Returns:
    A generator that yields prime numbers.
  """
  current_num = 2
  while current_num < limit:
    if primes == None:
      primes = []  # Ordered container needed.

    # set_trace()
    for divisor in primes:
      if current_num % divisor == 0:
        break
    else:
      yield current_num
      primes.append(current_num)  # Keeping after yield for priorities n fun.

    current_num += 2

  print 'Upper limit reached!'  # Use logging here.
  return  # Or stop iteration?


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  limit = parser.add_argument('--limit', type=int, default=100)
  args = parser.parse_args()
  for prime in gen_primes(args.limit):
    print prime
