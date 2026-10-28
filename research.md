---
title: Research
---

<section class="page-header" style="background-image: url('{{ '/assets/img/header.jpg' | relative_url }}')">
  <h1>Research</h1>
</section>

## Research Interests

All my research involves molecular simulations, by means of both classical molecular dynamics and ab initio calculations. The main focus of my research today is on oil-brine-rocks interactions, studying from the electronic level, where surface adsorptions and reactions are explored, and also at an atomistic level, where fluid-fluid and fluid-rock interfaces are simulated. I have also research on cement, nanofluidics and electronic transport.

- Natural Language Processing
- Database development (with Antonio Augusto Alves Junior): [www.midb.cloud](http://www.midb.cloud)
- High throughput calculations
- Machine Learning
- Water confinement
- Oil-brine-rock interactions
- Cement based materials
- Nanofluidics
- Electronic transport

## Group

Meet the students and postdocs I supervise, current and former, on the [Group]({{ '/group' | relative_url }}) page.

## Codes

Codes are available on GitHub:

- Personal: [github.com/jamesmalmeida]({{ site.github }})
- Group: [github.com/James-Almeida-Group]({{ site.github_group }})

## Production Summary

<div class="stats">
  <div><strong>{{ site.data.publications | size }}</strong><span>Publications</span></div>
  <div><strong>637</strong><span>Citations</span></div>
  <div><strong>14</strong><span>h-index</span></div>
  <div><strong>21</strong><span>i10-index</span></div>
</div>

Citations and indices: [Google Scholar]({{ site.scholar }}), checked 2026-10-27.

## Publications

{% assign by_year = site.data.publications | group_by: "year" %}
{% for y in by_year %}
<h3 class="year">{{ y.name }}</h3>
{% for p in y.items %}{% include publication.html pub=p %}{% endfor %}
{% endfor %}
