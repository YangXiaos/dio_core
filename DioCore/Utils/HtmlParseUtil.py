from bs4 import BeautifulSoup


def parse(html:str) -> BeautifulSoup:
    return BeautifulSoup(html, "lxml")
