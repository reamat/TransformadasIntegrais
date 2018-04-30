#Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite http://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

########################################
#
# ATENÇÃO
#
# POR SEGURANÇA, NÃO EDITE ESTE ARQUIVO.
#
########################################


pdf: main.tex
	cp config-pdf.knd config.knd
	latex 	main
	bibtex 	main
#	makeindex main
	latex 	main
	latex 	main
	dvips 	main.dvi
	ps2pdf	main.ps


ps: main.tex
	cp config-pdf.knd config.knd
	latex 	main
	bibtex 	main
#	makeindex main
	latex 	main
	latex 	main
	dvips 	main.dvi

dvi: main.tex
	cp config-pdf.knd config.knd
	latex 	main
	bibtex 	main
#	makeindex main
	latex 	main
	latex 	main

html: main.html

main.html: main.tex
	cp config-html.knd config.knd
	rm -f html/*
	mkdir -p html
	latex main
	latex main
	latex main
	htlatex main.tex "myconfig.cfg,3,notoc*" " -cunihtf" "-d./html/"
#	mk4ht htlatex main "myconfig,3,notoc*" "-cunihtf" "-d./html/"
#	htlatex main 'xhtml,mathml,charset=utf-8' ' -cunihtf'
	cp config-pdf.knd config.knd


clean: 
	rm -rf */*/*.aux */*/*.log */*/*.out */*/*.toc */*/*.bbl */*/*.idx */*/*.ilg */*/*.ind */*/*.blg */*/*.backup 
	rm -rf */*.aux */*.log */*.out */*.toc */*.bbl */*.idx */*.ilg */*.ind */*.blg */*.backup 
	rm -f *.aux *.log *.out *.toc *.bbl *.idx *.ilg *.ind *.blg *.backup *.html *.4ct *.4tc *.lg *.tmp *.xref

