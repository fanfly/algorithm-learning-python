all: w05

w05: slide handout

slide: w05-slide.tex
	pdflatex w05-slide && pdflatex w05-slide

handout: w05-slide.tex
	pdflatex w05-handout && pdflatex w05-handout

clean:
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.pdf
