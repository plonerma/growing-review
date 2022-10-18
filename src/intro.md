---
title: Review of Literature on Growing Neural Networks
css:
  - "https://fonts.xz.style/serve/inter.css"
  - "https://cdn.jsdelivr.net/npm/\\@exampledev/new.css\\@1.1.2/new.min.css"
  - "style.css"
author:
  - name: Max Ploner
    url: "https://maxploner.de"
    affiliation:
      - name: HU Berlin
        url: "https://www.informatik.hu-berlin.de/en/forschung-en/gebiete/ml-en"
      - name: Science of Intelligence
        url: "https://www.scienceofintelligence.de/"

keywords:
  - computer science
  - machine learning
  - continual learning
  - natural language processing
  - dynamically growing networks
papersize: a4
fontsize: 12pt
classoption:
  - pagesize
  - pdftex
  - twoside
  - BCOR=5mm
documentclass: article
biblio-style: authoryear
slide-level: 2
biblatexoptions:
  - "backend=biber"
numbersections: true
colorlinks: true
link-citations: true
graphics: true
tables: true
microtypeoptions:
  - draft=false
  - tracking=true
  - kerning=true
  - spacing=true
  - spacing=nonfrench
#  - "\\setlength{\\absleftindent}{10pt}"
#  - "\\setlength{\\absrightindent}{10pt}"
indent: true
---


# Introduction

This article aims to summarize the existing literature concerned with growing
artificial neural networks. For each paper it will list the most significant
contribution.
The following four questions will guide the summary of each paper:

1. Why are models grown? What is the goal or metric the approach is evaluated on?
2. When are the models grown?
3. Where are the models grown?
4. How are the the new parts initialized?

Each paper tries to make progress in answering at least one of the questions.
Hence, they can be used to categorize these papers.


# Existing Literature
