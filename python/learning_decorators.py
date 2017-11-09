"""Experimenting with decorators."""

import datetime
import inspect
from pdb import set_trace
# import timeit


def time_it(func):
  def new_func(*args, **kwargs):
    before = datetime.datetime.now()
    result = func(*args, **kwargs)
    after = datetime.datetime.now()
    print 'Time taken for {0}: {1}'.format(func.func_name, after - before)
    print 'Arguments: {0}'.format(args)
    print 'Keyword arguments: {0}'.format(kwargs)
    return result
  return new_func


def class_timer(cls):
  """Decorator for timing class methods."""

  class NewClass(object):  # Subclass cls?
    def __init__(self, *args, **kwargs):
      self.original_obj = cls(*args, **kwargs)
      self.original_cls = cls

    def __getattribute__(self, attr):
      # Not to mess up lookups for this class.
      # Sure this won't trigger recursion?
      # if hasattr(super(NewClass, self).__getattribute__(attr)
      # if hasattr(super(NewClass, self), attr):
      #   return super(NewClass, self).__getattribute__(attr)
      try:
        target = super(NewClass, self).__getattribute__(attr)
      except AttributeError:
        pass
      else:
        return target

      # target = self.original_obj.__getattribute__(attr)
      target = getattr(self.original_obj, attr)

      if inspect.ismethod(target):
        return time_it(target)
      return target

  return NewClass


if __name__ == '__main__':
  set_trace()
