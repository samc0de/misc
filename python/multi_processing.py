#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import multiprocessing
import click


class MyProcess(multiprocessing.Process):
    def __init__(self, proc_id, delay=1):
        self.id = proc_id
        self.delay = delay
        return super(MyProcess, self).__init__()

    def run(self):
        # Use click.echo.
        click.echo('Process id: %s started...' % self.id)
        time.sleep(self.delay)
        click.echo('Completed run of id: %s' % self.id)



@click.command(name='process command')
@click.option('--delay', default=1, help='Process delay.')
@click.argument('limit', type=int)
def process_looper(limit, delay):
    for num in range(limit):
        proc = MyProcess(num, delay)
        proc.start()


if __name__ == '__main__':
    process_looper()
