#!/usr/bin/env python3

"""
Usage:
    {self_filename} <root_dir> [options]

Options:
    --raw-size   do not print file sizes in "human readable" way, but use real size, in bytes
"""

import os
from pathlib import Path

import humanize
from docopt import docopt

args = docopt(__doc__.format(self_filename=Path(__file__).name))
root_dir = args['<root_dir>']

for folder, subs, files in os.walk(root_dir, topdown=True, onerror=None, followlinks=False):
    if folder == '.git':
        continue
    for filepath in files:
        file = Path(Path(folder) / filepath)
        if file.is_symlink():
            continue
        size_str = file.stat().st_size if args["--raw-size"] else humanize.naturalsize(file.stat().st_size)
        print("{} \t {}".format(str(file.relative_to(root_dir)), size_str))
