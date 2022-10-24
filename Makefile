CONTENT = src/intro.md build/compiled.md src/outro.md
CONTENT_LINKED = src/intro.md build/compiled_linked.md src/outro.md
BILDIOGRAPHY = src/articles.bib
SUMMARIES = src/summaries/*

.PHONY: all
all: html

.PHONY: pdf
pdf: dist/growing_review.pdf

.PHONY: html
html: dist/index.html

build/compiled_linked.md: $(SUMMARIES) $(BILDIOGRAPHY)
	python3 scripts/compile_articles.py build/compiled_linked.md --link_titles

build/compiled.md: $(SUMMARIES) $(BILDIOGRAPHY)
	python3 scripts/compile_articles.py build/compiled.md

dist:
	mkdir -p dist

.PHONY: static
static: src/static/* dist
	cp -r src/static/* dist/
	cp -r src/static/* build/

dist/references.bib: dist
	cp $(BILDIOGRAPHY) dist/references.bib


dist/index.html: $(CONTENT_LINKED) templates/template.html dist/references.bib dist static
	pandoc $(CONTENT_LINKED) -o build/index.html \
		--template=templates/template.html \
		--bibliography=$(BILDIOGRAPHY)\
		--shift-heading-level-by=1 \
		--filter pandoc-xnos \
		--citeproc \
		--mathjax \
		--toc \
		--default-image-extension=svg
	mv build/index.html dist/index.html

build/main.tex: $(CONTENT) templates/template.tex dist
	pandoc $(CONTENT) -o build/main.tex \
		--template=templates/template.tex \
		--filter pandoc-xnos \
		--bibliography=$(BILDIOGRAPHY) \
		--biblatex \
		--default-image-extension=pdf

dist/growing_review.pdf: build/main.tex dist static
	cd build && pdflatex -output-directory=. -halt-on-error ./main.tex
	biber build/main
	cd build && pdflatex -output-directory=. -halt-on-error ./main.tex
	cd build && pdflatex -output-directory=. -halt-on-error ./main.tex
	cp build/main.pdf dist/growing_review.pdf

.PHONY: clean
clean:
	rm -rf build
	rm -rf dist

.PHONY: dev
dev: html dist
	python3 -m http.server -d dist
