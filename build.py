"""
Builds index.html from template.html + content.py.

Usage:
    python build.py

Run this any time you edit content.py. It regenerates index.html
in this same folder — open that file in a browser to preview.
"""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

import content as c

HERE = Path(__file__).parent

env = Environment(loader=FileSystemLoader(HERE), autoescape=False)
template = env.get_template("template.html")

html = template.render(
    site=c.SITE,
    research=c.RESEARCH_STATEMENT,
    publications=c.PUBLICATIONS,
    demos_intro=c.DEMOS_INTRO,
    demos=c.DEMOS,
    open_source=c.OPEN_SOURCE,
    experience=c.EXPERIENCE,
    fellowships=c.FELLOWSHIPS,
    recognition=c.RECOGNITION,
)

output_path = HERE / "index.html"
output_path.write_text(html, encoding="utf-8")

print(f"Built {output_path} ({len(html):,} characters)")
