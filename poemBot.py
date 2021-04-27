#!/usr/bin/python
# main.py
from __future__ import print_function
import subprocess
import time
import socket
import csv
import textwrap
import random
import requests

from bs4 import BeautifulSoup

# from lib.bs4 import BeautifulSoup
from markupsafe import Markup

# Load up all poems from CSV
# poem CSV is structured with the columns: number,title,author,poem,book
# goldenTreasuryPoems.csv was parsed from the text of Project Gutenberg EBook #19221
# http://www.gutenberg.org/ebooks/19221
# the poem column contains the full text of the poem with no markup, only \n
# the CSV is in PC437 encoding since the printer only supports this character set
with open("poembot_poems_2020.csv") as csvPoems:
    allPoems = list(csv.reader(csvPoems, delimiter=","))


def getURL():
    randPoem = random.choice(allPoems)
    return randPoem[3]


# Start printing
print("Hello!")
print("Ready to print")


def getbs4Poems():
    """
    scrapePoems from poems.org url given in CSV file by calling getURL() from poemBot module
    Returns:
        [array]: [contains poem title, author, date, poem, url]
    """
    URL = str(getURL())
    r = requests.get(URL)
    # If this line causes an error, run 'pip install html5lib' or install html5lib
    soup = BeautifulSoup(r.content, "html5lib")
    # Escape HTML to make it render in flask
    poem = Markup(
        str(soup.find("div", attrs={"class": "poem__body px-md-4 font-serif"}))
    )
    title = Markup(str(soup.find("h1", attrs={"class": "card-title"}).contents[0]))
    date = Markup(str(soup.find("span", attrs={"class": "dates"})))
    author = Markup(str(soup.find("a", attrs={"itemprop": "author"})))

    # instructions = recipeSoup.find("span", itemprop="name")
    url = str(URL)
    # handle poem's whose URL has changed and can't scrape poem info
    if date == None:
        date = " "
    if author == None:
        # card-subtitle
        author = Markup(str(soup.find("a", attrs={"itemprop": "card-subtitle"})))
    if title == None:
        title = "Sorry, this poem's URL has changed"
    print("author", author)

    return [title, author, date, poem, url]
