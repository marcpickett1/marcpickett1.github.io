#!/usr/bin/env python3
"""
Read an edge list CSV (source,target,value) and emit a Sankey diagram.

Usage:
  python sankey_from_edges.py edges.csv out.html
  python sankey_from_edges.py edges.csv out.html --png out.png
"""

import argparse
import pandas as pd
import plotly.graph_objects as go


def build_sankey(df: pd.DataFrame, title: str = "Funds flow") -> go.Figure:
    # Normalize column names
    cols = {c.lower().strip(): c for c in df.columns}
    for required in ("source", "target", "value"):
        if required not in cols:
            raise ValueError(f"CSV must contain a '{required}' column (case-insensitive). Got: {list(df.columns)}")

    src_col, tgt_col, val_col = cols["source"], cols["target"], cols["value"]

    # Make node list + index mapping
    nodes = pd.Index(pd.concat([df[src_col], df[tgt_col]], ignore_index=True).astype(str).unique())
    node_index = {name: i for i, name in enumerate(nodes)}

    sources = df[src_col].astype(str).map(node_index).tolist()
    targets = df[tgt_col].astype(str).map(node_index).tolist()
    values  = df[val_col].astype(float).tolist()

    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="snap",  # keeps it tidy for tree-like flows
                node=dict(
                    label=nodes.tolist(),
                    pad=18,
                    thickness=18,
                    line=dict(width=0.5),
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values,
                ),
            )
        ]
    )
    fig.update_layout(
        title=title,
        font=dict(size=13),
        margin=dict(l=20, r=20, t=60, b=20),
    )
    return fig


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("edges_csv", help="CSV with columns: source,target,value")
    ap.add_argument("out_html", help="Output HTML file")
    ap.add_argument("--png", dest="out_png", default=None, help="Optional PNG output (requires kaleido)")
    ap.add_argument("--title", default="Your $100 cost basis — outflows", help="Chart title")
    args = ap.parse_args()

    df = pd.read_csv(args.edges_csv)
    fig = build_sankey(df, title=args.title)

    fig.write_html(args.out_html, include_plotlyjs="cdn")

    if args.out_png:
        # Kaleido export
        fig.write_image(args.out_png, scale=2)

    print(f"Wrote {args.out_html}" + (f" and {args.out_png}" if args.out_png else ""))


if __name__ == "__main__":
    main()
