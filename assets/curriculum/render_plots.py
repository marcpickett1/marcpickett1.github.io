"""Re-render plots from saved plotly JSON files using matplotlib xkcd style.
No need to reprocess the Gutenberg corpus -- just tweak and re-run this."""

import json, base64, warnings
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.font_manager as fm
fm.fontManager.addfont('/home/pickett/.fonts/xkcd-script.ttf')
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore', message='findfont')
plt.xkcd()
plt.rcParams['font.family'] = 'xkcd Script'
plt.rcParams['font.size'] = 14

CHINA_AGE = 28

def decode_trace(trace):
    out = {}
    for key in ['x', 'y']:
        val = trace[key]
        if isinstance(val, dict) and 'bdata' in val:
            out[key] = np.frombuffer(base64.b64decode(val['bdata']), dtype=val.get('dtype', 'f8'))
        else:
            out[key] = np.array(val)
    out['name'] = trace.get('name', '')
    return out

def load_json(path):
    with open(path) as f:
        fig = json.load(f)
    return [decode_trace(t) for t in fig['data']]

def find_bump(x, y, center, window=2):
    mask = (x >= center - window) & (x <= center + window)
    if not mask.any():
        idx = np.searchsorted(x, center)
        return x[idx], y[idx]
    idx = np.where(mask)[0][np.argmax(y[mask])]
    return x[idx], y[idx]

def render_main(json_path, png_path, title, xlabel, ylabel):
    traces = load_json(json_path)
    fig, ax = plt.subplots(figsize=(10, 5.5))
    x, y = traces[0]['x'], traces[0]['y']
    ax.plot(x, y, linewidth=2, color='#636EFA')
    ax.set_title(title, fontsize=18)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # "Trip to China" annotation at the bump
    bx, by = find_bump(x, y, CHINA_AGE)
    yrange = ax.get_ylim()[1] - ax.get_ylim()[0]
    ax.annotate(
        '"Trip to China"',
        xy=(bx, by),
        xytext=(bx - 3, by + yrange * 0.18),
        fontsize=15, color='red', ha='center',
        arrowprops=dict(arrowstyle='->', color='red', lw=2),
    )
    fig.tight_layout()
    fig.savefig(png_path, dpi=150)
    plt.close(fig)
    print(f"  Saved {png_path}")

def render_appendix(json_path, png_path, title, xlabel, ylabel):
    traces = load_json(json_path)
    fig, ax = plt.subplots(figsize=(10, 5.5))
    colors = ['#636EFA', '#EF553B']
    for i, t in enumerate(traces):
        ax.plot(t['x'], t['y'], linewidth=2, color=colors[i], label=t['name'])
    ax.set_title(title, fontsize=18)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(fontsize=12, loc='best')
    fig.tight_layout()
    fig.savefig(png_path, dpi=150)
    plt.close(fig)
    print(f"  Saved {png_path}")

print("Rendering main plots (xkcd style)...")
render_main("vocab_growth.json", "vocab_growth.png",
            "Vocabulary Growth Over a Lifetime", '"Age" (years)', "Vocabulary Size")
render_main("vocab_growth_rate.json", "vocab_growth_rate.png",
            "Vocabulary Growth Rate", '"Age" (years)', "New Words Per Day")
render_main("days_per_100_words.json", "days_per_100_words.png",
            "How Long Does It Take to Learn 100 New Words?", '"Age" (years)', "Days to Learn 100 New Words")

print("Rendering appendix plots...")
render_appendix("appendix_vocab_growth.json", "appendix_vocab_growth.png",
                "Vocabulary Growth: Random vs. Easy-First", '"Age" (years)', "Vocabulary Size")
render_appendix("appendix_growth_rate.json", "appendix_growth_rate.png",
                "Growth Rate: Random vs. Easy-First", '"Age" (years)', "New Words Per Day")

print("Done!")
