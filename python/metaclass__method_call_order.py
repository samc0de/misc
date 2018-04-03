"""Clarifies method calling order.

When a new class in instantiated/a new object is created, there are a number of
magic methods called. Order of their calls can show some clever code tricks!
This code attempts to show insights of these calls.
"""
from __future__ import print_function


DEBUG_KEY = 'debug'


class MetaClass(type):
  """This is a metaclass to be used below.

  Magic method of interest in this context is __call__.
  """
  def __call__(self, *args, **kwargs):
    """This method gets called when a new object of this class is created."""
    print('Inside __call__ method of {0}'.format(self.__class__.__name__))
    print('Positional args are: %s.' % (args or None))
    print('Keyword args are: %s.' % (kwargs or None))
    if kwargs.get(DEBUG_KEY):
      set_trace()

    return super(MetaClass, self).__call__(self)


class MyClass(object):
  __metaclass__ = MetaClass

  def __new__(cls, *args, **kwargs):
    """Called at creation time of a new object."""
    print('Inside __new__ of {0}.'.format(cls.__name__))
    print('Positional args are: %s.' % (args or None))
    print('Keyword args are: %s.' % (kwargs or None))
    if kwargs.get(DEBUG_KEY):
      set_trace()

  def __init__(self, *args, **kwargs):
    """Called at object (values) instantiation time of an object."""
    print('Inside __self__ of {0}.'.format(self.__class__.__name__))
    print('Positional args are: %s.' % (args or None))
    print('Keyword args are: %s.' % (kwargs or None))
    if kwargs.get(DEBUG_KEY):
      set_trace()


if __name__ == '__main__':
  import argparse
  from pdb import set_trace
  parser = argparse.ArgumentParser(prog='Magic methods call order demo.')
  # TODO: Add more args which can be passed in further.
  parser.add_argument('--' + DEBUG_KEY, action='store_false')
  args = parser.parse_args()
  # if args.get(DEBUG_KEY):
  debug = getattr(args, DEBUG_KEY)
  my_object = MyClass(debug=debug)
