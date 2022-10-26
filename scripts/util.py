import subprocess
from pathlib import Path
from typing import Mapping, Tuple, Union

from pybtex.database.input import bibtex


def latex_to_markdown(s: str) -> str:
    p = subprocess.run("pandoc -f latex -t markdown --wrap none".split(),
                       input=s, text=True, capture_output=True)
    assert p.returncode == 0
    return p.stdout.strip()


def read_summary(path: Union[str, Path]) -> Tuple[Mapping, str]:
    with open(path) as f:
        content = f.read()

        # remove metadata
        if content.strip().startswith("---\n"):
            summary = content.split("---\n")[-1]
            metadata = content.split("---\n")[0]
        else:
            summary = content
            metadata = dict()
    return metadata, summary


def get_articles(summary_dir="src/summaries", bib_path="src/articles.bib"):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_path)

    for article_path in Path(summary_dir).glob("*.md"):
        key = article_path.stem

        try:
            entry = bib_data.entries[key]
        except KeyError as e:
            raise KeyError(
                f"Bib-Key '{key}' not found in references file ({bib_path}).")

        metadata, summary = read_summary(article_path)

        yield dict(
            entry=entry,
            markdown_title=latex_to_markdown(entry.fields["title"]),
            key=key,
            metadata=metadata,
            summary=summary,
        )
