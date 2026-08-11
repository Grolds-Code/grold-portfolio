# Portfolio site — build instructions

## Files
- content.py       — all the text, links, and data on the site. Edit this only.
- template.html    — page structure (Jinja2). Edit only if you want to change layout.
- style.css        — visual styling. Edit only if you want to change design.
- favicon.svg      — small browser-tab icon.
- og-image.png     — the 1200x630 image shown in link previews (LinkedIn, Slack, X, etc).
- make_og_image.py — regenerates og-image.png from content.py, so the preview
  stays in sync if you change your name/role/thesis. Run it after editing
  content.py, same as build.py.
- assets/          — JetBrains Mono font files used only by make_og_image.py
  (the site itself loads the font from Google Fonts; this local copy is
  needed because Pillow can't use a web font).
- build.py         — generates index.html from the two files above.
- index.html       — the generated output. Don't edit by hand; it gets overwritten.

## Before going live
In content.py, update these two placeholder values once your domain is registered:
- canonical_url — currently "https://example.com/"
- og_image_url  — currently "https://example.com/og-image.png"; point this at
  wherever og-image.png ends up hosted once the site is live.

Then run `python build.py` again to bake the real URLs in.

## Workflow
1. Open content.py in PyCharm.
2. Edit any text, add or remove a publication, demo, or fellowship entry —
   it's plain Python dicts and lists.
3. Run:  python build.py
4. If you changed name/role/thesis, also run:  python make_og_image.py
5. Open the regenerated index.html in your browser to check it.
6. Repeat.

## First-time setup
pip install -r requirements.txt

## Deploying
index.html, style.css, favicon.svg, and og-image.png together are the whole
site — no server needed. Push them (plus content.py, template.html, build.py
if you want the source under version control too) to a GitHub repo and
enable GitHub Pages, or drag the files into Netlify or Vercel's static drop
zone. Once hosted, update og_image_url in content.py to the real hosted URL
and rebuild.
