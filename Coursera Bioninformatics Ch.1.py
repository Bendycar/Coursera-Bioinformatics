# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:57:28 2023

@author: bendc
"""
pattern = ''
string = 'GATCCAGATCCCCATAC'

def mostFrequent(string, k):
    options = []
    options_dict = {}
    for i in range(len(string) - k + 1):
        pattern = string[i:i + k]
        options_dict[pattern] = 0
        options.append(pattern)
    for i in options:
       options_dict[i] += 1
    
    most = max(options_dict.values())
    words = [key for key in options_dict if options_dict[key] == most]
    
    return words
    
    
def patternCount(pattern,string):
    counter = 0
    for i in range(len(string) - len(pattern) + 1):
        if string[i:i+len(pattern)] == pattern:
            counter += 1
    
    return counter

print(mostFrequent('TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT', 3))