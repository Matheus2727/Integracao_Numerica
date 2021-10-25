from math import cos

class Equa:
    # armazena um objeto 'function' e ums lista de pontos obtidos pelos calculos abaixo
    def __init__(self, equa, y0):
        self.equa = equa
        self.ys = [y0]

class Runge_Kutta:
    # resolve uma EDO especifica pelo metodo de Runge-Kutta
    def __init__(self, constantes:dict, inter:list, y0:float, dy0:float, h:float):
        """recebe constantes referentes a uma EDO cuja forma ja esta especificada.
        as constantes são 'epsilon', 'alfa', 'gama', 'omega' e 'f' e a equação é a 
        equação de Duffing. alem disso recebe um intervalo [n,m], um y(n) e um y'(n),
        alem de um passo h"""
        self.epsilon = constantes["epsilon"]
        self.alfa = constantes["alfa"]
        self.gama = constantes["gama"]
        self.omega = constantes["omega"]
        self.f = constantes["f"]
        eq0 = lambda *args: args[0] # a derivada de primeira ordem é atribuida a uma outra equação de (x, y)
        eq1 = lambda *args: -2*self.epsilon*args[0] - self.alfa*args[2] - self.gama*args[2]**3 + self.f*cos(self.omega*args[1])
        # a derivada de segunda ordem é isolada, a equação resltante é armazenada como uma função de (eq0, x e y)
        equa0 = Equa(eq0, y0)
        equa1 = Equa(eq1, dy0)
        self.equas = [equa0, equa1]
        self.inter = inter
        self.h = h
    
    def etapa(self, i):
        """cada etapa do metodo chama essa função pra um ponto no intervalo.
        esse ponto é (inicio do intervalo) + (passo)*(i)"""
        x_atu = self.inter[0]+self.h*(i) # o ponto atual no intervalo
        y_atu0 = self.equas[0].ys[i] # a imagem desse ponto na função 0 (referente a derivada de primeira ordem)
        y_atu1 = self.equas[1].ys[i] # a imagem desse ponto na função 1 (referente a derivada de segunda ordem)
        x_prox = self.inter[0]+self.h*(i+1) # o proximo ponto no intervalo, sobre o qual seram descobertas as proximas imagens
        equa0 = self.equas[0]
        equa1 = self.equas[1]

        # metodo pra equação 0: aqui é descoberta a imagem da função 0 no proximo ponto
        ylin_prox0 = y_atu1 + self.h*equa1.equa(y_atu1, x_atu, y_atu0)
        y_prox0 = y_atu0 + self.h*(y_atu1 + ylin_prox0)/2
        equa0.ys.append(y_prox0)
        
        # metodo pra equação 1: aqui é usado o resultado do calculo anterior pra descobrir a imagem da função 1 no proximo ponto
        ylin_prox1 = y_atu0 + self.h*y_atu1
        y_prox1 = y_atu1 + self.h*(equa1.equa(y_atu1, x_atu, y_atu0)+equa1.equa(ylin_prox0, x_prox, ylin_prox1))/2
        equa1.ys.append(y_prox1)
    
    def resolver(self):
        """chama a 'etapa' pra todos os pontos dentro do intervalo levando em consideração o passo"""
        for i in range(round(((self.inter[1]-self.inter[0])/self.h))):
            self.etapa(i)
    
    def formatar(self):
        """formata a lista de resultados para ser printada na interface"""
        linhas = []
        for i, _ in enumerate(self.equas[0].ys):
            t = round(self.inter[0] + self.h*i, 3)
            y0 = round(self.equas[0].ys[i], 4)
            y1 = round(self.equas[1].ys[i], 4)
            linhas.append("y({0}) = {1} e y'({0}) = {2}".format(t, y0, y1))

        return linhas
