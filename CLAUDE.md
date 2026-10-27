# almeida.page — site pessoal (Jekyll / GitHub Pages)

Site do James M. de Almeida, migrado do Google Sites em 2026-10. O GitHub Pages
compila o site direto (Jekyll 3, sem GitHub Actions), então use apenas plugins da
lista permitida do GitHub Pages (hoje: jekyll-redirect-from, jekyll-seo-tag, jekyll-sitemap).

## Estrutura

- `index.md` — Home. `/home` redireciona para `/`.
- `research.md` — interesses, códigos, resumo de produção e lista de publicações.
- `_data/publications.yml` — **todas as publicações**, mais recentes primeiro.
  A página agrupa por `year`. Campos: `title`, `authors` (use `**...**` no próprio nome),
  `venue`, `year`, `url`, `image` (opcional, arquivo em `assets/img/`), `abstract`.
- `courses-disciplinas.md` — lista automática das disciplinas (ordenada por `order`, decrescente).
- `_courses/<slug>.md` — uma página por disciplina. Front matter: `title`, `period`,
  `order` ("AAAA-Q"), `image` (banner), `thumb` (miniatura da lista), `redirect_from`
  (URLs antigas do Google Sites, com acento).
- `_includes/` — embeds: `youtube.html id=`, `drive.html id=` (arquivo), `drive-folder.html id=`,
  `sheet.html id=` (planilha). Ex.: `{% include drive.html id="1AbC..." %}`.
- `assets/css/style.css` — todo o visual (cores em variáveis no `:root`, com modo escuro).

## Tarefas comuns

- **Novo artigo:** inserir um bloco no topo de `_data/publications.yml`.
- **Números do Google Scholar** (publicações, citações, h-index, i10): fixos em `research.md`,
  bloco `stats`; o James informa os valores atuais.
- **Nova disciplina:** criar `_courses/<slug-sem-acento>.md` copiando o front matter de
  outra; material do Drive via includes.
- **Pré-visualizar:** `bundle exec jekyll serve` (requer `ruby-dev` e `bundle install`).

## Publicação

- Repositório: github.com/jamesmalmeida/almeida.page (GitHub Pages, branch `main`, raiz).
- Enquanto o DNS de almeida.page ainda aponta para o Google Sites, o site fica em
  jamesmalmeida.github.io/almeida.page com `baseurl: "/almeida.page"`. Ao migrar o domínio:
  `baseurl: ""`, criar `CNAME` com `www.almeida.page` e configurar o DNS.
