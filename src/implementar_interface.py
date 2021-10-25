import interface
import atualizar
import main as mn

def format_resul_inte(lista_intes):
    """formata os resultados das integrais e os retorna para serem printados
    na interface"""
    novo_conteudo = ""
    for i, inte in enumerate(lista_intes):
        p = "pontos"
        novo_conteudo += str(i+2) + " " + p + ": " + str(round(inte.resultado, 6)) + "   erro: " +  str(round(inte.erro, 6)) + "\n"
    
    return novo_conteudo

def format_resul_edo(lista_linhas):
    """formata os resultados das edos e os retorna para serem printados
    na interface"""
    novo_conteudo0 = ""
    novo_conteudo1 = ""
    tamanho = len(lista_linhas)
    for i in range(tamanho//2):
        linha0 = lista_linhas[i]
        linha1 = lista_linhas[i + tamanho//2]
        novo_conteudo0 += linha0 + "\n"
        novo_conteudo1 += linha1 + "\n"
    
    if novo_conteudo1[-1] != lista_linhas[-1]:
        novo_conteudo1 += lista_linhas[-1] + "\n"
    
    return novo_conteudo0, novo_conteudo1

def gerar_ajuda(**kwargs):
    """retorna o texto de ajuda"""
    conteudo_ajuda = ""
    conteudo_ajuda += "O programa pode receber uma função no formato da função default\n"
    conteudo_ajuda += "'1/(x+1)' e um intervalo no formato default '0,2' possibilitando\n"
    conteudo_ajuda += "integrar essa função nesse intervalo pelo metodo de gauss com um\n"
    conteudo_ajuda += "numero de subintervalos (descritos pelo numero de pontos) o qual\n"
    conteudo_ajuda += "aumenta ate atingir 6 casas decimais corretas. Tal funcionalidade\n"
    conteudo_ajuda += "esta no botão 'integrar', o botão 'grafico' plota a curva no\n"
    conteudo_ajuda += "intervalo e o botão 'atualizar' recebe uma nova função e intervalo\n"
    conteudo_ajuda += "escrita nos inputs de texto (o programa não suporta 'sen', 'cos',\n"
    conteudo_ajuda += "etc. Tambem gera erros se houver uma singularidade na função\n"
    conteudo_ajuda += "dentro do intervalo e se a função ou intervalo não estiverem\n"
    conteudo_ajuda += "corretos). A parte do programa referente a EDO está em resolver a\n"
    conteudo_ajuda += "equação dada pra pontos dentro do intervalo dado com um passo de\n"
    conteudo_ajuda += "0.05 ao usar o botão 'resolver'."
    return conteudo_ajuda

def atualizar_conteudo(novo_conteudo, janela, ident):
    """atualiza o conteudo do bloco de texto cujo nome esta armazenado em 'ident'
    e cuja janela esta em 'janela', alterando seu texto para a string em 
    'novo_conteudo'"""
    if novo_conteudo is None:
        novo_conteudo = ""
    
    for texto in janela.textos:
        if texto.nome == ident:
            texto.conteudo = novo_conteudo

def aplicar_atu(arqs, tabelas, subinter_max, **kwargs):
    """implementa o arquivo 'atualizar' para receber novos valores para o problema
    e implementa denovo linhas importantes do arquivo 'main' para processar esses
    novos valores. recebe uma lista de 'DataFrames', o numero maximo de subintervalos
    para o metodo de gauss de integração e um dicionario com um objeto 'Janela' na
    chave 'janela'"""
    func = None
    inter = None
    for input in kwargs["janela"].inputs:
        if input.nome == "func":
            func = input.input
        
        elif input.nome == "inter":
            inter = input.input
    
    atualizar.main(arqs, func, inter)
    mn.atualizar(kwargs["janela"], subinter_max, arqs, tabelas)


def setartextos(janela: interface.Janela):
    """implementa as caixas de texto e as coloca em um objeto 'Janela'"""
    text_titu_inte = interface.Texto(10, 10, 30, "Integral:", "titu_inte")
    text_titu_edo = interface.Texto(420, 10, 30, "Edo:", "titu_edo")
    text_func = interface.Texto(10, 50, 30, "Função:", "func")
    text_inter = interface.Texto(10, 90, 30, "Intervalo:", "inter")
    text_equa = interface.Texto(420, 50, 30, "Equação:", "equa")
    text_equa_edo = interface.Texto(420, 90, 30, "y''(t)+2*0*y'(t)+0.1*y+1*y**3=12*cos(1*t)", "equa_edo")
    text_inter_edo = interface.Texto(420, 130, 30, "Intervalo:", "inter_edo")
    text_inter_edo_val = interface.Texto(570, 130, 30, "0 , 1", "inter_edo_val")
    text_var = interface.Texto(10, 240, 27, "", "var")
    text_var2 = interface.Texto(500, 240, 27, "", "var2")
    janela.addTextos([text_titu_inte, text_titu_edo, text_func, text_inter, text_equa_edo, text_equa, text_inter_edo, text_inter_edo_val, text_var, text_var2])


def setarinputs(janela: interface.Janela):
    """implementa os inputs de texto e os coloca em um objeto 'Janela'"""
    inpu_func = interface.Inp(170, 50, 9, 30, "1/(x+1)", "func")
    inpu_inter = interface.Inp(170, 90, 6, 30, "0,2", "inter")
    janela.addInputs([inpu_func, inpu_inter])


def setarbots(janela: interface.Janela, funcs):
    """implementa os botões e os coloca em um objeto 'Janela'"""
    janela.botoes = []
    bot_inte = interface.Botao(10, 130, 0, 0, "integrar", "inte", 30,
                           [120, 120, 120], lambda: (atualizar_conteudo(format_resul_inte(funcs["inte"]()), janela, "var"), atualizar_conteudo("", janela, "var2")))
    bot_graf = interface.Botao(150, 130, 0, 0, "grafico", "graf", 30,
                           [120, 120, 120], funcs["graf"])
    bot_atu = interface.Botao(10, 180, 0, 0, "atualizar", "atu", 30,
                           [120, 120, 120], funcs["atu"], {"janela":janela})
    bot_resol = interface.Botao(420, 180, 0, 0, "resolver", "resol", 30,
                           [120, 120, 120], lambda: (atualizar_conteudo(format_resul_edo(funcs["edo"]())[0], janela, "var"), atualizar_conteudo(format_resul_edo(funcs["edo"]())[1], janela, "var2")))
    bot_help = interface.Botao(880, 10, 0, 0, "ajuda", "help", 30,
                           [120, 120, 120], lambda **kwargs: (atualizar_conteudo(gerar_ajuda(), janela, "var"), atualizar_conteudo("", janela, "var2")))
    janela.addBotões([bot_inte, bot_graf, bot_atu, bot_resol, bot_help])

def main(funcs):
    """implementa um objeto 'Janela', o utiliza nas outras funções desse arquivo,
    inicia a janela e a retorna. recebe um dicionario de funções a serem utilizadas
    pelos botões"""
    janela = interface.Janela(1000, 700, "menu")
    setartextos(janela)
    setarinputs(janela)
    setarbots(janela, funcs)
    janela.iniciar()
    return janela
