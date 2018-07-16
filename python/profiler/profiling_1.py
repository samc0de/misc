# coding: utf-8

import click
import string
from memory_profiler import profile


def called(num):
    value = range(num)
    print (len(value))
    return value
def called_gen(num):
    value = xrange(num)
    print ('Do not ask for length, it\'s a generator!')
    return value
def map_filter_map(ip):
    value = map(''.join, map(str, filter(lambda x: x%2 == 0, range(ip))))
    return value
def sum_filter_map(ip):
    value = sum(map(float, filter(lambda x: x%2 == 0, range(ip))))
    return value
def reduce_filter_map(ip):
    value = reduce(
            lambda x, y: float(x + y), filter(lambda x: x%2 == 0, range(ip)))
    return value


pcalled, pcalled_gen, psum_filter_map, pmap_filter_map, preduce_filter_map = (
        map(profile, [called, called_gen, map_filter_map, sum_filter_map,
            reduce_filter_map]))


class AlphabeticAttributer(object):
    def __init__(self, values=string.ascii_letters, debug=False):
        if debug:
            set_trace()
        [setattr(self, x, x + x) for x in values]
        return super(AlphabeticAttributer, self).__init__()

class AlphabeticAttributerSlotted(object):
    __slots__ = tuple(string.ascii_letters)
    def __init__(self, values=string.ascii_letters):
        [setattr(self, x, x + x) for x in values]
        return super(AlphabeticAttributerSlotted, self).__init__()

class AlphabeticAttributerSlottedSubclass(AlphabeticAttributer):
    __slots__ = tuple(string.ascii_letters)
    def __init__(self, values=string.ascii_letters, debug=False):
        [setattr(self, x + x, x + x + x) for x in values]
        return super(AlphabeticAttributerSlottedSubclass,
                self).__init__(values, debug)


# @click.command('profile')
if __name__ == '__main__':
    num = int(1e7)
    pcalled_gen(num)
    pcalled(num)
