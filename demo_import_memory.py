"""
Demos a multiprocessing job using a big blob imported as a module var.

Usage:
    demo_import_memory [--verbose] [--debug]

Options:
    --verbose        Print dots and stuff to note progress
    --debug          Print debug logging
"""
import sys
from multiprocessing import Pool

from dsm import defaults, import_processor
from dsm.util import main_for_demo


def main(argv=None):
    return main_for_demo(run, __doc__, argv)


def run(verbose=False):

    extractor_pool = Pool(processes=defaults.PROCESSES)
    for ob in extractor_pool.imap(import_processor.process,
                                  range(defaults.OBSERVATIONS)):
        if verbose:
            sys.stderr.write(".")
            sys.stderr.flush()

    if verbose:
        sys.stderr.write("\n")


if __name__ == "__main__":
    main()
