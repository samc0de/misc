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
# BASE_DIR = os_path.curdir
# See time performance of repeated dir-creation calls, as this approach avoids
# that but at the cost of bad memory performance, two diff objects hold data
# with similar data (paths and tree).
# Also json object to be created.

def organise_files(input_dirs, date=DATE, base_path=os_path.curdir):
    """Organise files as per above documented pattern."""
    # base_output_path
    # Read input dir.
    # def get_file_identifiers()
    projects, tasks, shots, exts, paths = set(), set(), set(), set(), {}
    for input_dir in input_dirs:
        path = pathlib.Path(base_path, input_dir)
        for file in path.iterdir():
            try:
                file_name, _, ext = file.name.split('.')
                project, shot, task = file_name.split(SEPARATOR)
            except ValueError as e:
                logging.warning('{} does not comply with filename standard.'
                        'Ignoring it....'.format(file.name))
                logging.debug(e)
                continue
            projects.add(project)
            tasks.add(task)
            exts.add(ext)
            paths[file] = (project, shot, task, ext)
    # Create dir struct.
    # if not tree:
    # Abort in case if dirs can't be created. Exception raised.
    tree = create_dir_tree(path, projects, date, shots, tasks, exts)
    # Move files.
    for file, identifiers in paths.items():
        # file.rename(tree[(project, shot, task, ext)])
        target = tree[identifiers]
        file.rename(target, file)


def create_dir_tree(path, projects, date, shots, tasks, extensions):
    """Create a directory tree as per above documantation with given params."""
    project_paths = {p: pathlib.Path(path, p, date) for p in projects}
    _ = [p.mkdir(exists_ok=True) for p in project_paths.values()]
    output_tree = {}
    for project, shot, task, ext in product(projects, tasks, shots, exts):
        leaf_dir = pathlib.Path(
                project_paths[project],
                SEPARATOR.join((project, shot)),
                task,
                ext)
        leaf_dir.mkdir(parents=True, exists_ok=True)
        output_tree[(project, shot, task, ext)] = leaf_dir.name
    return output_tree


def get_or_create(path):
    """Create"""
