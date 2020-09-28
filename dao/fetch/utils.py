from typing import Union

import requests

from bs4 import BeautifulSoup


def parse_url_to_bs(url: str) -> Union[BeautifulSoup, None]:
    try:
        res = requests.get(url)
        res.raise_for_status()

    except requests.RequestException:
        return None

    return BeautifulSoup(res.text, "html.parser")
