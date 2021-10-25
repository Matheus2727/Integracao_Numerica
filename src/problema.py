class Problema:
    # metodos e dados do problema que terão algum grau de interação com o usuario
    def __init__(self, equa, inter, erro):
        """recebe um objeto 'function', um intervalo e o erro requerido no problema"""
        self.equa = equa
        self.inter = inter
        self.erro = erro
    
    def resolver(self, x):
        return self.equa(x)
