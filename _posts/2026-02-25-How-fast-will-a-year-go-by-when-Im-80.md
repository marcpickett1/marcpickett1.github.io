---
layout: post
title: "How fast will a year go by when I'm 80?"
---

[^1]: Recognizing that permanent fulfillment of desire is impossible, Buddhism teaches that a person should seek to free themselves from desire.


*A toy model based on learning new "words"*

Most people report the same experience:

* Childhood felt long.
* Adulthood feels compressed.
* A week in a radically different place can feel like a month.

Here's a simple hypothesis:

> **You register the passage of time when you learn something genuinely new.**
> When nothing new is learned, time passes—but you don't remember it.

This isn't meant as a literal claim about neurons or language.
It's a toy model. But it turns out to line up surprisingly well with lived experience.



### A simple model of "registered time"

Imagine your mind maintains a growing *vocabulary* of concepts.

* Early in life, almost everything is new.
* Later, most experiences reuse existing concepts.
* Occasionally, you enter a new domain and learn many new concepts again.

If *registered time* corresponds to moments when your internal vocabulary grows, then:

* early life should feel dense and slow,
* later life should feel fast,
* but radically new experiences should still stretch time.

We can test this idea with text.



### The experiment

Treat **words** as "concepts."

1. Take ~12,000 English books from Project Gutenberg—about 830 million words, roughly a lifetime of reading at 30,000 words per day for 75 years.
2. Shuffle them into a random order.
3. Feed them through a learner that memorizes each new word the first time it appears.
4. Track the number of **distinct words** seen so far.

This is a classic result in quantitative linguistics: vocabulary growth is **sublinear**. It slows down, but never stops.

That's exactly what we want.



### What the curve looks like

![Vocabulary Growth Over a Lifetime]({{site.url}}/assets/curriculum/vocab_growth.png)

The shape is unmistakable: steep early growth that gradually flattens. By "age 10," you've already acquired about 350,000 words. By 40, growth has slowed to a crawl. By 60, the curve is nearly flat.

This is Heaps' law in action. And it already looks a lot like the subjective experience of aging.



### The growth rate tells the real story

The vocabulary curve is suggestive, but the derivative is the key quantity. If time perception tracks novelty, what matters is *how many new words you learn per day*.

![Vocabulary Growth Rate]({{site.url}}/assets/curriculum/vocab_growth_rate.png)

You start life learning ~270 new words per day. By age 10, it's dropped to ~70. By age 40, you're down to ~35. By age 60, about 25. The decline is steep and relentless—exactly the "time speeds up" curve that people report.

Notice the **lumps**. The growth rate isn't a smooth decay. There are bursts—sudden spikes where vocabulary shoots up. Those correspond to encountering a new author, genre, or domain. In other words: **out-of-distribution inputs**. We'll come back to this.



### What does a year feel like?

Here's the punchline. If it takes you N days to learn 100 new concepts, and those learning events are what you *remember*, then N is a rough measure of how compressed time has become. It's how many calendar days it takes to accumulate what used to be a single day's worth of novelty.

![How Long Does It Take to Learn 100 New Words?]({{site.url}}/assets/curriculum/days_per_100_words.png)

At "age 1," it takes less than a day to learn 100 new words. Every day is packed.

By "age 10," it takes about 1.5 days. Childhood still feels rich.

By "age 40," it takes nearly 3 days. A week has two "real" days in it.

By "age 60," it takes 4–5 days. A month has maybe six memorable days.

Remember what a school quarter felt like at age 10? About three months, crammed with events. That's roughly what a *year* feels like at 60—the same number of learning events, stretched over four times as many calendar days.



### China vs. your normal life

The lumps in the growth rate curve make a striking real-world prediction.

A week in your normal routine:

* mostly reuses existing concepts,
* adds very few "new words,"
* collapses in memory.

A week in China (or anywhere radically unfamiliar):

* new language cues,
* new social norms,
* new rituals,
* new prediction failures everywhere.

In model terms: you've switched corpora.

It's like suddenly reading a book from a completely different domain. Vocabulary growth spikes, and subjective time stretches.

That's why:

> **7 days in a radically different place can feel like a month of normal life.**


### Aging through this lens

This model suggests a simple picture:

* Childhood: almost every day adds new vocabulary → time feels slow.
* Adulthood: most days reuse old vocabulary → time feels fast.
* Major life changes (moves, relationships, new careers): vocabulary spikes → time expands again.

Time doesn't feel fast because "nothing happens."
It feels fast because **nothing new is learned**.



### What this is (and isn't)

This is not a claim that:

* the brain literally stores words,
* language is the only thing that matters,
* or that this is a complete theory of memory.

It *is*:

* a minimal, computational toy model,
* grounded in well-known linguistic statistics (Heaps' law, Zipf's law),
* that explains aging, routine, and travel with one mechanism.

No metaphysics required.



### The takeaway

> **You experience time in proportion to how much you learn.**

You can't stop the long-term slowdown.
But you can locally stretch time by doing things that force you to learn genuinely new "words"—new domains, new cultures, new roles, new ways of predicting the world.

China isn't special.
It's just far away in vocabulary space.

---

## Runnable code

```python
import os, random, plotly.express as px

gutendir = "~/gutenberg/eng/"  # directory of .txt files

random.seed(42)
all_files = sorted(os.listdir(os.path.expanduser(gutendir)))
random.shuffle(all_files)

vocab, points, token_i = set(), [], 0
while token_i < 1_000_000_000 and all_files:
    fname = all_files.pop()
    with open(os.path.join(os.path.expanduser(gutendir), fname), "r", encoding="utf-8") as f:
        try: text = f.read()
        except UnicodeDecodeError: text = ''
    text = "".join(c if 'a' <= c <= 'z' else ' ' for c in text.lower())
    words = text.split()
    for word in words:
        if word not in vocab:
            # A "learning" event!
            vocab.add(word)
            points.append((token_i, len(vocab)))
        token_i += 1

fig = px.line(
    x=[x[0] for x in points], y=[x[1] for x in points],
    labels={"x": '"Time" (Position in Text)', "y": "Vocabulary Size"},
)
fig.show()
```

---

## Appendix: Does the order of books matter?

The corpus used here is the English-language portion of [Project Gutenberg](https://www.gutenberg.org/ebooks/offline_catalogs.html), available for bulk download via their [offline catalogs and mirror sites](https://www.gutenberg.org/help/mirroring.html).

What if, instead of encountering books randomly, you always read the easiest next book—the one that introduces the fewest new words? This is a greedy "easy-first" curriculum, roughly analogous to a life of maximum routine.

![Vocabulary Growth: Random vs. Easy-First]({{site.url}}/assets/curriculum/appendix_vocab_growth.png)

The random curve (blue) is the sublinear shape from above. The easy-first curve (red) stays nearly linear for decades—the greedy algorithm keeps picking books that are almost entirely redundant with what's already known—then *explodes* at the end when it's forced to read the exotic texts it had been deferring.

![Growth Rate: Random vs. Easy-First]({{site.url}}/assets/curriculum/appendix_growth_rate.png)

The easy-first growth rate stays flat around 20–25 new words per day for decades. The greedy curriculum has engineered a life of maximum predictability. Then, past "age 55," it can no longer avoid the hard texts and the rate suddenly climbs—eventually *faster* than anything in the random learner's early life.

The random learner has a childhood full of wonder that gradually fades—the universal human experience. The easy-first learner lives in a long, flat middle: the life equivalent of never leaving your hometown, never changing careers, never reading outside your genre. But the deferred novelty doesn't disappear. It piles up.

---

## References

* Heaps, H. S. (1978). *Information Retrieval: Computational and Theoretical Aspects*. Academic Press.
* Zipf, G. K. (1949). *Human Behavior and the Principle of Least Effort*. Addison-Wesley.
* Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory*. Wiley.
* Anderson, J. R. (1990). *The Adaptive Character of Thought*. Lawrence Erlbaum.
