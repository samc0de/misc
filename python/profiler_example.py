#! /usr/bin/python2
# coding: utf-8
import argparse
import sys
from memory_profiler import profile


# TODO: Add timing profiling too.
SLOWNESS_THRESHOLD = 100000
POSITIVE = ['y', 'yes']


@profile
def square_adder(limit):
    total = sum(num * num for num in xrange(limit))
    return total


@profile
def square_adder_heavy(limit):
    total = sum([num * num for num in range(limit)])
    return total


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-e', '--epoch', help='Number of iterations.',
                      default=SLOWNESS_THRESHOLD, type=int)
  args = parser.parse_args()
  msg = ('%(SLOWNESS_THRESHOLD)s or more iterations can cause a slowness and '
         'possibly render the system unresponsive. Are you sure about this?\n')
  confirmation = 'n'

  if args.epoch > SLOWNESS_THRESHOLD:
    confirmation = raw_input(msg %locals())
    if confirmation.lower() not in POSITIVE:
      sys.exit(0)

  square_adder(args.epoch)
  square_adder_heavy(args.epoch)
