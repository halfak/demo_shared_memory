from . import defaults
from .keyed_vectors import demo_kv
from .util import generate_zero_vector


def process(_):
    sum_vector = generate_zero_vector()
    for i in range(defaults.WORDS):
        vector = demo_kv[str(i)]
        for i, val in enumerate(vector):
            sum_vector[i] = sum_vector[i] + val

    return [val / defaults.WORDS for val in sum_vector]
