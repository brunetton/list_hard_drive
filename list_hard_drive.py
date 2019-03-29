#!/usr/bin/env python3

"""
Usage:
    {self_filename} <root_dir>
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
        print(str(file.relative_to(root_dir)) + "\t" + humanize.naturalsize(file.stat().st_size))
