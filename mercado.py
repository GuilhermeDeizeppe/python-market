import colorama
from colorama import Fore, Back, Style
from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_str_moeda


colorama.init(autoreset=True)

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:

    print(Fore.LIGHTCYAN_EX + '========================================')
    print(Fore.LIGHTCYAN_EX + '============' + Fore.LIGHTYELLOW_EX + ' MERCADINHO S/A ' +
          Fore.LIGHTCYAN_EX + '============')
    print(Fore.LIGHTCYAN_EX + '========================================')

    menu()


def menu() -> None:

    print(Fore.BLUE + '\nServiços Disponíveis: ')
    print('1 - Cadastrar produtos')
    print('2 - Listar produtos')
    print('3 - Comprar produtos')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Encerrar sessão')

    try:
        opcao: int = int(input(Fore.BLUE + '\nDigite o sistema desejado: '))
    except ValueError:
        print('\n' + Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + 'Opção inválida:' + Style.RESET_ALL +
              ' certifique-se de digitar o número do sistema corretamente.')
        sleep(3.5)
        menu()

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print(Fore.LIGHTGREEN_EX + 'Sessão encerrada. Obrigado!')
        sleep(2)  # Vai aguardar 2 segundos antes de executar o próximo código.
        exit(0)
    else:
        print('\n' + Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + 'Opção inválida:' + Style.RESET_ALL +
              ' verifique o número digitado.')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('\n' + Fore.BLUE + 'Cadastro de Produtos')

    try:
        nome: str = input('Informe o nome do produto: ')
        if len(nome) <= 0 or nome.isspace():
            print(Fore.RED + 'O nome não pode ser vazio.')
            sleep(2)
            menu()
        else:
            nome = nome.lstrip()
            nome = nome.rstrip()
            nome = nome.title()

    except ValueError:
        print(Fore.RED + 'Nome inválido.')
        sleep(2)
        menu()

    try:
        preco: float = float(input('Informe o preço do produto: '))
    except ValueError:
        print(Fore.RED + 'Valor inválido.')
        sleep(2)
        menu()

    for prod in produtos:
        if nome == prod.nome:
            if preco == prod.preco:
                print(Fore.RED + f'{nome} já está cadastrado.')
                sleep(3)
                menu()

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)
    print(Fore.LIGHTGREEN_EX + f'{produto.nome} foi cadastrado com sucesso!\n')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:

        print(Fore.BLUE + 'Produtos\n')

        for produto in produtos:
            print(produto)
            print(Fore.BLUE + '------------------')
            sleep(1)

    else:
        print('Ainda não existem produtos cadastrados.\n')

    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:

        print(Fore.BLUE + '\n--------------------------------------------------------------')
        print(Fore.BLUE + '=================== ' + Fore.LIGHTYELLOW_EX + 'PRODUTOS DISPONÍVEIS' +
              Fore.BLUE + '======================')

        for produto in produtos:
            print(produto)
            print('\n')
            sleep(1)

        try:
            codigo: int = int(input(Fore.BLUE + 'Informe o código do produto que deseja adicionar ao carrinho: '))
            produto: Produto = pega_produto_por_codigo(codigo)
        except ValueError:
            print(Fore.RED + 'Código inválido.')
            sleep(2)
            menu()

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False

                for item in carrinho:
                    quant: int = item.get(produto)

                    if quant:
                        item[produto] = quant + 1
                        print(Fore.LIGHTGREEN_EX + f'{produto.nome} agora possui {quant + 1} unidades no carrinho.\n')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()

                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(Fore.LIGHTGREEN_EX + f'{produto.nome} foi adicionado ao carrinho.\n')
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(Fore.LIGHTGREEN_EX + f'{produto.nome} adicionado ao carrinho.\n')
        else:
            print(Fore.RED + f'Não encontramos nenhum produto com o código {codigo}. Verifique se digitou corretamente.\n')
            sleep(2)
            menu()
    else:
        print('A loja está sem estoque.\n')

    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print(Fore.BLUE + '\nCarrinho\n')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print(Fore.BLUE + '---------------------')
                sleep(1)
    else:
        print('O carrinho está vazio.\n')
        sleep(2)
        menu()

    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:

        valor_total: float = 0
        print(Fore.BLUE + '\nCarrinho\n')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print(Fore.BLUE + '----------------------------')
        print(Fore.BLUE + f'Valor total do pedido = {valor_total}')
        carrinho.clear()
        sleep(2)

    else:
        print('O carrinho está vazio.\n')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto

    return p


if __name__ == '__main__':
    main()
