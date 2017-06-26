#!/usr/bin/python
from collections import Counter
import sys

# This is for pretty output.  Longer words come 1st, then alphabetical
def wordsort(a, b):
  if len(a) > len(b): return -1
  elif len(a) < len(b): return 1
  elif len(a) == len(b) and b < a: return 1
  elif len(a) == len(b) and a < b: return -1
  else: return 0
def tuplewordsort(a, b):
  if a == b: return 0
  if len(a) == 0: return 1
  if len(b) == 0: return -1
  # Sort 1st by length
  for i, j in zip(a, b):
    if len(i) > len(j): return -1
    if len(i) < len(j): return 1
  # OK, now by abc
  for i, j in zip(a, b):
    if i != j: return wordsort(i, j)
  if len(a) > len(b): return -1
  return 1

# Actually find the anagrams
def branchWord(remainder, leftwords, words):
  if len(remainder) == 0: return set([frozenset()])
  leftwords2 = {x for x in leftwords if len(words[x] - remainder) == 0}
  allsets = set()
  for i in leftwords2:
    for dset in branchWord(remainder - words[i], leftwords2, words):
      newset = frozenset(set([i]) | dset)
      allsets.add(newset)
  return allsets
# Find multi-word anagrams.
def multianagram(word, words):
  w = Counter(word.lower())
  # Get rid of all the words that can't be made from words
  leftwords = {x for x in words if len(words[x] - w) == 0}
  # Remove the single-word anagrams
  return {x for x in branchWord(w, leftwords, words) if len(x) > 1}

# Find a 1-word anagrams.  (This is much easier than the multi-word
# case, so can be run by itself if multianagram blows up.)
def fullanagram(word, words):
  w = Counter(word.lower())
  return {x for x in words if len(words[x]-w)==0 and len(w-words[x])==0}

# Create the words list
# wordfile = '/usr/share/dict/words'
wordfile = './words'
words = {x:Counter(x) for x in [x.lower().strip() for x in open(wordfile)]}
# Hack to remove single letter words besides a and I.
for c in 'bcdefghjklmnopqrstuvwxyz':
  if c in words: words.pop(c)
for c in sorted(words):
  if len(c) == 2 and c not in ['ah', 'am', 'an', 'as', 'at', 'ax', 'be', 'by', 'do', 'eh', 'ex', 'go', 'ha', 'he', 'hi', 'ho', 'id', 'if', 'in', 'is', 'it', 'la', 'lo', 'ma', 'me', 'mu', 'my', 'no', 'of', 'oh', 'on', 'or', 'ox', 'pa', 'pi', 'so', 'to', 'uh', 'um', 'up', 'us', 'vs', 'we', 'ye', 'yo']:
    words.pop(c)

# Input word
newword = sys.argv[1]

# Get the 1-word anagrams
fullanagrams = fullanagram(newword, words) - set([newword.lower()])
print '# Full anagrams for', newword, '\n', '\n'.join(sorted(fullanagrams))
sys.stdout.flush()

# Get the multi-word anagrams
print '\n# Partial anagrams for', newword
anagrams2 = multianagram(newword, words)
anagrams = sorted([tuple(sorted(x, wordsort)) for x in anagrams2], tuplewordsort)
for i in anagrams: print ' '.join(i)
