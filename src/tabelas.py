import pandas as pd

class Tabela:
    # prepara e formata uma tabela inicial para ser usada pelas integrais
    def __init__(self, textos):
        """recebe uma lista de strings representando uma tabela"""
        self.textos = textos
        self.dados = ""
        self.tabelas = []
    
    def formatar_dict(self, param, chaves, dados):
        """recebe um dicionario 'param', uma lista chaves e dados. atribui os dados a
        esse dicionario nessas chaves e retorna o dicionario"""
        for i, chave in enumerate(chaves):
            param[chave].append(float(dados[i]))
        
        return param
    
    def setar_parametros(self, subinter_max):
        """cria um dicionario geral o qual sera populado com outros dicionarios.
        cada um desses outros dicionarios sera atrelado a um numero de subintervalos
        do metodo de gauss para integração."""
        self.parametros_gerais = {}
        for sub in range(1, subinter_max + 1): # faz esse loop para cada numero de subintervalo ate o maximo
            param = {}
            for i, linha in enumerate(self.textos):
                if i == 0: # recebe os dados na primeira linha como as 'keys' do dicionario
                    chaves = linha[:-1].split("\t")
                    for chave in chaves:
                        param[chave] = []
                
                else: # nas outras linhas adiciona os dados as chaves respectivas se o numero de subintervalo da tabela for igual ao numero de subintervalos referido no loop
                    dados = linha[:-1].split("\t")
                    if int(dados[0]) == sub:
                        param = self.formatar_dict(param, chaves, dados)
            
            self.parametros_gerais[sub] = param
    
    def setar_tabelas(self):
        """transforma cada dicionario dentro do dicionario 'parametros_gerais' armazenado
        em um DataFrame"""
        for subs in self.parametros_gerais.keys():
            self.tabelas.append(pd.DataFrame(self.parametros_gerais[subs]))
