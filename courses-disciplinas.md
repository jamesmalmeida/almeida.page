---
title: Courses (Disciplinas)
---

<section class="page-header" style="background-image: url('{{ '/assets/img/header.jpg' | relative_url }}')">
  <h1>Courses (Disciplinas)</h1>
</section>

Material das disciplinas que ministrei. Conteúdo em português.

{% assign courses = site.courses | sort: "order" | reverse %}
{% assign groups = "Ilum|Ilum – Escola de Ciência (CNPEM);UFABC|Universidade Federal do ABC (UFABC)" | split: ";" %}
{% for g in groups %}{% assign parts = g | split: "|" %}
{% assign list = courses | where: "institution", parts[0] %}
{% if list.size > 0 %}
<h2 class="course-group">{{ parts[1] }}</h2>
<div class="course-list">
{% for c in list %}
  <a class="course" href="{{ c.url | relative_url }}">
    {% if c.thumb %}<img src="{{ '/assets/img/' | append: c.thumb | relative_url }}" alt="" loading="lazy">{% else %}<span class="course-thumb">{{ c.title | slice: 0 }}</span>{% endif %}
    <div>
      <h3>{{ c.title }}</h3>
      <p>{{ c.period }} <span class="badge">{{ c.institution }}</span>{% if c.status == 'em andamento' %} <span class="badge badge-live">Em andamento</span>{% endif %}</p>
    </div>
  </a>
{% endfor %}
</div>
{% endif %}
{% endfor %}
