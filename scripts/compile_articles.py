#!/usr/bin/env python3


from pathlib import Path

import subprocess

from pybtex.database.input import bibtex

import argparse


def latex_to_markdown(s):
    p = subprocess.run("pandoc -f latex -t markdown".split(),
                       input=s, text=True, capture_output=True)
    assert p.returncode == 0
    return p.stdout.strip()


def compile(bib_path="src/articles.bib", summary_dir="src/summaries",
            target_path="build/compiled.md", link_titles=True,
            heading_level=2):

    print("Building article.")
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_path)

    article_paths = {}

    for article_path in Path(summary_dir).glob("*.md"):
        key = article_path.stem

        if key not in bib_data.entries.keys():
            raise KeyError(
                f"Bib-Key '{key}' not found in references file ({bib_path}).")

        article_paths[key] = article_path

    articles = list()

    for key, entry in bib_data.entries.items():
        entry = bib_data.entries[key]

        title = latex_to_markdown(entry.fields["title"])

        if key in article_paths:
            print(f"Summary found: '{title}'")

            with open(article_paths[key]) as f:
                summary = f.read()
        else:
            print(f"Summary missing!: '{title}'")
            summary = "*coming soon*"

        articles.append((
            entry.fields["year"],
            title,
            key,
            summary,
            entry.fields.get("url", None)
        ))

    articles = sorted(articles)

    target_path = Path(target_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    with open(target_path, "w") as f:
        for year, title, key, summary, url in articles:
            if url is not None and link_titles:
                title = f"[{title}]({url})"

            heading_prefix = "#" * heading_level
            f.write(f"{heading_prefix} {title} [@{key}]\n\n{summary}\n\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Build article from summaries.')

    parser.add_argument('target_path')
    parser.add_argument('--link_titles', action='store_true')

    args = vars(parser.parse_args())

    try:
        compile(**args)
    except KeyError as e:
        print(e)
        quit(1)
