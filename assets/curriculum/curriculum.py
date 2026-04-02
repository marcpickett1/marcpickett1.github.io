import os, random, plotly.express as px, numpy as np

# Importantly, we read Pat The Bunny before we read Ulysses, so early vocabulary growth is faster.
# I'm not capturing that here.
# Note that I'm using Gutenberg as a proxy for "life experience" (not just language), which is still simplified for babies, but less curated
#   than what we deliberately read to them.
# In this "learning" model, we're memorizing each new "word" the first time we see it.  Real learning is obviously more complex.

# I assume if we sorted the files by "minimum delta".  The effect would be less pronunced, but still present.

# Wait But Why style
#   mv source to github. (See kids.md)
#   Trajectories: "Random", "Easy" and "China trip"
#   This simple model exhibits the phenomenon.
#   What will a year feel like at age 80?  (Age 10, quarter felt like year today.)


def windowed_derivative(x, y, window_size):
    j = np.searchsorted(x, x + window_size, side="right")
    valid = j < len(x)
    dydx = np.full_like(x, np.nan, dtype=float)
    dydx[valid] = (y[j[valid]] - y[valid]) / (x[j[valid]] - x[valid])
    return (x[valid], dydx[valid])

def readfile(gutendir, fname):
    with open(os.path.join(os.path.expanduser(gutendir), fname), "r", encoding="utf-8") as f:
        try: text = f.read()
        except UnicodeDecodeError: text = ''
    text = "".join(c if 'a' <= c <= 'z' else ' ' for c in text.lower())
    words = text.split()
    return words

def get_easiest_text(current_vocab, vocabs, okset):
    min_new_words, easiest_fname = float('inf'), None
    for fname in okset:
        vocab, dlen = vocabs[fname]
        # n_new = len(vocab - current_vocab) / dlen
        # Going absolute (at risk of overly biasing towards weird short texts)
        # Going relative starts with a text of 2M words!
        n_new = len(vocab - current_vocab)
        if n_new < min_new_words: min_new_words, easiest_fname = n_new, fname
    return easiest_fname

def main():
    gutendir = "./gutenberg/eng/"  # directory of .txt files
    word_per_day = 30_000 # Approximate number of total words a person hears/reads per day
    curriculum_file = 'RANDOM' # 'curriculum.dat'
    all_files = set(os.listdir(os.path.expanduser(gutendir)))
    if os.path.exists(curriculum_file):
        with open(curriculum_file, 'r', encoding='utf-8') as f:
            curriculum = [line.strip() for line in f.readlines()]
    elif curriculum_file == 'RANDOM':
        random.seed(42)
        random.shuffle(all_files)
        curriculum = all_files
    else: curriculum = []
    vocabs = {}
    for fname in all_files:
        words = readfile(gutendir, fname)
        fvocab = set(words)
        if len(fvocab) > 0: vocabs[fname] = (fvocab, len(words))
    vocab, token_i = set(), 0
    if not curriculum:
        okset = set(vocabs.keys())
        while okset and token_i < word_per_day * 80 * 365:
            easiest_fname = get_easiest_text(vocab, vocabs, okset)
            fvocab, flen = vocabs[easiest_fname]
            curriculum.append(easiest_fname)
            okset.remove(easiest_fname)
            print(f"Read {token_i:,} words.  |vocab| = {len(vocab):,}.  Reading {easiest_fname} with {len(fvocab-vocab)} new words.  ({len(okset)} texts left).")
            token_i += flen
            vocab |= fvocab
    vocab, vocab_size_lis, words_read_lis, token_i = set(), [], [], 0
    for easiest_fname in curriculum:
        if easiest_fname not in vocabs:
            print(f"Skipping {easiest_fname} -- no vocab")
            continue
        fvocab, flen = vocabs[easiest_fname]
        token_i += flen
        vocab |= fvocab
        vocab_size_lis.append(len(vocab))
        words_read_lis.append(token_i)
    print(f"Processed {token_i:,} tokens, vocab size {len(vocab):,}")
    times = np.array(words_read_lis) / (word_per_day * 365)  # convert to "years"
    vsize = np.array(vocab_size_lis)
    fig = px.line(x=times, y=vsize, labels={"x": '"Age" (years)', "y": "Vocabulary Size"})
    fig.show()
    # Get the "derivative" of the curve: how fast is vocab growing?
    window_size = 365 * 1/365 # One year window
    deriv_xs, deriv = windowed_derivative(times, vsize, window_size)
    vocab_growth_rate = deriv / 365  # convert to new words per day
    fig_deriv = px.line(x=deriv_xs, y=vocab_growth_rate, labels={"x": '"Age" (years)', "y": "Vocabulary Growth Rate (new words/day)"})
    fig_deriv.show()
    baseline = 100 # 100 new words/day
    fig_ratio = px.line(x=deriv_xs, y=(baseline / vocab_growth_rate), labels={"x": '"Age" (years)', "y": f"Days to learn {baseline} new words"})
    fig_ratio.show()
