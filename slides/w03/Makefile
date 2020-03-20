all: w03

w03: slide handout

slide: w03.tex
	pdflatex w03-slide && pdflatex w03-slide

handout: w03.tex
	pdflatex w03-handout && pdflatex w03-handout

clean:
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.pdf