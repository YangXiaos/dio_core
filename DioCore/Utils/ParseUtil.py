from bs4 import BeautifulSoup


def getBs4Soup(text):
    return BeautifulSoup(text, "lxml")