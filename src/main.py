import implementar_problema as ip
import implementar_grafico as ig
import implementar_tabelas as it
import implementar_integral as ii
import implementar_interface as iint
import implementar_edo as ie
import arquivos
# importa os implementadores para serem chamados

def atualizar(janela, subinter_max, arqs, tabelas):
    """chama funçoes importantes do main quando os dados principais do programa forem
    modificados e todas as informaçoes referentes a eles precisarem ser atualizadas.
    recebe um objeto 'Janela', o numero maximo de subintervalos para o metodo de gauss,
    um objeto 'Arquivos' e uma lista de DataFrames"""
    func_base = ip.main()
    grafico = ig.main(func_base.equa, func_base.inter)
    lista_inte = ii.main(func_base.equa, func_base.inter, tabelas, subinter_max, func_base.erro)
    edo = ie.main()
    funcs = {}
    funcs["inte"] = lambda **kwargs: lista_inte
    funcs["edo"] = lambda **kwargs: edo.formatar()
    funcs["graf"] = lambda **kwargs: grafico.plotar()
    funcs["atu"] = lambda **kwargs: iint.aplicar_atu(arqs, tabelas, subinter_max, **kwargs)
    iint.setarbots(janela, funcs)

def main(subinter_max):
    """função principal do programa, inicia a janela e implementa todas as classes
    principais utilizando os valores default do problema. recebe o numero maximo
    de subintervalos a serem utilizados no metodo de integração de gauss"""
    arqs = arquivos.Arquivos()
    tabelas = it.main(subinter_max, arqs)
    func_base = ip.main()
    grafico = ig.main(func_base.equa, func_base.inter)
    lista_inte = ii.main(func_base.equa, func_base.inter, tabelas, subinter_max, func_base.erro)
    edo = ie.main()
    funcs = {}
    funcs["inte"] = lambda **kwargs: lista_inte
    funcs["edo"] = lambda **kwargs: edo.formatar()
    funcs["graf"] = lambda **kwargs: grafico.plotar()
    funcs["atu"] = lambda **kwargs: iint.aplicar_atu(arqs, tabelas, subinter_max, **kwargs)
    janela = iint.main(funcs)
    iint.aplicar_atu(arqs, tabelas, subinter_max, **{"janela": janela})
    janela.main_loop()

if __name__ == "__main__":
    main(7)
