import integral

def loop(equa, inter, tabela, subinter_max:int, erro_prob):
    """um loop de integrais. o metodo de gauss é chamado varias vezes, cada
    vez com um numero de subintevalos maior, ate que o erro fique abaixo do erro
    requerido pelo problema. recebe um objeto 'function', um intervalo, 
    uma lista de DataFrames, o maior numero de subintervalos e o erro requerido
    e retorna uma lista de objetos 'Integral'"""
    integrais = []
    erro = 100
    i = 0
    while erro > erro_prob: # repetir ate o erro ser menor que o requerido
        if i == subinter_max: # sair do loop se o numero maximo de subintervalos estiver para ser ultrapassado
            break

        i += 1
        integrais.append(integral.Gauss(equa, inter, tabela, i))
        integrais[i-1].determinar_nova_equa()
        integrais[i-1].somatorio()
        if i >= 2: # checar o erro se existirem integrais suficientes
            erro = abs(integrais[i-1].resultado - integrais[i-2].resultado)
            integrais[i-1].erro = erro
        
        else: # se não existirem, usar um erro arbitrariamente grande default
            erro = 0
            integrais[i-1].erro = erro
            erro = 100
    
    return integrais


def main(equa, inter, tabela, subinter_max:int, erro_prob):
    """chama o loop e retorna a lista de objetos 'Integral'. recebe
    um objeto 'function', um intervalo, uma lista de DataFrames, o
    maior numero de subintervalos e o erro requerido"""
    integrais = loop(equa, inter, tabela, subinter_max, erro_prob)
    return integrais
