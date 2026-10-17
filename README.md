# stargazer1995.github.io

Personal site for **StarGazer** — autonomous driving, systems work, and
astrophotography. Built with Hugo and the LoveIt theme, published to GitHub
Pages.

## Content sources

The site deliberately keeps two Notion databases apart:

| Source | Notion database | Hugo section | Purpose |
|---|---|---|---|
| Blog Pages | `a5584e7f-b264-40b7-b3fa-268da9ee8560` | `content/posts` | Essays, books, travel, life |
| Tech Notes | `3fcb3b02-81c4-812f-b0ef-d69e5c01aab8` | `content/tech` | Engineering notes, paper breakdowns, project writeups |

Only rows with `pstatus = 已发布` are published. `ptype = page` rows land in
`content/pages`.

## Pipeline

`.github/workflows/Notion2Hugo.yml` runs every two hours and on demand:

1. Sync **Blog Pages** → `content/posts`.
2. Sync **Tech Notes** → `content/tech`.
3. `scripts/postprocess_notion.py` downloads Notion-hosted images into
   `static/images/notion/` and rewrites the temporary S3 URLs to local paths.
4. Commit changed content and deploy the Hugo build to GitHub Pages.

Required repository secrets:

- `NOTION_SECRET` — Notion integration token.
- `NOTION_DATABASE_ID` — Blog Pages database id.
- `PICBED_CONFIG` — optional; only used if `pic_migrate` is enabled.

The Tech Notes database id is stored directly in the workflow because it is
not a secret. Update the constant there if the database is replaced.

## Local development

```bash
git submodule update --init --recursive
hugo server --themesDir themes
```

Hugo extended 0.114+ is required for the theme's SCSS pipeline.

## Layout

- `layouts/index.html` — custom homepage (hero, tech cards, writing, projects).
- `static/css/home.css` — homepage styles, light/dark aware.
- `data/projects.yaml` — project cards on the homepage.
- `content/tech/_index.md` — Tech Notes section landing page.

The homepage reads `site.RegularPages` from the `tech` and `posts` sections, so
new Notion rows appear automatically after a sync.
