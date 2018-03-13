"""
Demos a multiprocessing job using a big blob as an explicit global.

Usage:
    demo_import_memory [--verbose] [--debug]

Options:
    --verbose        Print dots and stuff to note progress
    --debug          Print debug logging
"""
import logging
import sys
from multiprocessing import Pool

from dsm import defaults, global_processor
from dsm.util import main_for_demo

logger = logging.getLogger(__name__)


def main(argv=None):
    return main_for_demo(run, __doc__, argv)


def run(verbose=False):
    logger.debug("Starting extractor pool with {0} processes."
                 .format(defaults.PROCESSES))
    extractor_pool = Pool(processes=defaults.PROCESSES)
    for ob in extractor_pool.imap(global_processor.process,
                                  range(defaults.OBSERVATIONS)):
        if verbose:
            sys.stderr.write(".")
            sys.stderr.flush()

    if verbose:
        sys.stderr.write("\n")


if __name__ == "__main__":
    main()
