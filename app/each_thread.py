import requests


def get_threads_responses(links_to_be_processed: list) -> list[dict[str, int]]:
    responses = []
    for each_link in links_to_be_processed:
        response = requests.get(url=each_link.get("url"))
        responses.append(
            {"id": each_link.get("id"), "status": response.status_code}
        )
    return responses
