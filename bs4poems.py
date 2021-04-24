# This will not run on online IDE
import requests
from bs4 import BeautifulSoup
from poemBot import getURL
from markupsafe import Markup


def getbs4Poems():
    """
    scrapePoems from poems.org url given in CSV file by calling getURL() from poemBot module
    Returns:
        [array]: [contains poem title, author, date, poem, url]
    """
    URL = str(getURL())
    r = requests.get(URL)
    # If this line causes an error, run 'pip install html5lib' or install html5lib
    soup = BeautifulSoup(r.content, 'html5lib')
    # Escape HTML to make it render in flask
    poem = Markup(
        str(soup.find('div', attrs={'class': 'poem__body px-md-4 font-serif'})))
    title = Markup(
        str(soup.find('h1', attrs={'class': 'card-title'}).contents[0]))
    date = Markup(
        str(soup.find('span', attrs={'class': 'dates'})))
    author = Markup(
        str(soup.find('a', attrs={'author': 'author'})))
    url = str(URL)
    # handle poem's whose URL has changed and can't scrape poem info
    if date == None:
        date = "Sorry, this poem's URL has changed"
    if author == None:
        author = "Sorry, this poem's URL has changed"
    if title == None:
        title = "Sorry, this poem's URL has changed"

    return [title, author, date, poem, url]
