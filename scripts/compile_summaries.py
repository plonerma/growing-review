#!/usr/bin/env python3

import argparse
from pathlib import Path

from util import get_articles


def compile(bib_path="src/articles.bib", summary_dir="src/summaries",
            target_path="build/compiled.md", link_titles=True,
            heading_level=2):

    print("Building article.")

    articles = sorted(
        list(get_articles(summary_dir=summary_dir, bib_path=bib_path)),
        key=lambda a: (a["year"], a["markdown_title"], a["key"]))

    target_path = Path(target_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    with open(target_path, "w") as f:
        for article in articles:

            title = article["markdown_title"]
            key = article["key"]
            summary = article["summary"]

            if article["url"] is not None and link_titles:
                title = f"[{title}]({article['url']})"

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
