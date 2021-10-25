import edo

def main():
    """implementa a classe 'Edo', setando as constantes da equação de Duffing
    e retorna um objeto 'Edo' resolvido"""
    equa_dif = edo.Runge_Kutta({"epsilon":0, "alfa":0.1, "gama":1, "omega":1, "f":12}, [0, 1], 0, 4, 0.05)
    equa_dif.resolver()
    return equa_dif
