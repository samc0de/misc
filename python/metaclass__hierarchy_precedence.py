"""Attempts to show and clarify hierarchy and precedence in metaclass finding.

Docs/resources say that:
when a class def is found, python reads it, reads all attributes, and looks for
__metaclass__. If not found, any module level __metaclass__ attribute is
searched for. Also __metaclass__ attr is searched in super classes as well. If
not found, 'type' is used otherwise.

There is some disagreement about this (esp. Eli Bendersky's website which
doesn't mention about module level attribute in this hierarchy).

This should clarify that confusion. Especially when super classes with
__metaclass__ are involved.
"""
# Add debugging mode if required.
# Create inherited metaclasses too, for fun!

# from abc import ABCMeta
from __future__ import print_function


class MetaClass(type):
  def __new__(cls, *args, **kwargs):
    # Not sure what does this mean here.
    # Try removing the cls from the super() args.
    print('Inside __new__ of {0}.'.format(cls.__name__))
    print('(Actually in MetaClass)')
    return super(MetaClass, cls).__new__(cls, *args, **kwargs)

  def __init__(self, *args, **kwargs):
    # Does MetaClasses have __init__s?
    print('Inside __init__ of {0}.'.format(self.__class__.__name__))
    print('(Actually in MetaClass)')
    return super(MetaClass, self).__init__(*args, **kwargs)

  def __call__(self, *args, **kwargs):
    print('Inside __call__ of {0}.'.format(self.__class__.__name__))
    print('(Actually in MetaClass)')
    return super(MetaClass, self).__call__(*args, **kwargs)


class Class1Level1(object):
  """A class at level 1 with __metaclass__ defined inside."""
  __metaclass__ = MetaClass
  # set_in = Class1Level1
  Class1Level1 = True

  def __new__(cls, *args, **kwargs):
    # Try removing the cls from the super() args.
    print('Inside __new__ of {0}.'.format(cls.__name__))
    print('(Actually in Class1Level1)')
    return super(Class1Level1, cls).__new__(cls, *args, **kwargs)

  def __init__(self, *arguments, **kwargs):
    print('Inside __init__ of {0}.'.format(self.__class__.__name__))
    print('(Actually in Class1Level1)')
    self.arguments = arguments
    self.kwargs = kwargs
    self.set_in = self.__class__.__name__
    return super(Class1Level1, self).__init__(*arguments, **kwargs)


class Class2Level1(object):
  """A class at level 1 without a __metaclass__ defined."""
  Class2Level1 = True

  def __new__(cls, *args, **kwargs):
    # Try removing the cls from the super() args.
    print('Inside __new__ of {0}.'.format(cls.__name__))
    print('(Actually in Class2Level1)')
    return super(Class2Level1, cls).__new__(cls, *args, **kwargs)

  def __init__(self, *arguments, **kwargs):
    print('Inside __init__ of {0}.'.format(self.__class__.__name__))
    print('(Actually in Class2Level1)')
    self.arguments = arguments
    self.kwargs = kwargs
    self.set_in = self.__class__.__name__
    return super(Class2Level1, self).__init__(*arguments, **kwargs)


class Class1Level2(Class1Level1):
  """A level 2 class without a meta but with a parent having meta."""
  Class1Level2 = True

  def __new__(cls, *args, **kwargs):
    # Try removing the cls from the super() args.
    print('Inside __new__ of {0}.'.format(cls.__name__))
    print('(Actually in Class1Level2)')
    return super(Class1Level2, cls).__new__(cls, *args, **kwargs)

  def __init__(self, *arguments, **kwargs):
    print('Inside __init__ of {0}.'.format(self.__class__.__name__))
    print('(Actually in Class1Level2)')
    self.arguments = arguments
    self.kwargs = kwargs
    self.set_in = self.__class__.__name__
    return super(Class1Level2, self).__init__(*arguments, **kwargs)


class Class2Level2(Class2Level1):
  """A level 2 class with meta class defined neither in it nor in a parent."""
  Class2Level2 = True

  def __new__(cls, *args, **kwargs):
    # Try removing the cls from the super() args.
    print('Inside __new__ of {0}.'.format(cls.__name__))
    print('(Actually in Class2Level2)')
    return super(Class2Level2, cls).__new__(cls, *args, **kwargs)

  def __init__(self, *arguments, **kwargs):
    print('Inside __init__ of {0}.'.format(self.__class__.__name__))
    print('(Actually in Class2Level2)')
    self.arguments = arguments
    self.kwargs = kwargs
    self.set_in = self.__class__.__name__
    return super(Class2Level2, self).__init__(*arguments, **kwargs)


class Class3Level2(Class1Level1, Class2Level1):
  """A level 2 class with a meta class defined in first of its parents."""
  Class3Level2 = True

  def __new__(cls, *args, **kwargs):
    # Try removing the cls from the super() args.
    print('Inside __new__ of {0}.'.format(cls.__name__))
    print('(Actually in Class3Level2)')
    return super(Class3Level2, cls).__new__(cls, *args, **kwargs)

  def __init__(self, *arguments, **kwargs):
    print('Inside __init__ of {0}.'.format(self.__class__.__name__))
    print('(Actually in Class3Level2)')
    self.arguments = arguments
    self.kwargs = kwargs
    self.set_in = self.__class__.__name__
    return super(Class3Level2, self).__init__(*arguments, **kwargs)


class Class4Level2(Class2Level1, Class1Level1):
  """A level 2 class with a meta class defined in its second parent."""
  Class4Level2 = True

  def __new__(cls, *args, **kwargs):
    # Try removing the cls from the super() args.
    print('Inside __new__ of {0}.'.format(cls.__name__))
    print('(Actually in Class4Level2)')
    return super(Class4Level2, cls).__new__(cls, *args, **kwargs)

  def __init__(self, *arguments, **kwargs):
    print('Inside __init__ of {0}.'.format(self.__class__.__name__))
    print('(Actually in Class4Level2)')
    self.arguments = arguments
    self.kwargs = kwargs
    self.set_in = self.__class__.__name__
    return super(Class4Level2, self).__init__(*arguments, **kwargs)


if __name__ == '__main__':
  from pdb import set_trace
  set_trace()
