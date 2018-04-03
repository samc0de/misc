"""Just to test class creation with type.

Classes can be created in runtime/on the fly with 'type' function. This has two
syntaxes, the one we need has signature:
  type('class_name', (tuple, of, superclasses), {'dict of': 'attributes'})

There is a catch with the 'class_name' above, this program is an attempt to
clarify that to myself.
"""
try:
  from ipdb import set_trace
except ImportError:
  from pdb import set_trace


class AClass(object):
  pass


BClass = type('AnotherClass', (AClass,), {'attr': True})


if __name__ == '__main__':
  set_trace()


# Conclusion:
# Here 'BClass' is just a variable name, holding a reference to that class. The
# actual classname however is 'AnotherClass'. We can import BClass name but the
# name AnotherClass is not available to be used in any namespace here. The
# official classname of that class, given by BClass.__name__ holds AnotherClass
# as name.
