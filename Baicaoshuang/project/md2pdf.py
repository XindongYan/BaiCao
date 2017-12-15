import os, re
import sys, getopt
from enum import Enum
from subprocess import call
from functools import reduce

from docopt import docopt

__version__ = '1.0'

def main():
    dest_file = "translation_result.html"
    dest_pdf_file = "translation_result.pdf"

    only_pdf = False

    args = docopt(__doc__, version=__version__)

    dest_file = args['']