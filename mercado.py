from typing import List, Dict
from models.produto import Produto
from time import sleep
from utils.helper import formata_moeda
from stringcolor import *

# ============================================ EXERCÍCIO SISTEMA DE MERCADO ============================================

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('======================================================================\n'
          '================= ' + cs('SISTEMA DE MERCADO SIMPLES', 'green') + ' =========================\n'
          '======================================================================')
    print('\nDIGITE o número indicado para selecionar uma das opções abaixo:\n'
          '1) Cadastrar produto\n'
          '2) Listar produto\n'
          '3) Comprar produto\n'
          '4) Vizualizar carrinho\n'
          '5) Fechar pedido\n'
          '6) Sair\n')

    opcao = int(input('>>> DIGITE: '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualiar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Sistema fechado...')
        sleep(2)
        exit(0)
    else:
        print(cs('>>> OPÇÃO INVÁLIDA, TENTE NOVAMENTE <<<', 'red'))
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('\n---------------------\n' +
          cs('--Cadastro de Produto--', 'yellow') +
          '\n-----------------------\n')

    nome: str = input('>>> Informe o nome do produto: ')
    preco: float = float(input('>>> Informe o preço do produto '))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O {produto.nome} foi cadastrado com sucesso!')
    sleep(1)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print(cs('-------- Listagem de produtos --------', 'yellow'))
        for produto in produtos:
            print(produto)
            sleep(1)
    else:
        print(cs('>>> Ainda não existem produtos cadastrados! <<<', 'red'))
        sleep(1)
        menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: \n' +
              cs('-------------------- PRODUTOS DISPONIVEIS ----------------------', 'yellow'))
        for produto in produtos:
            print(produto)
            print('------------------------------------------------------------')
            sleep(1)
        codigo: int = int(input('>>> DIGITE O CÓDIGO: '))
        produto: Produto = produto_por_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(1)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(1)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(1)
                menu()
        else:
            print(cs(f'O produto com código ({codigo}) não foi encontrado!', 'red'))
            sleep(1)
            menu()
    else:
        print(cs('>>> Ainda não existem produtos à venda <<<', 'red'))
        sleep(1)
        menu()


def visualiar_carrinho() -> None:
    if len(carrinho) > 0:
        print(cs('------------ Produtos no carrinho --------------', 'yellow'))
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}\n'
                      f'---------------------------------------')
                sleep(1)
                menu()
    else:
        print(cs('>>> Ainda não existem produtos no carrinho! <<<', 'red'))
        sleep(1)
        menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print(cs('---------- Produtos do carrinho ----------', 'yellow'))
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quandidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('-------------------------')
                sleep(1)
        print(f'Sua fatura é: {formata_moeda(valor_total)}')
        carrinho.clear()
        sleep(2)

    else:
        print(cs('>>> Carrinho está vazio <<<', 'red'))
        sleep(1)
        menu()


def produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
