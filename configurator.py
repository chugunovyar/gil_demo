import logging.config
import logging
import multiprocessing

import yaml

with open('./logging.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
logging.config.dictConfig(config)
logger = logging.getLogger("main")

kernels = multiprocessing.cpu_count()
num_of_links = 1000
url = "https://edition.cnn.com/"
"""
I have 8 cores. The number of links is divided without a remainder.
Therefore, I did not describe the behavior when the number of cores is not divided without a remainder
"""
batch_size = num_of_links // kernels
