#!/usr/bin/python3.10
import multiprocessing
import time
from multiprocessing import Process

from configurator import logger, kernels, num_of_links, batch_size, url
from each_process import each_process


class Application:
    links_to_be_processed = []
    list_of_processes = []
    queue = multiprocessing.Queue()
    results = []
    start_time = time.time()

    def __init__(self, number_of_links: int, proc_chunk_size: int):
        self.proc_chunk_size = proc_chunk_size
        self.number_of_links = number_of_links

        for i in range(0, self.number_of_links):
            self.links_to_be_processed.append({"id": i, "url": url})

        logger.info(
            f"CPU kernels: {kernels} "
            f"batch size for each proc: {proc_chunk_size}  "
            f"links to be processed:  {len(self.links_to_be_processed)}"
        )

    def run_app_processes(self):
        next_batch_step = 0
        for i in range(kernels):
            batch_of_links = self.links_to_be_processed[next_batch_step:next_batch_step + batch_size]
            next_batch_step += batch_size
            p = Process(target=each_process, args=(batch_of_links, self.queue), name=f"proc {i}")
            p.start()
            self.list_of_processes.append(p)

        for proc in self.list_of_processes:
            proc.join()

    def results_processing(self):
        while not self.queue.empty():
            self.results = self.results + self.queue.get()
        self.results = sorted(self.results, key=lambda k: k['id'])
        logger.info(f"data processed with time {time.time() - self.start_time} \n results: {self.results}")


if __name__ == '__main__':
    app = Application(number_of_links=num_of_links, proc_chunk_size=batch_size)
    app.run_app_processes()
    app.results_processing()
