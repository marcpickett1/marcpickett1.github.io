import os, random, plotly.graph_objects as go, numpy as np
from collections import defaultdict

def windowed_derivative(x, y, window_size):
    j = np.searchsorted(x, x + window_size, side="right")
    valid = j < len(x)
    dydx = np.full_like(x, np.nan, dtype=float)
    dydx[valid] = (y[j[valid]] - y[valid]) / (x[j[valid]] - x[valid])
    return (x[valid], dydx[valid])

def readfile(gutendir, fname):
    with open(os.path.join(gutendir, fname), "r", encoding="utf-8") as f:
        try: text = f.read()
        except UnicodeDecodeError: text = ''
    text = "".join(c if 'a' <= c <= 'z' else ' ' for c in text.lower())
    return text.split()

gutendir = "./gutenberg/eng/"
word_per_day = 30_000
max_tokens = word_per_day * 80 * 365  # 80 years

all_files = list(os.listdir(gutendir))
print(f"Found {len(all_files)} files. Reading vocabularies...")

word_to_id = {}
file_vocab_ids = {}
file_lens = {}

for i, fname in enumerate(all_files):
    words = readfile(gutendir, fname)
    ids = set()
    for w in words:
        if w not in word_to_id:
            word_to_id[w] = len(word_to_id)
        ids.add(word_to_id[w])
    if len(ids) > 0:
        file_vocab_ids[fname] = ids
        file_lens[fname] = len(words)
    if (i+1) % 2000 == 0:
        print(f"  Read {i+1}/{len(all_files)} files...")

print(f"Loaded {len(file_vocab_ids)} files, {len(word_to_id):,} unique words.")

# --- Random curriculum ---
print("\n=== Random curriculum ===")
random.seed(42)
random_order = list(file_vocab_ids.keys())
random.shuffle(random_order)

known = set()
vocab_size_lis, words_read_lis, token_i = [], [], 0
for fname in random_order:
    fvocab = file_vocab_ids[fname]
    token_i += file_lens[fname]
    known |= fvocab
    vocab_size_lis.append(len(known))
    words_read_lis.append(token_i)
    if token_i >= max_tokens:
        break

random_times = np.array(words_read_lis) / (word_per_day * 365)
random_vsize = np.array(vocab_size_lis)
print(f"Random: {token_i:,} tokens, vocab {len(known):,}")

# --- Easy (greedy) curriculum ---
print("\n=== Easy (greedy) curriculum ===")

word_to_files = defaultdict(set)
for fname, ids in file_vocab_ids.items():
    for wid in ids:
        word_to_files[wid].add(fname)

new_count = {fname: len(ids) for fname, ids in file_vocab_ids.items()}
okset = set(file_vocab_ids.keys())
known = set()
vocab_size_lis, words_read_lis, token_i = [], [], 0
step = 0

while okset and token_i < max_tokens:
    best_fname = min(okset, key=lambda f: new_count[f])
    fvocab = file_vocab_ids[best_fname]
    new_words = fvocab - known
    for wid in new_words:
        for f in word_to_files[wid]:
            if f in okset:
                new_count[f] -= 1
    known |= new_words
    token_i += file_lens[best_fname]
    okset.remove(best_fname)
    vocab_size_lis.append(len(known))
    words_read_lis.append(token_i)
    step += 1
    if step % 1000 == 0:
        print(f"  Step {step}: {token_i:,} tokens, vocab {len(known):,}, {len(okset)} left")

easy_times = np.array(words_read_lis) / (word_per_day * 365)
easy_vsize = np.array(vocab_size_lis)
print(f"Easy: {token_i:,} tokens, vocab {len(known):,}")

# --- Shared style ---
print("\nGenerating plots...")
plot_template = "plotly_white"
blue = "#636EFA"
red = "#EF553B"
window_size = 1.0

r_dx, r_dy = windowed_derivative(random_times, random_vsize, window_size)
r_rate = r_dy / 365
e_dx, e_dy = windowed_derivative(easy_times, easy_vsize, window_size)
e_rate = e_dy / 365
baseline = 100

# === Main plots (random only) ===

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=random_times, y=random_vsize, mode='lines', line=dict(color=blue), showlegend=False))
fig1.update_layout(title="Vocabulary Growth Over a Lifetime", xaxis_title='"Age" (years)', yaxis_title="Vocabulary Size", template=plot_template, width=900, height=500)
fig1.write_json("vocab_growth.json")
fig1.write_image("vocab_growth.png", scale=2)
print("  Saved vocab_growth.png + .json")

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=r_dx, y=r_rate, mode='lines', line=dict(color=blue), showlegend=False))
fig2.update_layout(title="Vocabulary Growth Rate", xaxis_title='"Age" (years)', yaxis_title="New Words Per Day", template=plot_template, width=900, height=500)
fig2.write_json("vocab_growth_rate.json")
fig2.write_image("vocab_growth_rate.png", scale=2)
print("  Saved vocab_growth_rate.png + .json")

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=r_dx, y=(baseline / r_rate), mode='lines', line=dict(color=blue), showlegend=False))
fig3.update_layout(title="How Long Does It Take to Learn 100 New Words?", xaxis_title='"Age" (years)', yaxis_title=f"Days to Learn {baseline} New Words", template=plot_template, width=900, height=500)
fig3.write_json("days_per_100_words.json")
fig3.write_image("days_per_100_words.png", scale=2)
print("  Saved days_per_100_words.png + .json")

# === Appendix plots (both trajectories) ===

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=random_times, y=random_vsize, mode='lines', name='Random order', line=dict(color=blue)))
fig4.add_trace(go.Scatter(x=easy_times, y=easy_vsize, mode='lines', name='Easy-first order', line=dict(color=red)))
fig4.update_layout(title="Vocabulary Growth: Random vs. Easy-First", xaxis_title='"Age" (years)', yaxis_title="Vocabulary Size", template=plot_template, width=900, height=500, legend=dict(x=0.55, y=0.3))
fig4.write_json("appendix_vocab_growth.json")
fig4.write_image("appendix_vocab_growth.png", scale=2)
print("  Saved appendix_vocab_growth.png + .json")

fig5 = go.Figure()
fig5.add_trace(go.Scatter(x=r_dx, y=r_rate, mode='lines', name='Random order', line=dict(color=blue)))
fig5.add_trace(go.Scatter(x=e_dx, y=e_rate, mode='lines', name='Easy-first order', line=dict(color=red)))
fig5.update_layout(title="Growth Rate: Random vs. Easy-First", xaxis_title='"Age" (years)', yaxis_title="New Words Per Day", template=plot_template, width=900, height=500, legend=dict(x=0.6, y=0.9))
fig5.write_json("appendix_growth_rate.json")
fig5.write_image("appendix_growth_rate.png", scale=2)
print("  Saved appendix_growth_rate.png + .json")

# === Save raw data for render_plots.py ===
np.savez("plot_data.npz",
    random_times=random_times, random_vsize=random_vsize,
    r_dx=r_dx, r_rate=r_rate, r_days=baseline / r_rate,
    easy_times=easy_times, easy_vsize=easy_vsize,
    e_dx=e_dx, e_rate=e_rate,
)
print("  Saved plot_data.npz")

# --- Key stats ---
print("\n=== Key stats ===")
for label, dx, rate in [("Random", r_dx, r_rate), ("Easy-first", e_dx, e_rate)]:
    for age in [1, 5, 10, 20, 40, 60, 75]:
        idx = np.searchsorted(dx, age)
        if idx < len(rate) and rate[idx] > 0:
            days_per_100 = baseline / rate[idx]
            print(f"  {label} age {age}: {rate[idx]:.1f} new words/day, {days_per_100:.1f} days to learn 100 new words")

print("\nDone!")
