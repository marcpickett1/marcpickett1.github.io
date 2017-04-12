---
layout: default
---

[Link to my old page](www/index.html).

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

Some [help for Marc](marchelp).
