all: w02

w02: slide handout

slide: w02.tex
	pdflatex w02-slide && pdflatex w02-slide

handout: w02.tex
	pdflatex w02-handout && pdflatex w02-handout

clean:
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.pdf