---
layout: default
title: Marc's Debris
---

### Posts

<ul> {% for post in site.posts %}
{% if post.secondary != null %}
{% else %}
<li>
{{post.date| date: "%Y/%m/%d"}}: <a href="{{ post.url }}">{{ post.title }}</a>
</li>
{% endif %}
{% endfor %} </ul>

***

A simple [chrome extension](https://chrome.google.com/webstore/detail/hnmgemoihkmeokbbnfjackbolifealma?utm_source=chrome-app-launcher-info-dialog) I wrote to help ration my web browsing.

[Montezuma's Revenge in under 5KB](montezuma): A hand-crafted script that achieves infinite score in Atari 2600 Montezuma's Revenge.

[Europe Debris](./debris/europe.pdf) (2006): Also on [Amazon](http://www.amazon.com/EUROPE-DEBRIS-Epic-Gabe-Europe/dp/0557033764).

[A Memex on The Meaning of Life](./debris/meaning.pdf)

Some [help for Marc](marchelp) and [my other page](index).
