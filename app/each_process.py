from multiprocessing import Queue

from app.custom_thread_with_results import CustomThreadWithResult
from app.each_thread import get_threads_responses
from configurator import logger


def each_process(links_to_be_processed: list, queue: Queue, num_of_threads: int):
    thread_chunk_size = len(links_to_be_processed) // num_of_threads  # Calculate chunk size for threads
    next_step = 0
    thread_responses = []

    for thread_num in range(num_of_threads):
        chunk_of_links = links_to_be_processed[next_step:next_step + thread_chunk_size]
        thread = CustomThreadWithResult(target=get_threads_responses, args=(chunk_of_links,), name=f"thread {thread_num}")
        thread.start()
        thread.join()
        thread_responses = thread_responses + thread.result
        next_step = next_step + thread_chunk_size
        try:
            logger.debug(
                f" with thread {thread.name} "
                f"size {chunk_of_links.__len__()} with first element {chunk_of_links[0]} "
                f"with last element {chunk_of_links[-1]}"
            )
        except IndexError:
            print("number_of_threads can't be less then chunk_size")
    thread_responses = sorted(thread_responses, key=lambda k: k['id'])
    queue.put_nowait(thread_responses)
