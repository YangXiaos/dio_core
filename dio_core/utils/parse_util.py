from bs4 import BeautifulSoup


def get_bs4_soup(text):
    return BeautifulSoup(text, "lxml")