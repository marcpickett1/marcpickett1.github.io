---
layout: post
title: "Fnordnet: The fnord only thing they fear is fnord."
---

[^1]: Recognizing that permanent fulfillment of desire is impossible, Buddhism teaches that a person should seek to free themselves from desire.


## A Puzzle: How can we allow general learning *and* innate instincts?

Both biological and artificial systems benefit from general learning, since adaptability is a key to robust success.  For mammalian brains, the
Mountcastle hypothesis proposes that the neocortex is a general learning system. The same cortical circuitry that does high-level planning also
does seeing and hearing.  Sur and Rubenstein even suggest that a newborn ferret's auditory cortex can learn to "see".  Artificial systems, such
as Transformers, have shown that the same neural circuitry can be used for language, vision, and other modalities, with the only differentiator
being the data fed to these systems.

On the other hand, innate instincts are also essential for some species survival.  An anecdotal example is a beaver raised in human captivity
since infancy that builds a "dam" inside its human owners' home using household items.  Presumably, this beaver had never been instructed on how
to build a dam, yet it had a drive to do so.

One possibility for how this drive is genetically encoded is that a special module in the beaver's brain is dedicated to dam building.  This
module "hard codes" the neural structure all the way from grounding in visual and auditory signals to motor control.  Essentially saying "When
you see these patterns, take these actions".  The problem with this module is it would break if we were to reroute a baby beaver's optic nerve
to its auditory cortex.  Or if we were to permute the baby beaver's retinotopic mapping, essentially changing the "pixels" that travel along the
optic nerve.

Of course, biology is never so simple, but this raises the question of *Is it conceivable that the baby beaver's brain has a "dam building"
circuit that is innate, but at the same time is plastic enough so that it's vision and other modalities are as flexible as that of a ferret?*

## Making the problem concrete

To approach this, I've made some assumptions that hopefully simplify the problem while still attacking the core.
1. The baby beaver's experience is completely unsupervised.  At no point should the process rely on explicit labels.
2. There are invariants that all "dam building" processes share: E.g., stacking objects, moving objects, etc..  Of course, words like "stack"
   and "move" ultimately need to be grounded in the beaver's sensory experience, but we can encode "floating" abstractions.
3. Solving a classification problem *without relying on labels available during learning or assuming a specific sensory configuration* is
   sufficient to address the core problem, which is how concepts can be innately encoded without explicit grounding or labels.  If a beaver
   learns concepts like "move", "stack", and "object", I hope it's not too far a stretch to imagine that it can be rewarded for "stacking
   objects".

Given these assumptions, I propose a Baby version of The Baby Beaver Problem: (The Baby Baby-Beaver-Problem.)

## The Baby Baby-Beaver-Problem: Fear the FNORDs!

In this setup, we assume a passive unsupervised learning system.  There are no labels or actions.  The system is given a stream of fixed-length
vectors representing 26 English "letters" plus a space/other.  The sequences are from common English texts.  We assume that the sequence
distribution is fixed for all Beaver worlds.  The system is given no other information from the environment.  We consider our system a success
if after "training" there is a node that is active if and only if the system has just seen the letter sequence "F-N-O-R-D".  (Note that this
sequence is extremely rare outside the writings of Shea and Wilson.  We may reasonably assume that the system never sees this sequence during
training.)  If we succeed, we can hook up the "FNORD detector" to a large negative reward in a control system, and, with some liberties, claim
that our system has an innate fear of FNORDs.

The "letters" that the vectors represent have a 1:1 correspondence with the English alphabet, but the system isn't given labels or any explicit
knowledge whether two vectors represent the same letter.  (If we assume we're told whether two vectors represent the same letter, then the
problem is a fairly trivial cipher decoding: We simply find a permutation that matches the unigram and bigram frequency of English letters.)
Each letter vector is a fixed dimensionality (D x 1), but we don't know what this is beforehand.  Concretely, the letters could be color or
grayscale images, but the images might be permuted or otherwise transformed.  (If English phonemes had a 1:1 correspondence with spelling, we
could even consider short audio clips of individual phonemes.)

## A solution attempt

The core idea is to exploit the N-gram distribution of English letters.

This is non-trivial because the system needs to simultaneously learn which letter map to which and which letters are the same as others.

My approach: Exploit an innately encoded N-gram distribution for the characters.  (I assume that this distribution is relatively stable.)

I created an objective that is forced to use the ngram distribution to predict next characters.  It then uses KL to see if its two predictions
match (its prediction using an encoder vs. using the ngram model from its encoding of other characters).  I also add a "self prediction" loss to
prevent encoding collapse.

I can show that this objective is optimized if I cheat and pretrain an encoder using labels.  But when training end-to-end without cheating, the
optimizer rarely finds this and gets a loss substantially higher.



[We should mention all the things that didn't work.  E.g., Character frequency matching.  Just using bigrams.]


