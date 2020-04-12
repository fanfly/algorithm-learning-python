all: w06

w06: slide handout

slide: w06-slide.tex
	pdflatex $^ && pdflatex $^

handout: w06-handout.tex w06-slide.tex
	pdflatex $< && pdflatex $<

clean:
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.pdf
