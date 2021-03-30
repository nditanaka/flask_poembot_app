#!/usr/bin/python
# main.py
from __future__ import print_function
import subprocess
import time
import socket
import csv
import textwrap
import random


def printPoem():
    # get a random poem
    randPoem = random.choice(allPoems)
    # nicely wrap the content for the printer
    # Title and Author are printed in 'M' medium font, limit is 32 character per line
    # poem is printed in 'S' small font, limit is 32 characters per line
    # book and publisher are in "fontB", limit is 42 character per line
    wrappedTitle = textwrap.fill(randPoem[1], width=32)
    wrappedAuthor = textwrap.fill(randPoem[2], width=32)
    wrappedPoem = ""
    for line in randPoem[3].splitlines():
        wrappedLine = textwrap.fill(line, width=32, subsequent_indent="    ")
        wrappedPoem += wrappedLine + "\n"
    # print the poem
    # return (wrappedTitle, '\n', wrappedPoem, '\n',
        # wrappedAuthor, '\n', randPoem[4], '\n', randPoem[0])
    years = str(randPoem[4]) + '\n'
    author = str(wrappedTitle) + '\n'
    poem = wrappedAuthor + '\n'
    url = str(randPoem[3]) + '\n'
    title = randPoem[0] + '\n'

    # return title + '\n' + author + '\n' + poem + '\n' + years + '\n' + url
    return title, author, poem, years, url
# Print random poem, called on tap


def tap():
    # print a random poem
    return printPoem()


def hold():
    return ('Goodbye!')


# Load up all poems from CSV
# poem CSV is structured with the columns: number,title,author,poem,book
# goldenTreasuryPoems.csv was parsed from the text of Project Gutenberg EBook #19221
# http://www.gutenberg.org/ebooks/19221
# the poem column contains the full text of the poem with no markup, only \n
# the CSV is in PC437 encoding since the printer only supports this character set
with open('poembot_poems_2020.csv') as csvPoems:
    allPoems = list(csv.reader(csvPoems, delimiter=','))

# Start printing
print('Hello!')
print('Ready to print')
tap()
