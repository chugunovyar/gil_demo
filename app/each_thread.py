import requests


def request_maker(element_id: str, url: str) -> dict[str, int]:
    r = requests.get(url=url)
    return {"id": element_id, "status": r.status_code}


def each_thread(links_to_be_processed: list) -> list[dict[str, int]]:
    responses = []
    for each_link in links_to_be_processed:
        responses.append(
            request_maker(element_id=each_link.get("id"), url=each_link.get("url"))
        )
    return responses
