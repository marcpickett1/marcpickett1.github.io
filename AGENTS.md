# Repository Guidelines

## Project Structure & Module Organization
The site runs on Jekyll. Content lives in `_posts/` for published articles, with in-progress drafts in `_drafts/` and standalone pages at the repository root. Layout templates reside in `_layouts/`, shared styles in `_sass/`, and site assets (images, JS, fonts) in `assets/`. The generated output in `_site/` is disposable—never edit it manually. Automation utilities sit in `script/`, while `jekyll-theme-slate.gemspec` defines the bundled theme. `vendor/` captures checked-in dependencies required by GitHub Pages.

## Build, Test, and Development Commands
Run `script/bootstrap` once per environment to install Bundler and gem dependencies. Use `bundle exec jekyll serve --livereload` for a local preview at `http://localhost:4000`. Execute `bundle exec jekyll build` before committing to confirm the site renders cleanly. CI mirrors `script/cibuild`, which performs the build and packages the theme gem—run it locally when touching layout, asset, or gemspec files.

## Coding Style & Naming Conventions
Author Markdown posts with YAML front matter and wrap prose at roughly 80 characters. Name new posts `_posts/YYYY-MM-DD-title.md`, keeping slugs lowercase and hyphenated. Indent YAML with two spaces, and prefer fenced code blocks with language tags. House new SCSS partials in `_sass/` (filename prefixed with `_`) and import them through `assets/css/style.scss`. Follow standard Ruby style (two-space indentation, snake_case filenames) for any scripts.

## Testing Guidelines
Treat a warning-free `bundle exec jekyll build` as the minimum acceptance test. After layout or asset tweaks, run `bundle exec jekyll serve --drafts` and review the affected pages in the browser. When updating the theme gem metadata or assets, execute `script/cibuild` and inspect the generated `.gem` artifact in the repository root.

## Commit & Pull Request Guidelines
Write short, imperative commit subjects (e.g., `Add masonry gallery layout`). Isolate unrelated content, asset, and configuration updates. PR descriptions should list the verification commands run, call out edits to `_config.yml` or theme files, and attach screenshots or preview URLs for visual changes. Reference related issues and request a second maintainer review for any theme or configuration adjustments.
