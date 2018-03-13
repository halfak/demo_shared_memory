import logging
import random

import docopt

from .defaults import N_VECTORS, VECTOR_LENGTH


def generate_random_keyed_vectors(n=N_VECTORS, vector_length=VECTOR_LENGTH):
    return {str(i): [random.random() for j in range(vector_length)]
            for i in range(n)}


def generate_zero_vector(vector_length=VECTOR_LENGTH):
    return [0] * vector_length


def main_for_demo(run_func, doc, argv):
    args = docopt.docopt(doc, argv=argv)

    logging.basicConfig(
        level=logging.INFO if not args['--debug'] else logging.DEBUG,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )
    logging.getLogger('requests').setLevel(logging.WARNING)

    verbose = args['--verbose']

    return run_func(verbose=verbose)
