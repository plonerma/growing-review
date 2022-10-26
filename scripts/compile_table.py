import argparse
from pathlib import Path

from pybtex.database.input import bibtex

from util import get_articles


def compile(bib_path="src/articles.bib", summary_dir="src/summaries",
            target_path="build/table.md"):

    print("Building table.")

    articles = sorted(
        list(get_articles(summary_dir=summary_dir, bib_path=bib_path)),
        key=lambda a: (a["year"], a["markdown_title"], a["key"]))

    target_path = Path(target_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    with open(target_path, "w") as f:
        f.write('::: {.sortable .paper-categories}\n\\scriptsize\n')


        heads = [
            "Short Title", "Year", "Why?", "When?", "Where?", "How?", "Paper"
        ]

        f.write(" | ".join(heads))
        f.write("\n")
        f.write("|".join(["---"]*len(heads)))
        f.write("\n")


        for article in articles:
            fields = [
                f"[{article['markdown_shorttitle']}](#sec:{article['key']})",
                article["year"],
                article["metadata"].get("why", ""),
                article["metadata"].get("when", ""),
                article["metadata"].get("where", ""),
                article["metadata"].get("how", ""),
                f"@{article['key']}"
            ]

            f.write(" | ".join(fields))
            f.write("\n")

        caption = "Papers according to the three questions (see *@sec:introduction). {#tbl:papers_cat}"

        f.write(f"\n: {caption}\n\n")

        f.write("\\normalsize\n:::\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build table for articles.')

    parser.add_argument('target_path')

    args = vars(parser.parse_args())

    try:
        compile(**args)
    except KeyError as e:
        print("Encountered Error:", repr(e))
        quit(1)
