import sys
import os

def casa_brackets(text, sub=b"{"):
    if sub not in text or b"}" not in text :
        return -1, -1
    pos_ini = text.find(sub) + len(sub) - 1
    pos = pos_ini+1
    count = 1
    while count > 0 and pos < len(text):
        # print(pos, text[pos], count)
        if text[pos] in b'{':
            count += 1
        elif text[pos] in b'}':
            count -= 1
        pos += 1
    return pos_ini, pos


def extrai_exercicios(arq, exer, exeresol, converte):
    texto = b""

    blocos = ([rb"exer", rb"resp"] if exer else [])\
           + ([rb"exeresol", rb"resol"] if exeresol else [])
    aberturas = [rb"\begin{" + l + rb"}" for l in blocos]
    fechamentos = [rb"\end{" + l + rb"}" for l in blocos]
    tags = [rb"\chapter{", rb"\section{"] #  , rb"\subsection{"]
    contagem = 0
    dentro_de_bloco = False
    with open(arq, 'rb') as f: 
        for linha in f.readlines():
            if converte:
                linha = linha.replace(rb"{exeresol}", rb"{exer}").replace(rb"{resol}", rb"{resp}")
            if any([s in linha for s in tags]):
                texto += linha

            if any([s in linha for s in aberturas]):
                dentro_de_bloco = True
                contagem = contagem + 1

            if dentro_de_bloco:
                # if rb"ref{" in linha:
                #   print(linha)
                if linha.strip() != b'':
                    texto += linha 

            if any([s in linha for s in fechamentos]):
                dentro_de_bloco = False

    return contagem, limpa_secoes_vazias(texto.decode()) if contagem>0 else ""


def abre_arquivos(exer, exeresol, converte):
    texto = ""
    with open("main.tex", "rb") as f:
        for linha in f.readlines():
            if linha.strip()[0:9] == rb"\include{":
                # print(linha)
                s, e = casa_brackets(linha)
                arq = linha[s+1 : e-1].decode() + ".tex"
                print(r"%Extraindo de " + arq)
                texto = texto + r"%%%% Extraído de " + arq + "\n"
                contagem, conteudo = extrai_exercicios(arq,
                     exer, exeresol, converte)
                texto = texto + conteudo
                # print(texto)
    return texto

def limpa_secoes_vazias(texto):
    tag = r"\section"
    tags = [tag, r"\chapter", r"%%%% Extraído de"]
    linhas = texto.splitlines() + [""]
    
    texto = ""
    for i, linha in enumerate(linhas):
        if (tag in linha and all(t not in linhas[i+1] for t in tags) and linhas[i+1] != "") or tag not in linha:
            texto += linha+"\n"
        elif tag in linha:
            texto += r"\stepcounter{section}"
            print("Seção vazia")

    return texto.strip()
        

cabecalho = r"""\documentclass[12pt]{book}
\input preambulo.tex
\setlength{\headheight}{30pt}
\usepackage{xr}
\externaldocument{main}
\begin{document}"""

receitas = [("exercicios_resolvidos.tex", (False, True,  False)),
            ("exercicios.tex",            (True,  False, False)),
            ("exercicios_todos.tex",      (True,  True,  False))]

for arq, receita in receitas:
    if receita[0] or receita[2]:
        rodape = r"\include{respostas}" + '\n' + r"\end{document}"
    else:
        rodape = r"\end{document}"

    texto = cabecalho + abre_arquivos(*receita) + rodape
    with open(arq, "w") as f:
        f.write(texto)

# print(texto)
