from multiprocessing import Queue

from configurator import logger
from custom_thread_with_results import CustomThreadWithResult
from each_thread import each_thread


def each_process(links_to_be_processed: list, queue: Queue):
    thread_chunk_size = len(links_to_be_processed) // 5  # Calculate chunk size for threads
    next_step = 0
    threads_in_process = []
    thread_responses = []

    for i in range(5):
        chunk_of_links = links_to_be_processed[next_step:next_step + thread_chunk_size]
        thread = CustomThreadWithResult(target=each_thread, args=(chunk_of_links,), name=f"thread {i}")
        thread.start()
        threads_in_process.append(thread)
        next_step = next_step + thread_chunk_size
        logger.debug(
            f" with thread {thread.name} "
            f"size {chunk_of_links.__len__()} with first element {chunk_of_links[0]} "
            f"with last element {chunk_of_links[-1]}"
        )

    for thread in threads_in_process:
        thread.join()
        thread_responses = thread_responses + thread.result
    thread_responses = sorted(thread_responses, key=lambda k: k['id'])
    queue.put_nowait(thread_responses)
