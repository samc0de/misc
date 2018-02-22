"""Various ways of generating prime numbers."""

import argparse


LIMIT = 1e15


def gen_primes(start=3, limit=LIMIT, primes=None):
  """Generate primes.

  Args:
    start: Starting number, default is 2.

    limit: Upper limit to find primes upto. Negative for infinite!

    primes: List of already known primes, also used as divisors.

  Returns:
    A generator that yields prime numbers.
  """
  yield 2
  current_num = 3
  while current_num < limit or limit < 0:
    if primes == None:
      primes = [2]  # Ordered container needed.

    for divisor in primes:
      if current_num % divisor == 0:
        break
    else:
      yield current_num
      primes.append(current_num)  # Keeping after yield for priorities n fun.

    # Special case handeling for efficiency. Enables increments by 2.
    current_num += 2

  print 'Upper limit reached!'  # Use logging here.
  return  # Or stop iteration?


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  limit = parser.add_argument('--limit', type=int, default=100)
  args = parser.parse_args()
  for prime in gen_primes(args.limit):
    print prime
