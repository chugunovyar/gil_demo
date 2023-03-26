import requests


def each_thread(links_to_be_processed: list) -> list:
    responses = []
    for each_link in links_to_be_processed:
        r = requests.get(url=each_link.get("url"))
        responses.append({"id": each_link.get("id"), "status": r.status_code})
    return responses
