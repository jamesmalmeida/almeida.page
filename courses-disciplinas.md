---
title: Courses (Disciplinas)
---

<section class="page-header" style="background-image: url('{{ '/assets/img/header.jpg' | relative_url }}')">
  <h1>Courses (Disciplinas)</h1>
</section>

Material das disciplinas que ministrei. Conteúdo em português.

{% assign courses = site.courses | sort: "order" | reverse %}
<div class="course-list">
{% for c in courses %}
  <a class="course" href="{{ c.url | relative_url }}">
    {% if c.thumb %}<img src="{{ '/assets/img/' | append: c.thumb | relative_url }}" alt="" loading="lazy">{% endif %}
    <div>
      <h2>{{ c.title }}</h2>
      <p>{{ c.period }}</p>
    </div>
  </a>
{% endfor %}
</div>
