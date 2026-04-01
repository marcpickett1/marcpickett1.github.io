# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal blog and portfolio site for Marc Pickett (marcpickett.com), built with Jekyll and hosted on GitHub Pages. Uses a custom `jekyll-theme-slate` gem defined in this repo.

## Commands

```bash
script/bootstrap                          # Install dependencies (once per environment)
bundle exec jekyll serve --livereload     # Local preview at http://localhost:4000
bundle exec jekyll serve --drafts         # Include drafts in preview
bundle exec jekyll build                  # Build site to _site/
script/cibuild                            # Full CI build (also packages theme gem)
```

A warning-free `bundle exec jekyll build` is the minimum acceptance test.

## Architecture

This repo doubles as both a **Jekyll site** and a **Jekyll theme gem** (`jekyll-theme-slate`):

- `_posts/` — published Markdown posts (front matter required)
- `_drafts/` — in-progress posts (excluded from production build)
- `_layouts/` — Liquid HTML templates (`default.html`, `post.html`)
- `_sass/` — SCSS partials imported via `assets/css/style.scss`
- `assets/` — images, CSS, curriculum/CV files, academic papers
- `_site/` — generated output, never edit manually
- `script/` — bootstrap, cibuild, release automation
- `jekyll-theme-slate.gemspec` — defines the theme as a distributable gem
- `vendor/` — checked-in gems required by GitHub Pages

## Content Conventions

- Post filenames: `_posts/YYYY-MM-DD-title.md` (lowercase, hyphenated slug)
- YAML front matter: 2-space indentation
- Prose: wrap at ~80 characters
- Code blocks: fenced with language tag
- New SCSS partials go in `_sass/` (prefix filename with `_`) and must be imported in `assets/css/style.scss`

## Theme Gem

When modifying layout files, assets, or `jekyll-theme-slate.gemspec`, run `script/cibuild` to verify the gem packages correctly. The `script/release` script tags, builds the gem, and pushes to both GitHub and RubyGems.
