#!/usr/bin/env python3

import nltk
from nltk.corpus import brown
from math import log
from numpy import argmax
from collections import defaultdict, Counter, deque
import sys
import itertools

class Hypothesis():
    def __init__(self, prob=-sys.maxsize, prev_idx=-1):
        self.prob=prob
        self.prev_idx=prev_idx

class POSDecoder():
    def __init__(self, vocab_size=10000):
        self.tag_word_counts=defaultdict(lambda: Counter())
        self.tag_tag_counts = defaultdict(lambda: Counter())

        self.tag_word_probs = defaultdict(lambda: defaultdict(lambda: -sys.maxsize))
        self.tag_tag_probs = defaultdict(lambda: defaultdict(lambda: -sys.maxsize))
        
        self.vocab = set(x[0] for x in Counter(w.lower() for w in brown.words()).most_common(vocab_size))
        self.tags = Counter(self.cleanTag(t) for w, t in brown.tagged_words())

        self.getCounts()
        self.getProbs()

    def getCounts(self):
        for sent in brown.tagged_sents():
            words = [w.lower() for w,t in sent]
            if set(words) - self.vocab: continue # Ignore sentences with OOVs.
        
            prev_tag = "<START>"
            for word, tag in sent:
                tag = self.cleanTag(tag)
                word = word.lower()
 
                self.tag_word_counts[tag].update((word,))
                self.tag_tag_counts[prev_tag].update((tag,))
                prev_tag = tag
                                
    def getProbs(self):
        actualvocab=set()
        for pos, word_counts in self.tag_word_counts.items():
            total=sum(word_counts.values())
            for word, count in word_counts.items():
                self.tag_word_probs[pos][word]= log(count/total)
                actualvocab.update((word,))
        for pos, pos_counts in self.tag_tag_counts.items():
            total=sum(pos_counts.values())
            for tag, count in pos_counts.items():
                self.tag_tag_probs[pos][tag] = log(count/total)
                
    def cleanTag(self, tag):
        tag=tag.split("-")[0]
        tag=tag.split("+")[0]
        tag=tag.rstrip("$*")
        return tag

    def decode(self, sent):
        # Build DP table, which should be |sents| x |tags|
        tags = list(self.tag_word_probs.keys())

        table = [[Hypothesis(0,-1) for tag in tags] for word in sent]        

        # Initialize the first column with the values from
        # tag_tag_probs based on a previous tag of "<START>"

        start_dict = self.tag_tag_probs["<START>"]
        for i, tag in enumerate(tags):
            table[0][i].prob = start_dict[tag] + self.tag_word_probs[tag][sent[0]]
            
        # Iterate through the rest of the words: for each
        # words, find the MAX of all possible paths to each
        # tag. Store the prev_idx that tells which previous
        # tag gave the best path to that point.

        # TO DO: WRITE THIS LOOP

        
        # Find the highest-probability tag for the last word in the
        # sentence.

        output = deque()
        best_ti = argmax([hyp.prob for hyp in table[-1]])
        best_hyp=table[-1][best_ti]
        output.appendleft(tags[best_ti])

        # Follow the back-pointers to recover the
        # most likely tags for all of the other words in the
        # sentence.        

        for wi in range(len(table)-1,0,-1):
            output.appendleft(tags[best_hyp.prev_idx])
            best_hyp=table[wi-1][best_hyp.prev_idx]

        return output

if __name__=="__main__":
    decoder=POSDecoder()
    sentences = ["i see the sheep","the sheep is in the field", "who went to the store with you", "the plane will land on the land", "the horse raced past the barn fell"]
    for sentence in sentences:
        output = decoder.decode(sentence.split())
        print(list(zip(output, sentence.split())))
