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
  def __call__(self, *arguments, **kwargs):
    """This method gets called when a new object of this class is created."""
    print('Inside __call__ method of {0}'.format(self.__class__.__name__))
    print('Positional arguments are: %s.' % (arguments or None))
    print('Keyword arguments are: %s.' % (kwargs or None))
    # See if popping/modifying kwargs here affects other class's methods!
    # IT DOES! Do not pop/modify kwargs or even arguments.
    # if kwargs.pop(DEBUG_KEY):
    if kwargs.get(DEBUG_KEY):
      set_trace()
      # kwargs.pop(DEBUG_KEY)

    return super(MetaClass, self).__call__(*arguments, **kwargs)


class MyClass(object):
  __metaclass__ = MetaClass

  def __new__(cls, *arguments, **kwargs):
    """Called at creation time of a new object."""
    print('Inside __new__ of {0}.'.format(cls.__name__))
    print('Positional arguments are: %s.' % (arguments or None))
    print('Keyword arguments are: %s.' % (kwargs or None))
    if kwargs.get(DEBUG_KEY):
      set_trace()

    # Notice a different syntax for the super call? __new__ is a static method,
    # so there is no binding to 'cls' in the __new__ returned by super(). It
    # needs to be passed explicitly.
    # https://stackoverflow.com/a/7471469/860421
    return super(MyClass, cls).__new__(cls, *arguments, **kwargs)

  def __init__(self, *arguments, **kwargs):
    """Called at object (values) instantiation time of an object."""
    print('Inside __init__ of {0}.'.format(self.__class__.__name__))
    print('Positional arguments are: %s.' % (arguments or None))
    print('Keyword arguments are: %s.' % (kwargs or None))
    if kwargs.get(DEBUG_KEY):
      set_trace()

    return super(MyClass, self).__init__(*arguments, **kwargs)


if __name__ == '__main__':
  import argparse
  from pdb import set_trace
  parser = argparse.ArgumentParser(prog='Magic methods call order demo.')
  # TODO: Add more args which can be passed in further.
  # Value store_true holds true when option is included. Opposite behaviour
  # with store_false.
  parser.add_argument('--' + DEBUG_KEY, action='store_true')
  args = parser.parse_args()
  # if args.get(DEBUG_KEY):
  debug = getattr(args, DEBUG_KEY)
  if debug:
    set_trace()
  my_object = MyClass(debug=debug)
