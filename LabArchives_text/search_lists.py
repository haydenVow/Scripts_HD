# Searches the given text file for ordered lists associated with the keyword given as a command line argument.

import re
import os
import sys
import logs
import nltk
import argparse

#regex to match a number list of arbitrary length
pattern = re.compile("\d+\.\s+.*?\n(?:\d+\.\s+.*?\n)*", re.MULTILINE | re.DOTALL | re.VERBOSE)

def search_lists(file):
    with open(file, 'r') as f:
        text = f.read()

    matches = pattern.findall(text)

    return matches

def search_lists_for_keyword(keyword, matches):
    # searches for the keyword in the matches
    # outputs the results to a file titled with the keyword + .txt
    # logs the number of matches

    # create a file to write the results to
    file = keyword + '.txt'
    with open(file, 'w') as f:
        for match in matches:
            if keyword in match:
                f.write(match)
                f.write('')
                logs.logger.info(f'found match for {keyword}')


# configure argparse
# expecting arbitrary number of keywords, and only one file
parser = argparse.ArgumentParser(description='Searches the given text file for ordered lists associated with the keyword given as a command line argument.')
# arguement for keywords -k
parser.add_argument('-k', '--keywords', nargs='+', help='keywords to search for')
parser.add_argument('-f','--file', help='file to search')
args = parser.parse_args()

# search the file for lists
matches = search_lists(args.file)
# search the lists for the keyword
for keyword in args.keywords:
    search_lists_for_keyword(keyword, matches)




