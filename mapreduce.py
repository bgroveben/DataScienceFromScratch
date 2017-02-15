from __future__ import division
import math, random, re, datetime
from collections import defaultdict, Counter
from functools import partial
from naive_bayes import tokenize


def word_count_old(documents):
    """ word count without using MapReduce """
    return Counter(word
                   for document in documents
                   for word in tokenize(document))


def wc_mapper(document):
    """ for each word in the document, emit (word,1) """
    for word in tokenize(document):
        yield (word, 1)


def wc_reducer(word, counts):
    """ sum up the counts for a word """
    yield (word, sum(counts))


def word_count(documents):
    """ count the words in the input documents using Mapreduce """

    # create a place to store the grouped values
    collector = defaultdict(list)

    for document in documents:
        for word, count in wc_mapper(document):
            collector[word].append(count)

    return [output
            for word, counts in collector.iteritems()
            for output in wc_reducer(word, counts)]


def map_reduce(inputs, mapper, reducer):
    """ runs MapReduce on the inputs using mapper and reducer """

    collector = defaultdict(list)

    for input in inputs:
        for key, value in mapper(input):
            collector[key].append(value)

    return [output
            for key, values in collector.iteritems()
            for output in reducer(key, values)]


def reduce_with(aggregation_fn, key, values):
    """ reduces a key-value pair by applying aggregation_fn to the values """
    yield (key, aggregation_fn(values))


def values_reducer(aggregation_fn):
    """ turns a function (values -> output) into a reducer """
    return partial(reduce_with, aggregation_fn)


sum_reducer = values_reducer(sum)
max_reducer = values_reducer(max)
min_reducer = values_reducer(min)
count_distinct_reducer = values_reducer(lambda values: len(set(values)))


##
## Analyzing Status Updates
##


status_updates = [
    { "id": 1,
      "username": "bgroveben",
      "text": "Yo, imma be geekin my brainz out, howboudah?",
      "created_at": datetime.datetime(2017, 2, 15, 3, 30, 0),
      "liked_by": ["some_guy", "some_gal", "cousin_tavo"] },
    { "id": 2,
      "username": "cousin_tavo",
      "text": "Yo, user bgroveben has very little respect for grammar!",
      "created_at": datetime.datetime(2017, 2, 16, 4, 30, 0),
      "liked_by": ["some_guy", "some_gal", "bgroveben"] },
    { "id": 3,
      "username": "some_gal",
      "text": "Yo, stop worrying about petty things and focus on the task at hand, people.",
      "created_at": datetime.datetime(2017, 2, 17, 5, 15, 0),
      "liked_by": ["some_guy", "bgroveben", "cousin_tavo"] }
]


def data_science_day_mapper(status_update):
    """ yields (day_of_week, 1) if status_update contains 'data_science' """
    if "yo," in status_update["text"].lower():
        day_of_week = status_update["created_at"].weekday()
        yield (day_of_week, 1)

data_science_days = map_reduce(status_updates,
                               data_science_day_mapper,
                               sum_reducer)


def words_per_user_mapper(status_update):
    user = status_update["username"]
    for word in tokenize(status_update["text"]):
        yield (user, (word, 1))


def most_popular_word_reducer(user, words_and_counts):
    """ given a sequence of (word, count) pairs, return the word with the highest total count """
    word_counts = Counter()
    for word, count in words_and_counts:
        word_counts[word] += count

    word, count = word_counts.most_common(1)[0]

    yield (user, (word, count))


user_words = map_reduce(status_updates,
                        words_per_user_mapper,
                        most_popular_word_reducer)


def liker_mapper(status_update):
    user = status_update["username"]
    for liker in status_update["liked_by"]:
        yield (user, liker)


distinct_likers_per_user = map_reduce(status_updates,
                                      liker_mapper,
                                      count_distinct_reducer)


##
## Matrix Multiplication
##


def matrix_multiply_mapper(m, element):
    """ m is the common dimension (columns of A, rows of B) """
    """ element is a tuple (matrix_name, i, j, value) """
    matrix, i, j, value = element

    if matrix == "A":
        for column in range(m):
            # A_ij is the j-th entry in the sum for each C_i_column
            yield((i, column), (j, value))
    else:
        for row in range(m):
            # B_ij is the i-th entry in the sum for each C-row_j
            yield((row, j), (i, value))


def matrix_multiply_reducer(m, key, indexed_values):
    results_by_index = defaultdict(list)
    for index, value in indexed_values:
        results_by_index[index].append(value)
    # sum up all of the products of the positions with two results
    sum_product = sum(results[0] * results[1]
                      for results in results_by_index.values()
                      if len(results) == 2)
    if sum_product != 0.0:
        yield (key, sum_product)


if __name__ == '__main__':

    documents = ["data science", "big data", "science fiction"]

    wc_mapper_results = [result
                         for document in documents
                         for result in wc_mapper(document)]

    print
    print "Results of wc_mapper_results: "
    print wc_mapper_results
    print

    print "Results of word_count(documents): "
    print word_count(documents)
    print

    print "Word count using MapReduce function: "
    print map_reduce(documents, wc_mapper, wc_reducer)
    print

    print "Data Science Days: "
    print data_science_days
    print

    print "User words: "
    print user_words
    print

    print "Distinct Likers: "
    print distinct_likers_per_user
    print

    ## Matrix Multiplication

    entries = [("A", 0, 0, 3), ("A", 0, 1,  2),
           ("B", 0, 0, 4), ("B", 0, 1, -1), ("B", 1, 0, 10)]

    mapper = partial(matrix_multiply_mapper, 3)
    reducer = partial(matrix_multiply_reducer, 3)

    print "MapReduce Matrix Multiplication: "
    print "entries: ", entries
    print "result: ", map_reduce(entries, mapper, reducer)
    print
