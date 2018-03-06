"""Experiments with __repr__ and __str__ for understanding."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function



class Vehicle(object):
  def __init__(self, car_type='Commuter'):
    self.type = car_type


class Car(object):
  def __init__(self, car_type='Four wheeler car'):
    return super(Car, self).__init__(car_type)


def main():
  pass


if __name__ == '__main__':
  main()
