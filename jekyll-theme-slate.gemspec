# encoding: utf-8

Gem::Specification.new do |s|
  s.name          = "jekyll-theme-slate"
  s.version       = "0.0.4"
  s.license       = "CC0-1.0"
  s.authors       = ["Jason Costello", "GitHub, Inc."]
  s.email         = ["opensource+jekyll-theme-slate@github.com"]
  s.homepage      = "https://github.com/pages-themes/slate"
  s.summary       = "Slate is a Jekyll theme for GitHub Pages"

  s.files         = `git ls-files -z`.split("\x0").select do |f|
    f.match(%r{^((_includes|_layouts|_sass|assets)/|(LICENSE|README)((\.(txt|md|markdown)|$)))}i)
  end

  s.platform      = Gem::Platform::RUBY
  s.add_runtime_dependency "jekyll", ">= 3.3", "< 5.0"
end
