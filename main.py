#!/usr/bin/python3.10
import multiprocessing
import time
from multiprocessing import Process

from configurator import logger, number_of_cores
from app.each_process import each_process

import argparse


class Application:
    queue = multiprocessing.Queue()
    results = []
    start_time = time.time()

    def __init__(self, number_of_links: int, proc_chunk_size: int, num_of_threads, url):
        self.proc_chunk_size = proc_chunk_size
        self.number_of_links = number_of_links
        self.num_of_threads = num_of_threads
        self.links_to_be_processed = [{"id": id, "url": url} for id in range(self.number_of_links)]

        logger.info(
            f"CPU kernels: {number_of_cores} "
            f"batch size for each proc: {proc_chunk_size}  "
            f"links to be processed:  {len(self.links_to_be_processed)}"
        )

    def run_app_processes(self):
        next_batch_step = 0
        for core in range(number_of_cores):
            batch_of_links = self.links_to_be_processed[next_batch_step:next_batch_step + chunk_size]
            next_batch_step += chunk_size
            proc = Process(target=each_process, args=(batch_of_links, self.queue, self.num_of_threads), name=f"proc {core}")
            proc.start()
            proc.join()

    def results_processing(self):
        while not self.queue.empty():
            self.results = self.results + self.queue.get()
        self.results = sorted(self.results, key=lambda k: k['id'])
        logger.info(f"data processed with time {time.time() - self.start_time} \n results: {self.results}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа для обработки ссылок'
    )
    parser.add_argument(
        '--number_of_threads',
        type=int,
        default=5,
        help='количество потоков',
    )
    parser.add_argument(
        '--num_of_links',
        type=int,
        default=16,
        help='количество ссылок',
    )
    parser.add_argument(
        '--url',
        default="https://edition.cnn.com/",
        help='url адрес',
    )
    args = parser.parse_args()

    chunk_size = args.num_of_links // number_of_cores

    app = Application(
        number_of_links=args.num_of_links,
        proc_chunk_size=chunk_size,
        num_of_threads=args.number_of_threads,
        url=args.url,
    )
    app.run_app_processes()
    app.results_processing()
