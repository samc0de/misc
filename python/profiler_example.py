#! /usr/bin/python2
# coding: utf-8
import argparse
import sys
from memory_profiler import profile


# TODO: Add timing profiling too.
SLOWNESS_THRESHOLD = 100000
POSITIVE = ['y', 'yes']


def square_adder(limit):
    total = sum(num * num for num in xrange(limit))
    return total


def square_adder_heavy(limit):
    total = sum([num * num for num in range(limit)])
    return total


memory_profiled_func = profile(square_adder)
memory_profiled_func_heavy = profile(square_adder_heavy)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-e', '--epoch', help='Number of iterations.',
                      default=SLOWNESS_THRESHOLD, type=int)
  # Or a boolean, time or not time (= memory)?
  parser.add_argument('-t', '--type', help='Type of profiling.',
                      default='time', choices=['time', 'memory'])

  args = parser.parse_args()
  msg = ('%(SLOWNESS_THRESHOLD)s or more iterations can cause a slowness and '
         'possibly render the system unresponsive. Are you sure about this?\n')
  confirmation = 'n'

  if args.epoch > SLOWNESS_THRESHOLD:
    confirmation = raw_input(msg %locals())
    if confirmation.lower() not in POSITIVE:
      sys.exit(0)

  if args.type != 'time':
    # Add timit here!
    func, func_heavy = memory_profiled_func, memory_profiled_func_heavy
    # func_heavy = memory_profiled_func_heavy
  else:
    func, func_heavy = square_adder, square_adder_heavy

  func(args.epoch)
  func_heavy(args.epoch)
