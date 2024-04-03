# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:05:48 2024

@author: bendc
"""

# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i +(n//2)])
    
    return array

def PatternCount(Pattern, Text):
    counter = 0
    for i in range(len(Text) -len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            counter += 1
    
    return counter

# Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    
    array[0] = PatternCount(symbol, Genome[0:n//2])
                            
    for i in range(1,n):
        
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i] - 1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i] + 1
    return array


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
# import sys
# lines = sys.stdin.read().splitlines()
# print(FasterSymbolArray(lines[0],lines[1]))


def SkewArray(Text):
    skew = {}
    skew[0] = 0
    
    for i in range(len(Text)):
        if Text[i] == 'A' or Text[i] == 'T':
            skew[i+1] = skew[i]
        if Text[i] == 'C':
            skew[i+1] = skew[i] - 1
        if Text[i] == 'G':
            skew[i+1] = skew[i] + 1
    
    skewlist = [i for i in skew.values()]
    
    return skewlist

def MinimumSkew(Genome):
    positions = []
    array = SkewArray(Genome)
    MinSkew = min(array)
    
    for i in range(len(array)):
        if array[i] == MinSkew:
            positions.append(i)
            
    return positions

def HammingDistance(p, q):
    Ham = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            Ham += 1
    
    return Ham

def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance((Text[i:i+len(Pattern)]), Pattern) <= d:
            positions.append(i)
    
    return positions

def ApproximatePatternCount(Text, Pattern, d):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance((Text[i:i+len(Pattern)]), Pattern) <= d:
            count += 1
    
    return count