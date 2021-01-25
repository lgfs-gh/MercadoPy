from utils.helper import formata_moeda
from stringcolor import *


class Produto:
    contador_codigo: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador_codigo
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador_codigo += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    def __str__(self: object) -> str:
        return bold(f'Código: ') + f'{self.codigo}\n' \
               + bold(f'Nome: ') + f'{self.nome}\n' \
               + bold(f'Preço: ') + f'{formata_moeda(self.preco)}\n'
