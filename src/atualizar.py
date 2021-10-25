def main(arqs, equa:str="1/(x+1)", inter:str="0,2"):
    """refaz o arquivo 'dados_problema.py' para trabalhar com uma função e um intervalo novos,
    recebe um objeto 'Arquivos', uma equação e um intervalo"""
    nome = "dados_problema.py"
    texto = ""
    texto += "equa=lambda x:" + equa + "\n"
    texto += "inter=[" + inter + "]\n"
    texto += "erro=0.000001\n"
    arqs.refazer_arq(nome, texto)
    