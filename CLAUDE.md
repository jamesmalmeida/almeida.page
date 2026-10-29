# almeida.page — site pessoal (Jekyll / GitHub Pages)

Site do James M. de Almeida, migrado do Google Sites em 2026-10. O GitHub Pages
compila o site direto (Jekyll 3, sem GitHub Actions), então use apenas plugins da
lista permitida do GitHub Pages (hoje: jekyll-redirect-from, jekyll-seo-tag, jekyll-sitemap).

## Estrutura

- `index.md` — Home: card Group (largura total, fotos dos membros atuais) acima de Research e Courses. `/home` redireciona para `/`.
- Menu (`_layouts/default.html`): Home, Group, Research, Courses.
- `research.md` — interesses, códigos, resumo de produção e lista de publicações.
- `_data/publications.yml` — **todas as publicações**, mais recentes primeiro.
  A página agrupa por `year`. Campos: `title`, `authors` (use `**...**` no próprio nome),
  `venue`, `year`, `url`, `image` (opcional, arquivo em `assets/img/`), `abstract`.
  `pdf` (opcional, arquivo em `assets/pdf/`) mostra um botão "PDF". **Só pôr o PDF da editora
  quando a licença permite**: acesso aberto (Creative Commons) ou APS. ACS, Elsevier, RSC, Wiley,
  Springer, IOP e OTC fechados: só a versão aceita do autor (ex.: do Overleaf), nunca o PDF final.
  PDFs publicados do James: `/data/GDrive/Dropbox/Papers-Published/`.
  `manuscript` (opcional, `assets/pdf/AAAA-am-*.pdf`) mostra o botão "Accepted manuscript": versão
  aceita do autor (Overleaf), com capa contendo o aviso exigido pela editora (ACS, Elsevier CC-BY-NC-ND,
  Springer) e o DOI. Sem marcações de revisão (destaques amarelos etc.).
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
- **Disciplinas (Courses):** `_courses/<slug>.md` com `institution: Ilum|UFABC`, `status: em andamento|concluída`,
  `coteaching` (opcional), `materials:` e `lessons:` (n, title, files[label, file]). A tabela vem de
  `_includes/lessons.html`; arquivos relativos ficam em `assets/courses/<slug>/`, valores com `://` são links.
  - Fonte: `/data/GDrive/Dropbox/Aulas`. Só a **versão mais recente** de cada disciplina; em andamento, só a atual,
    e cada aula entra **depois de dada**.
  - **Nunca publicar** notas, listas de presença, grupos, trabalhos/relatórios/diários de alunos, provas, testes
    em sala, resoluções/gabaritos (inclusive de listas), livros/artigos de terceiros, arquivos internos
    (HANDOVER, CLAUDE.md, scripts de montagem). Copiar arquivo por arquivo, nunca pasta inteira.
  - Slides: `.pptx` → PDF (LibreOffice + Ghostscript), tirando os slides de teste/resolução e os que tenham
    nomes de alunos; notebooks com saídas limpas.
  - **Deck com vídeos:** o PDF sozinho não serve. O `.pptx` limpo (sem testes, notas do apresentador e comentários)
    e os vídeos de aula completa vão para `/data/GDrive/almeida.page-material/<slug>/` (sincroniza com o Google
    Drive pelo Insync; pasta compartilhada "qualquer pessoa com o link") e entram na tabela como link do Drive;
    o PDF fica como "PDF (sem vídeos)".
  - Antes de publicar, conferir o texto de tudo contra a lista de nomes de alunos (montada das planilhas de
    notas, só localmente), e-mails, RAs e chaves de API.
- **Pré-visualizar:** `bundle exec jekyll serve` (requer `ruby-dev` e `bundle install`).

## Publicação

- Repositório: github.com/jamesmalmeida/almeida.page (GitHub Pages, branch `main`, raiz).
- Domínio: www.almeida.page (arquivo `CNAME`); `almeida.page` redireciona para o www.
- DNS na Squarespace Domains (ex-Google Domains): A `@` → 185.199.108–111.153, CNAME `www` →
  jamesmalmeida.github.io. **Não mexer** nos registros do Mailgun (MX, SPF, `krs._domainkey`)
  nem no CNAME de verificação do Google (`engpnpnkvxgg`).
