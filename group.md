---
title: Group
---

<section class="page-header" style="background-image: url('{{ '/assets/img/header.jpg' | relative_url }}')">
  <h1>Group</h1>
</section>

Group codes and repositories: [github.com/James-Almeida-Group]({{ site.github_group }})

## Current members

<div class="members">
{% for m in site.data.group.current %}{% include member.html m=m %}{% endfor %}
</div>

## Alumni

<div class="members alumni">
{% for m in site.data.group.alumni %}{% include member.html m=m %}{% endfor %}
</div>
