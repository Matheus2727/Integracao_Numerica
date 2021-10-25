import problema as pr
import importlib

def recarregar():
    """utiliza a biblioteca importlib para importar uma nova 'versao' do
    arquivo 'dados_problema' e a retorna"""
    dp_re = importlib.reload(dp)
    return dp_re

def main():
    """realiza filtragens de erro no arquivo 'dados_problema', o importa, 
    implementa um objeto 'Problema' e o retorna"""
    global dp
    try: # filtragem de erros para evitar problemas na importação dos dados
        import dados_problema as dp
        dp = recarregar()
        equa = dp.equa
        inter = dp.inter
        erro = dp.erro
    
    except: # se erros foram encontrados serão utilizados esses valores default
        equa = lambda x: 0
        inter = [0,1]
        erro = 1
        
    for i in inter: # filtra erros em relação ao tamanho e o conteudo do intervalo
        if type(i) != int and type(i) != float or len(inter) != 2:
            inter = [0,1]

    problema = pr.Problema(equa, inter, erro)
    try: # filtragem de erros para evitar porblemas com a função utilizade
        problema.resolver(1)

    except: # se erros foram encontrados utiliza um objeto 'Problema' default
        problema = pr.Problema(lambda x: 0, inter, erro)

    return problema
