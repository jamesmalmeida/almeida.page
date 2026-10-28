---
title: Home
redirect_from:
  - /home
---

<section class="page-header" style="background-image: url('{{ '/assets/img/header.jpg' | relative_url }}')">
  <h1>James M. de Almeida</h1>
</section>

<div class="cards">
  <a class="card card-wide" href="{{ '/group' | relative_url }}">
    <div class="card-faces">
      {% for m in site.data.group.current %}{% if m.photo %}<img src="{{ '/assets/img/group/' | append: m.photo | relative_url }}" alt="{{ m.name }}" loading="lazy">{% endif %}{% endfor %}
    </div>
    <h2>Group</h2>
    <p>Current members and alumni of the research group.</p>
  </a>
  <a class="card" href="{{ '/research' | relative_url }}">
    <img src="{{ '/assets/img/home-research.jpg' | relative_url }}" alt="James M. de Almeida usando óculos de realidade virtual diante de uma visualização molecular" loading="lazy">
    <h2>Research</h2>
    <p>Information about my research.</p>
  </a>
  <a class="card" href="{{ '/courses-disciplinas' | relative_url }}">
    <img src="{{ '/assets/img/courses-books.jpg' | relative_url }}" alt="" loading="lazy">
    <h2>Courses</h2>
    <p>Information about the current and past courses. In Portuguese only.</p>
  </a>
</div>

## Contact

Email: <a href="mailto:{{ site.email }}">{{ site.email }}</a>
