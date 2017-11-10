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
    original_name = __name__
    __name__ = original_cls_name = cls.__name__

    def __init__(self, *args, **kwargs):
      self.original_obj = cls(*args, **kwargs)
      self.original_cls = cls
      print 'Inside __init__.'

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



# Code highlighting problem:
@class_timer
class Math(object):
  def add(self, first, second):
    return first + second


# Subclass for subtraction.
@class_timer
class MathSubSub(Math):
  def __init__(self, *args, **kwargs):
    print 'Inside MathAnother.__init__.'
    self._args = args
    self._kwargs = kwargs
    super(MathAnother, self).__init__(*args, **kwargs)
  def sub(self, first, second):
    return first - second


# Martelli approach.
def class_timer_another(cls):
  """Decorator for timing class methods."""

  class NewClass(object):  # Subclass cls?
    _original_cls = cls

    def __init__(self, *args, **kwargs):
      self.original_obj = cls(*args, **kwargs)
      print 'Inside __init__.'

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


@class_timer_another
class MathAnother(object):
  def __init__(self):
    if '_original_cls' in self.__class__.__dict__:
      self.__class__ = self.__class__._original_cls

  def add(self, first, second):
    return first + second


# Subclass for subtraction.
@class_timer_another
class MathAnotherSubSub(Math):
  def __init__(self, *args, **kwargs):
    set_trace()
    print 'Inside MathAnother.__init__.'
    self._args = args
    self._kwargs = kwargs
    super(MathAnother, self).__init__(*args, **kwargs)
  def sub(self, first, second):
    return first - second




if __name__ == '__main__':
  set_trace()
