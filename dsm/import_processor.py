from . import defaults
from .util import generate_zero_vector

class extractor:
    def __init__(self, demo_kv):
        self.demo_kv=demo_kv

    def process(self, _):
        sum_vector = generate_zero_vector()
        for i in range(defaults.WORDS):
            vector = self.demo_kv[str(i)]
            for i, val in enumerate(vector):
                sum_vector[i] = sum_vector[i] + val

        return [val / defaults.WORDS for val in sum_vector]
