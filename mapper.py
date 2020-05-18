#!/usr/bin/env python
# coding: utf-8
import sys
import re
import string
from sklearn.feature_extraction import stop_words 

#stopwords = set(['the', 'and'])
stops = set(stop_words.ENGLISH_STOP_WORDS)

# get all lines from stdin
for line in sys.stdin:
        # remove leading and trailing whitespace
    line = line.strip().lower()
    line = re.sub('[' + string.punctuation + ']', '', line.decode('utf‐8'))
    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stops:
            print '%s\t%s' % (word, "1")
