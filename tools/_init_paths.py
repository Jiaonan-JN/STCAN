import os.path as osp
import sys


def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)


this_dir = osp.dirname(osp.abspath(__file__))
lib_path = osp.join(this_dir, '..', 'lib')
lib_path = osp.abspath(lib_path)
add_path(lib_path)

