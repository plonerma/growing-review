#!/usr/bin/env python3

import argparse
from pathlib import Path

from util import get_articles


def compile(bib_path="src/articles.bib", summary_dir="src/summaries",
            target_path="build/table.md"):

    print("Building table.")

    # Retrieve summaries and articles
    articles = sorted(
        list(get_articles(summary_dir=summary_dir, bib_path=bib_path)),
        key=lambda a: (a["year"], a["markdown_title"], a["key"]))

    # Compile table for all articles
    target_path = Path(target_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    with open(target_path, "w") as output_file:
        # Write fencing div: html uses class for styling
        output_file.write('::: {.sortable .paper-categories}\n')

        # Decrease font size in latex (in html this is ingored)
        output_file.write('\\scriptsize\n')

        # Write table heading
        heads = [
            "Short Title", "Year", "Why?", "When?", "Where?", "How?", "Paper"
        ]

        output_file.write(" | ".join(heads))
        output_file.write("\n")

        # Write line spereating head and body of the table
        output_file.write("|".join(["---"]*len(heads)))
        output_file.write("\n")

        for article in articles:
            fields = [
                f"[{article['markdown_shorttitle']}](#sec:{article['key']})",
                article["year"] or "",
                article["metadata"].get("why") or "",
                article["metadata"].get("when") or "",
                article["metadata"].get("where") or "",
                article["metadata"].get("how") or "",
                f"@{article['key']}"
            ]

            output_file.write(" | ".join(fields))
            output_file.write("\n")

        # Caption of the table
        caption = (
            "Papers according to the three questions (see *@sec:introduction)."
            " {#tbl:papers_cat}"
        )

        output_file.write(f"\n: {caption}\n\n")

        # Return to normal font size in latex (in html this is ingored)
        output_file.write("\\normalsize\n:::\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build table for articles.')

    parser.add_argument('target_path')

    args = vars(parser.parse_args())

    try:
        compile(**args)
    except KeyError as e:
        print("Encountered Error:", repr(e))
        quit(1)
