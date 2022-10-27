CONTENT = src/intro.md build/table.md src/summaries_intro.md build/summaries.md src/outro.md
CONTENT_LINKED = src/intro.md build/table.md src/summaries_intro.md build/summaries_linked.md src/outro.md
BILBIOGRAPHY = src/articles.bib
SUMMARIES = src/summaries/*
STATIC_SRC_FILES := $(shell find src/static/ -type f)
STATIC_FILES := $(patsubst src/static/%,build/%,$(STATIC_SRC_FILES)) $(patsubst src/static/%,dist/%,$(STATIC_SRC_FILES)) dist/references.bib

.PHONY: all pdf html clean dev

all: html pdf

pdf: dist/growing_review.pdf

html: dist/index.html


debug:
	@echo $(STATIC_SRC_FILES)
	@echo $(STATIC_FILES)

dist/references.bib: $(BILBIOGRAPHY)
	mkdir -p $(@D)
	cp $(BILBIOGRAPHY) dist/references.bib

build/%: src/static/%
	mkdir -p $(@D)
	cp $< $@

dist/%: src/static/%
	mkdir -p $(@D)
	cp $< $@

build/summaries.md: $(SUMMARIES) $(BILBIOGRAPHY)
	python3 scripts/compile_summaries.py $@

build/summaries_linked.md: $(SUMMARIES) $(BILBIOGRAPHY)
	python3 scripts/compile_summaries.py $@ --link_titles

build/table.md: $(SUMMARIES) $(BILBIOGRAPHY)
	python3 scripts/compile_table.py $@

dist/index.html: $(CONTENT_LINKED) templates/template.html $(STATIC_FILES)
	pandoc $(CONTENT_LINKED) -o build/index.html \
		--template=templates/template.html \
		--bibliography=$(BILBIOGRAPHY)\
		--filter pandoc-xnos \
		--citeproc \
		--mathjax \
		--toc \
		--default-image-extension=svg
	cp build/index.html dist/index.html

build/main.tex: $(CONTENT) templates/template.tex $(STATIC_FILES)
	pandoc $(CONTENT) -o build/main.tex \
		--template=templates/template.tex \
		--filter pandoc-xnos \
		--bibliography=$(BILBIOGRAPHY) \
		--biblatex \
		--default-image-extension=pdf

dist/growing_review.pdf: build/main.tex $(STATIC_FILES)
	cd build && pdflatex -output-directory=. -halt-on-error ./main.tex
	biber build/main
	cd build && pdflatex -output-directory=. -halt-on-error ./main.tex
	cd build && pdflatex -output-directory=. -halt-on-error ./main.tex
	cp build/main.pdf $@

clean:
	rm -rf build
	rm -rf dist

dev: html
	mkdir -p dist
	python3 -m http.server -d dist
