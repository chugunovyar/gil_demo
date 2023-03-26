import logging
import multiprocessing

log_level = logging.INFO
logger = logging.getLogger(__name__)
logger.setLevel(log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
formatter = logging.Formatter('%(asctime)s - %(processName)s - %(threadName)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

number_of_cores = multiprocessing.cpu_count()
number_of_threads = 5
num_of_links = 1000
url = "https://edition.cnn.com/"
"""
I have 8 cores, so I did not describe the behavior when the number of links is divided with the remainder.
This problem could be solved by adding the rest of the links to the last thread along with the main chunk.
Please keep this in mind.
"""
chunk_size = num_of_links // number_of_cores
