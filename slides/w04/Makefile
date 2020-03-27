all: w04

w04: slide handout

slide: w04-slide.tex
	pdflatex w04-slide && pdflatex w04-slide

handout: w04-slide.tex
	pdflatex w04-handout && pdflatex w04-handout

clean:
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.pdf
