CONTENT = src/intro.md build/table.md src/summaries_intro.md build/summaries.md src/outro.md
CONTENT_LINKED = src/intro.md build/table.md src/summaries_intro.md build/summaries_linked.md src/outro.md
BILBIOGRAPHY = src/articles.bib
SUMMARIES = src/summaries/*

.PHONY: all
all: html

.PHONY: pdf
pdf: dist/growing_review.pdf

.PHONY: html
html: dist/index.html

.PHONY: static_files
static_files: src/static/*
	mkdir -p dist
	cp -r src/static/* dist/
	cp -r src/static/* build/
	cp $(BILBIOGRAPHY) dist/references.bib

build/summaries.md: $(SUMMARIES) $(BILBIOGRAPHY)
	python3 scripts/compile_summaries.py $@

build/summaries_linked.md: $(SUMMARIES) $(BILBIOGRAPHY)
	python3 scripts/compile_summaries.py $@ --link_titles

build/table.md: $(SUMMARIES) $(BILBIOGRAPHY)
	python3 scripts/compile_table.py $@

dist/index.html: $(CONTENT_LINKED) templates/template.html static_files
	mkdir -p dist
	pandoc $(CONTENT_LINKED) -o build/index.html \
		--template=templates/template.html \
		--bibliography=$(BILBIOGRAPHY)\
		--filter pandoc-xnos \
		--citeproc \
		--mathjax \
		--toc \
		--default-image-extension=svg
	mv build/index.html dist/index.html

build/main.tex: $(CONTENT) templates/template.tex static_files
	mkdir -p dist
	pandoc $(CONTENT) -o build/main.tex \
		--template=templates/template.tex \
		--filter pandoc-xnos \
		--bibliography=$(BILBIOGRAPHY) \
		--biblatex \
		--default-image-extension=pdf

dist/growing_review.pdf: build/main.tex static_files
	mkdir -p dist
	cd build && pdflatex -output-directory=. -halt-on-error ./main.tex
	biber build/main
	cd build && pdflatex -output-directory=. -halt-on-error ./main.tex
	cd build && pdflatex -output-directory=. -halt-on-error ./main.tex
	cp build/main.pdf $@

.PHONY: clean
clean:
	rm -rf build
	rm -rf dist

.PHONY: dev
dev: html
	mkdir -p dist
	python3 -m http.server -d dist
