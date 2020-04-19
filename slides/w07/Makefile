all: w07

w07: slide handout

slide: w07-slide.tex
	pdflatex $^ && pdflatex $^

handout: w07-handout.tex w07-slide.tex
	pdflatex $< && pdflatex $<

clean:
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.pdf
