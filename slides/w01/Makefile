all: w01

w01: slide handout

slide: w01.tex
	pdflatex -jobname=w01-slide w01.tex

handout: w01.tex
	pdflatex -jobname=w01-handout \
		"\PassOptionsToClass{handout}{beamer} \input{w01.tex}"

clean:
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.pdf