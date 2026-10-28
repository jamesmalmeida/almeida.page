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
- `group.md` + `_data/group.yml` — página Group: `current` e `alumni` (name, role, since,
  topic, funding, note, place, lattes = só o número, scholar = URL, orcid = só o identificador, photo = arquivo em `assets/img/group/`).
  Sem foto, o card mostra as iniciais.
- `courses-disciplinas.md` — lista automática das disciplinas (ordenada por `order`, decrescente).
- `_courses/<slug>.md` — uma página por disciplina. Front matter: `title`, `period`,
  `order` ("AAAA-Q"), `image` (banner), `thumb` (miniatura da lista), `redirect_from`
  (URLs antigas do Google Sites, com acento).
- `_includes/` — embeds: `youtube.html id=`, `drive.html id=` (arquivo), `drive-folder.html id=`,
  `sheet.html id=` (planilha). Ex.: `{% include drive.html id="1AbC..." %}`.
- `assets/css/style.css` — todo o visual (cores em variáveis no `:root`; só tema claro, fundo branco — o James não quer modo escuro).

## Tarefas comuns

- **Novo artigo:** inserir um bloco no topo de `_data/publications.yml` (valores com ": "
  entre aspas). Aceitos sem DOI entram sem `url`, com venue "Revista, accepted (ano)".
- **Sempre que adicionar artigo, atualizar o resumo de produção** (`research.md`, bloco `stats`):
  - Publicações: automático (tamanho de `_data/publications.yml`).
  - Citações, h-index, i10: abrir o perfil do Google Scholar (`site.scholar`) pelo plugin do
    Chrome, ler a tabela `#gsc_rsb_st` (coluna "All") e atualizar os números e a data em
    "checked AAAA-MM-DD".
- **Nova disciplina:** criar `_courses/<slug-sem-acento>.md` copiando o front matter de
  outra; material do Drive via includes.
- **Pré-visualizar:** `bundle exec jekyll serve` (requer `ruby-dev` e `bundle install`).

## Publicação

- Repositório: github.com/jamesmalmeida/almeida.page (GitHub Pages, branch `main`, raiz).
- Domínio: www.almeida.page (arquivo `CNAME`); `almeida.page` redireciona para o www.
- DNS na Squarespace Domains (ex-Google Domains): A `@` → 185.199.108–111.153, CNAME `www` →
  jamesmalmeida.github.io. **Não mexer** nos registros do Mailgun (MX, SPF, `krs._domainkey`)
  nem no CNAME de verificação do Google (`engpnpnkvxgg`).
