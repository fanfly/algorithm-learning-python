all: w08

w08: slide handout

slide: w08-slide.tex
	pdflatex $^ && pdflatex $^

handout: w08-handout.tex w08-slide.tex
	pdflatex $< && pdflatex $<

clean:
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.pdf
