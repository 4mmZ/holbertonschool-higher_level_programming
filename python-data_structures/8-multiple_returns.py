#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        l = len(sentence)
        f = sentence[0]
        return l, f
    else:
        return None