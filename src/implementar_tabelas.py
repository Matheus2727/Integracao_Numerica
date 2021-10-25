import tabelas

def main(subinter_max:int, arqs):
    """implementa a classe 'Tabela', recebendo um inteiro como sendo
    o numero maximo de subintervalos para o matodo de gauss para
    integração e um objeto 'Arquivos' e retorna uma lista de DataFrames"""
    textos = arqs.ler_arq("dados_gauss.txt") # recebe a tabela
    tab = tabelas.Tabela(textos)
    tab.setar_parametros(subinter_max)
    tab.setar_tabelas() # gera uma lista de DataFrames referentes a tabela
    return tab.tabelas
