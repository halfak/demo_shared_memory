import logging

from . import defaults
from .util import generate_random_keyed_vectors, generate_zero_vector

logger = logging.getLogger(__name__)
logger.debug("Loading a random keyed vector as a global")
demo_kv = generate_random_keyed_vectors()


def process(_):
    global demo_kv  # Here we have an explicit global
    sum_vector = generate_zero_vector()
    for i in range(defaults.WORDS):
        vector = demo_kv[str(i)]
        for i, val in enumerate(vector):
            sum_vector[i] = sum_vector[i] + val

    return [val / defaults.WORDS for val in sum_vector]
