TXT=$(wildcard *.txt)
PDF12=$(patsubst %.txt, %.1.2.pdf, $(TXT))
PDF13=$(patsubst %.txt, %.1.3.pdf, $(TXT))
PDF14=$(patsubst %.txt, %.1.4.pdf, $(TXT))



all: $(PDF12) $(PDF13) $(PDF14)


%.ps: %.txt
	enscript -p $@ $<

%.pdf: %.ps
	ps2pdf $< $@

%.1.2.pdf: %.pdf
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.2 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$@ $<
%.1.3.pdf: %.pdf
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.3 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$@ $<
%.1.4.pdf: %.pdf
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$@ $<

clean:
	$(RM) $(PDF12) $(PDF13) $(PDF14)
