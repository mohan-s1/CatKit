import os
from sys import path, argv
import ase

from catkit.hub.ase_tools import check_traj


def main(base):
    for roots, dirs, files in os.walk(base):
        traj_files = [f for f in files if f.endswith('traj')]
        for f in traj_files:
            check_traj('{}/{}'.format(roots, f))


if __name__ == '__main__':
    try:
        base = argv[1]
    except IndexError:
        base = '.'
    main(base)
