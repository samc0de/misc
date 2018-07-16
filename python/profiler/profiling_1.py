# coding: utf-8

import click
import string
from memory_profiler import profile as mem_prof
from cProfile import runctx as time_prof


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
            lambda x, y: float(x + y), filter(lambda x: x % 2 == 0, range(ip)))
    return value


pcalled, pcalled_gen, psum_filter_map, pmap_filter_map, preduce_filter_map = (
        map(mem_prof, [called, called_gen, map_filter_map, sum_filter_map,
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


def get_memory_profile(funcs, num):  # Generic args if needed.
    # new_funcs = {f_name: mem_prof(func) for func in funcs}
    # new_funcs = map(mem_prof, funcs)
    for func in funcs:
        mem_prof(func)(num)


def funcs_caller(num):
    slotted, vanilla, slotted_subclassed = [], [], []
    for count in xrange(num):
        slotted.append(AlphabeticAttributerSlotted())
        # vanilla.append(AlphabeticAttributerSlottedSubclass())
        # slotted_subclassed.append(AlphabeticAttributer())


@click.command('profile')
@click.argument('num', default=10000000)
@click.option('--mode', type=click.Choice(['time', 'memory']),
        prompt=True, default='memory')
def profile_functions(num, mode='memory'):
    cmd = 'mem_prof(funcs_caller)(num)'
    time_prof(cmd, globals(), locals())


if __name__ == '__main__':
    profile_functions()
