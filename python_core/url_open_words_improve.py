""" Retrieve and print words from an URL.
        
    Ussage:
        python3 words.py <URL>
"""
import sys
from  urllib.request import urlopen

def fetch_words():
    """ Fetch a list of words from URL.
        
        Args:
            url: The URL of UTF-8 text document.
        
        Returns:
            A list of strings containing the words from
            the document. 
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words= line.decode('utf8').split()
        for word in line_words:
            story_words.append(word) 
    story.close()
    return story_words
    

def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__== "__main__":
    main(sys.argv[1])



# This will import our file as a module in Python.
# The name of the module is the same as the filename. 
import url_open_words_improve
help(list)
help(fetch_words)