#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Organises files in given directories as per below hierarchy.

This library should be using only standard library. It's responsible for
organising files in a given directory in the following fasion.

Example Input:
    delivery01/
        PROJECTNAME_SHOTNAME_TASKNAME.0001.dpx
        PROJECTNAME_SHOTNAME_TASKNAME.0002.dpx
        PROJECTNAME_SHOTNAME_TASKNAME.0003.dpx
        PROJECTNAME_SHOTNAME_TASKNAME.0001.exr
        PROJECTNAME_SHOTNAME_TASKNAME.0002.exr
        PROJECTNAME_SHOTNAME_TASKNAME.0003.exr
        PROJECTNAME_SHOTNAME_TASKNAME.0001.jpg
        PROJECTNAME_SHOTNAME_TASKNAME.0002.jpg
        PROJECTNAME_SHOTNAME_TASKNAME.0003.jpg
Example Output:
    PROJECTNAME/
        DATE/
            PROJECTNAME_SHOTNAME/
                TASKNAME/
                    EXR/
                        PROJECTNAME_SHOTNAME_TASKNAME.0001.exr
                        PROJECTNAME_SHOTNAME_TASKNAME.0002.exr
                        PROJECTNAME_SHOTNAME_TASKNAME.0003.exr
                    DPX/
                        PROJECTNAME_SHOTNAME_TASKNAME.0001.dpx
                        PROJECTNAME_SHOTNAME_TASKNAME.0002.dpx
                        PROJECTNAME_SHOTNAME_TASKNAME.0003.dpx
                    JPG/
                        PROJECTNAME_SHOTNAME_TASKNAME.0001.jpg
                        PROJECTNAME_SHOTNAME_TASKNAME.0002.jpg
                        PROJECTNAME_SHOTNAME_TASKNAME.0003.jpg

Files not adhering to input standards are ignored. Any errors occurred while
creating directories due to OS reasons such as insufficient space, access
issues will not be handled explicitly (=reraised).
"""

from os import path as os_path
import pathlib
from datetime import datetime
import logging
from itertools import product

DATE_FORMAT = '%Y%m%d%H%m'
SEPARATOR = '_'
DATE = datetime.today().strftime(DATE_FORMAT)
# See time performance of repeated dir-creation calls, as this approach avoids
# that but at the cost of bad memory performance, two diff objects hold data
# with similar data (paths and tree).
# %timeit org.organise_files(input_dirs)
# 246 µs ± 71.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
#
# Files created using:
#  tasks = ['TT' + str(x) for x in range(4)]
# 
#  projs = ['P1', 'P22', 'P3', 'P2']
# 
#  shots = ['S' + str(x) for x in range(2, 7)]
# 
#  tasks = ['TT' + str(x) for x in range(2, 5)]
# 
#  base_dir = 'ip_1/'
# 
#  base_dir = 'ip_2/'
# 
#  for p, t, s, e in product(projs, tasks, shots, ftypes):
#      for num in range(4):
#          fl_name = '_'.join((p, s, '.'.join((t, '000%d' % num, e))))
#          with open(base_dir + fl_name, 'wt') as fl:
#              fl.write('')
# 
#  projs = ['P1', 'P2', 'P3']
# 
#  tasks = ['T' + str(x) for x in range(4)]
# 
#  shots = ['S' + str(x) for x in range(4)]
# 
#  base_dir = 'ip_1/'
# 
#  for p, t, s, e in product(projs, tasks, shots, ftypes):
#      for num in range(4):
#          fl_name = '_'.join((p, s, '.'.join((t, '000%d' % num, e))))
#          with open(base_dir + fl_name, 'wt') as fl:
#              fl.write('')
# For 2 dirs: input_dirs = ['ip_1/', 'ip_2/']
# 
# %timeit org.organise_files(input_dirs, out_dir='../out/')
# 101 µs ± 49.7 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
# Also json object to be created.


def get_file_identifiers(input_dirs, base_path):
    projects, tasks, shots, exts, paths = set(), set(), set(), set(), {}
    for input_dir in input_dirs:
        path = pathlib.Path(base_path, input_dir)
        for file in path.iterdir():
            try:
                file_name, _, ext = file.name.split('.')
                project, shot, task = file_name.split(SEPARATOR)
            except ValueError as e:
                logging.warning('{} does not comply with filename standard.'
                        'Ignoring it....'.format(file))
                logging.debug(e)
                continue
            projects.add(project)
            tasks.add(task)
            shots.add(shot)
            exts.add(ext)
            paths[file] = (project, shot, task, ext)
    return paths, projects, tasks, shots, exts


def create_dir_tree(path, projects, date, shots, tasks, exts):
    """Create a directory tree as per above documantation with given params."""
    project_paths = {p: pathlib.Path(path, p, date) for p in projects}
    _ = [p.mkdir(parents=True, exist_ok=True) for p in project_paths.values()]
    output_tree = {}
    for project, shot, task, ext in product(projects, shots, tasks, exts):
        leaf_dir = pathlib.Path(
                project_paths[project],
                SEPARATOR.join((project, shot)),
                task,
                ext.upper())
        leaf_dir.mkdir(parents=True, exist_ok=True)
        output_tree[(project, shot, task, ext)] = leaf_dir
    return output_tree


def organise_files(input_dirs, out_dir, date=DATE, base_path=os_path.curdir):
    """Organise files as per above documented pattern."""
    # Read input dir.
    paths, projects, tasks, shots, exts = get_file_identifiers(
            input_dirs, base_path)
    # Create dir struct.
    out_path = pathlib.Path(base_path, out_dir)
    # Abort in case if dirs can't be created. Exception raised.
    tree = create_dir_tree(out_path, projects, date, shots, tasks, exts)
    # Move files.
    for file, identifiers in paths.items():
        target = tree[identifiers]
        file.rename(target / file.name)
