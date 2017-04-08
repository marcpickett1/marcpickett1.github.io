---
layout: default
---

[Link to another page](another-page).

[Immortal](immortal).

[The Castle](castle).

[Link to my old page](www/index.html).

[Help for Marc](test).

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

