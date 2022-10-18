CONTENT = src/intro.md build/compiled.md src/outro.md
CONTENT_LINKED = src/intro.md build/compiled_linked.md src/outro.md
BILDIOGRAPHY = src/articles.bib
SUMMARIES = src/summaries

.PHONY: all
all: html

.PHONY: pdf
pdf: dist/growing_review.pdf

.PHONY: html
html: dist/index.html pdf

build/compiled_linked.md: $(SUMMARIES) $(BILDIOGRAPHY)
	python3 scripts/compile_articles.py build/compiled_linked.md --link_titles

build/compiled.md: $(SUMMARIES) $(BILDIOGRAPHY)
	python3 scripts/compile_articles.py build/compiled.md

dist:
	mkdir -p dist

dist/style.css: src/style.css dist
	cp src/style.css dist/style.css

dist/references.bib: dist
	cp $(BILDIOGRAPHY) dist/references.bib


dist/index.html: $(CONTENT_LINKED) templates/template.html dist/style.css dist/references.bib dist
	pandoc $(CONTENT_LINKED) -o build/index.html \
		--template=templates/template.html \
		--bibliography=$(BILDIOGRAPHY)\
		--shift-heading-level-by=1 \
		--citeproc
	mv build/index.html dist/index.html

build/main.tex: $(CONTENT) templates/template.tex dist
	pandoc $(CONTENT) -o build/main.tex \
		--template=templates/template.tex \
		--bibliography=$(BILDIOGRAPHY) \
		--biblatex

dist/growing_review.pdf: build/main.tex dist
	pdflatex -output-directory=build -halt-on-error build/main.tex
	biber build/main
	pdflatex -output-directory=build -halt-on-error build/main.tex
	pdflatex -output-directory=build -halt-on-error build/main.tex
	mv build/main.pdf dist/growing_review.pdf

.PHONY: clean
clean:
	rm -rf build

.PHONY: dev
dev: html dist
	python3 -m http.server -d dist
