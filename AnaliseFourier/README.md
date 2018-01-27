# Análise de Fourier - Um Livro Colaborativo

Este é um livro colaborativo sobre análise de Fourier, conteúdo normalmente estudado em cursos de graduação das áreas exatas e da terra na disciplina de cálculo numérico.

Participe da escrita do livro. Veja como em https://www.ufrgs.br/reamat/participe.html. Qualquer dúvida, poste no nosso fórum https://www.ufrgs.br/reamat/forum.html, crie um _issue_ no repositório do livro ou escreva para reamat@ufrgs.br.

## Licença

Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite <https://creativecommons.org/licenses/by-sa/3.0/> ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

## Sobre o código fonte

O código fonte está escrito em [Latex](https://latex-project.org/) e as referências bibliográficas em [BibTex](http://www.bibtex.org/), testado em computador Linux com o pacote [TexLive](http://www.tug.org/texlive/). O texto está em formatação **utf-8**.

### Folha de estilo

Mais informações sobre a organização do código-fonte e padrões de escrita do livro, veja a folha de estilo disponível em https://github.com/reamat/Docs/blob/master/livro/FOLHA_DE_ESTILO.md.

## Compilando

### Em computador Linux

O código LaTeX está testado em computador [Linux](https://pt.wikipedia.org/wiki/Linux) com o pacote [TexLive](https://www.tug.org/texlive/) instalado. O livro pode ser compilado com:

    $ make

Isto gera o livro em formato PDF (main.pdf). Também, o código pode ser compilado em formato DVI:

    $ make dvi

Alguma vezes a compilação pode gerar erros devido a incompatibilidade com antigos arquivos temporários. Para limpar os arquivos temporários gerados durante a compilação, digite:

    $ make clean

Alternativamente, o livro pode ser compilado com os comandos usuais `latex main`, `bibtex main`, `pdflatex main`, `makeindex main`. Lembrando que `main.tex` é o arquivo LaTeX principal.

#### Formato HTML
O livro também pode ser compilado em formato HTML, digitando:

	$ make html

Este comando cria a pasta `./html` onde todo os arquivos da versão HTML do livro são colocados.

### Outros sistemas operacionais

O código LaTeX pode ser compilado em outros sistemas operacionais. Para tanto, deve-se editar o arquivo de configuração `config.knd`. Este arquivo contém instruções TeX para controlar o formato e a versão do livro. Por exemplo, para setar o formato do livro em PDF, garanta que este arquivo contenha o seguinte texto:

    \ispdftrue \ishtmlfalse

Por fim, o livro pode ser compilado com a seguinte sequência de comandos:

    latex main
    bibtex main
    latex main
    latex main
	dvips main.dvi
	ps2pdf main.ps
