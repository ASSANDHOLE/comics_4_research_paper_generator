.PHONY: paper
paper: main.tex
	pdflatex -output-directory=output -jobname=paper -quiet main.tex
	$(MAKE) bib
	pdflatex -output-directory=output -jobname=paper -quiet main.tex
	pdflatex -output-directory=output -jobname=paper -quiet main.tex
	cp output/paper.pdf ./paper.pdf

.PHONY: bib
bib:
	mkdir -p output/bib/
	cp -r bib/* output/bib/
	cd output && bibtex paper && cd ..

.PHONY: clean
clean:
	rm -rf paper.pdf output/

.PHONY: once
once:
	pdflatex -output-directory=output -jobname=paper -quiet main.tex
	cp output/paper.pdf ./paper.pdf

.PHONY: rebuild
rebuild: clean all

.PHONY: windows
windows:
	-rd /s /q output
	pdflatex -output-directory=output -jobname=paper -quiet main.tex
	mkdir output\bib
	copy bib output\bib
	cd output && bibtex paper && cd ..
	pdflatex -output-directory=output -jobname=paper -quiet main.tex
	pdflatex -output-directory=output -jobname=paper -quiet main.tex
	copy output\paper.pdf .\paper.pdf

all: paper