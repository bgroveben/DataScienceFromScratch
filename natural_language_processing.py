#!# This file can output quite a bit of data, so I have commented out a number of function calls and print statements.

from __future__ import division
import math, random, re
from collections import defaultdict, Counter
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt


def plot_resumes(plt):
    data = [ ("big data", 100, 15), ("Hadoop", 95, 25), ("Python", 75, 50),
         ("R", 50, 40), ("machine learning", 80, 20), ("statistics", 20, 60),
         ("data science", 60, 70), ("analytics", 90, 3),
         ("team player", 85, 85), ("dynamic", 2, 90), ("synergies", 70, 0),
         ("actionable insights", 40, 30), ("think out of the box", 45, 10),
         ("self-starter", 30, 50), ("customer focus", 65, 15),
         ("thought leadership", 35, 35)]

    def text_size(total):
        """ equals 8 if the total is 0, 28 if the total is 200 """
        return 8 + total / 200 * 20

    for word, job_popularity, resume_popularity in data:
        plt.text(job_popularity, resume_popularity, word,
                 ha='center', va='center',
                 size=text_size(job_popularity + resume_popularity))
    plt.xlabel("Popularity on Job Postings")
    plt.ylabel("Popularity on Resumes")
    plt.axis([-10, 110, -10, 110])
    plt.show()
# plot_resumes(plt)


##
## n-gram models
##


def fix_unicode(text):
    return text.replace(u"\u2019", "'")


def get_document():
    url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    content = soup.find("div", "article-body")   # find article-body div tags
    regex = r"[\w']+|[\.]"                       # matches a word or a period

    document = []

    for paragraph in content("p"):
        words = re.findall(regex, fix_unicode(paragraph.text))
        document.extend(words)

#   print document
    return document
# get_document()


def generate_using_bigrams(transitions):
    current = "."  # this means that the next word will start a sentence.
    result = []
    while True:
        next_word_candidates = transitions[current]    # bigrams (current, _)
        current = random.choice(next_word_candidates)  # choose one at random
        result.append(current)                         # append it to results
        if current == ".": return " ".join(result)     # if "." then we're done


def generate_using_trigrams(starts, trigram_transitions):
    current = random.choice(starts)  # choose a random starting word
    prev = "."                       # and precede it with a '.'
    result = [current]
    while True:
        next_word_candidates = trigram_transitions[(prev, current)]
        next = random.choice(next_word_candidates)
        prev, current = current, next
        result.append(current)
        if current == ".":
            return " ".join(result)


def is_terminal(token):
    return token[0] != "_"


def expand(grammar, tokens):
    for i, token in enumerate(tokens):
        # ignore terminals
        if is_terminal(token): continue
        # choose a replacement at random
        replacement = random.choice(grammar[token])

        if is_terminal(replacement):
            tokens[i] = replacement
        else:
            tokens = tokens[:i] + replacement.split() + tokens[(i+1):]
        return expand(grammar, tokens)
    # if we reach this point we have gone through all of the terminals and are done
    return tokens


def generate_sentence(grammar):
    return expand(grammar, ["_S"])


##
## Gibbs Sampling
##
