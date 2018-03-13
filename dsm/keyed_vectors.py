import logging

from .util import generate_random_keyed_vectors

logger = logging.getLogger(__name__)

logger.debug("Loading a random keyed vector in the module")
demo_kv = generate_random_keyed_vectors()
