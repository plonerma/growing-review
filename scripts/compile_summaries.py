#!/usr/bin/env python3

import argparse
from pathlib import Path

from util import get_articles


def compile(bib_path="src/articles.bib", summary_dir="src/summaries",
            target_path="build/compiled.md", link_titles=True,
            heading_level=2):

    print("Building article.")

    articles = list()

    for a in get_articles(summary_dir=summary_dir, bib_path=bib_path):
        articles.append((
            a["entry"].fields["year"],
            a["markdown_title"],
            a["key"],
            a["summary"],
            a["entry"].fields.get("url", None)
        ))

    articles = sorted(articles)

    target_path = Path(target_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    with open(target_path, "w") as f:
        for year, title, key, summary, url in articles:
            if url is not None and link_titles:
                title = f"[{title}]({url})"

            heading_prefix = "#" * heading_level
            f.write(f"{heading_prefix} {title} [@{key}] {{#sec:{key}}}\n\n{summary}\n\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Build article from summaries.')

    parser.add_argument('target_path')
    parser.add_argument('--link_titles', action='store_true')

    args = vars(parser.parse_args())

    try:
        compile(**args)
    except KeyError as e:
        print("Encountered Error:", repr(e))
        quit(1)
