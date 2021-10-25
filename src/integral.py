class Gauss:
    # metodo de gauss para resolução de integrais
    def __init__(self, equa, inter:list, tabelas, subinter):
        """recebe um objeto 'function', um intervalo, uma lista de
        DataFrames e o numero de subinter que serão utilizados"""
        self.equa = equa
        self.inter = inter
        self.tabela = tabelas[subinter-1] # utiliza o numero de subintervalos para escolher o DataFrame certo
        self.nova_eq = None
        self.erro = 0
    
    def determinar_nova_equa(self):
        """gera uma função que sera utilizada com diversas constantes de acordo com o
        metodo de gauss"""
        novo_x0 = (self.inter[1]-self.inter[0])/2
        novo_x1 = (self.inter[1]+self.inter[0])/2
        novo_dxdt = (self.inter[1]-self.inter[0])/2
        self.nova_eq = lambda t: self.equa(novo_x0*t + novo_x1)*novo_dxdt
    
    def somatorio(self):
        """utiliza a função gerada e as constantes do DataFrame armazenado para gerar
        uma serie de resultados, os quais são somados e o resultado final é a resolução
        da integral"""
        resultado = 0
        for i in self.tabela.index:
            ti = self.tabela.loc[i]["ti"]
            ai = self.tabela.loc[i]["Ai"]
            resultado += self.nova_eq(ti)*ai
        
        self.resultado = resultado
