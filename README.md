# Work in Progress: Review of Literature on Growing Neural Networks

The article aims to summarize the existing literature concerned with growing
artificial neural networks. For each paper it will list the most significant
contribution.

## Contributing

### Structure of the Content

All articles in `src/articles.bib` are included in the article (ordered by
year and title). If a summary file with file name matching the bibkey
exists (`src/summaries/{bibkey}.md`), it is added beneath the respective
heading.

To add a new article, simply add it to the bib file and add a new summary file
using the same key. The rest is handled by the github actions.


General comments, as well as the list of contributors, can be found in
`src/intro.md`.

Please verify, the build is handled correctly before pushing/merging to main
(this includes the html as well as the pdf file).


### Local Building and Testing

Content pushed/merged to the main branch is automatically deployed.

Locally, distribution files can be generated using the Makefile.
A python3 installation with the packages listed in `requirements.txt`
is required to build article summaries into one file.

Additionally, pandoc as well as latex installation is required.

`make pdf`: Produces the PDF document (which can the be found in the dist
directory).

`make html`: Produces the html file, copies the stylesheet and references file,
and also produces the PDF (as it can be accessed via the web page).

`make serve`: Runs a local http server in the `dist` folde (after creating the
required files, see `make html`). The build webpage can then be accessed via
`localhost:8000`.
