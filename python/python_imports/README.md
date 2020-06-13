The relative imports work but imports should be relative to the starting entry point script that's being called with `python my_program.py`


This commit(daf3d399002afc094cb7e52c2292098de6ece2e0) should work with command `python root/__init__.py`.

And this commit(6d155758fa8b60a908cb2541a419611c0c54f07f) should work with command `python __init__.py`


Struture:

(misc-3)    Sun 14 Jun 03:10:10  misc/python   master ✘ ⬆ 
 $ tree python_imports/
python_imports/
├── __init__.py
├── README.md
└── root
    ├── a
    │   ├── __init__.py
    │   ├── module_a.py
    │   └── __pycache__
    │       ├── __init__.cpython-37.pyc
    │       └── module_a.cpython-37.pyc
    ├── b
    │   ├── __init__.py
    │   ├── module_b.py
    │   └── __pycache__
    │       ├── __init__.cpython-37.pyc
    │       └── module_b.cpython-37.pyc
    ├── __init__.py
    └── __pycache__
        └── __init__.cpython-37.pyc


