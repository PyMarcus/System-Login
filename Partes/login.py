#!/bin/python3.9
from mail import Mail
from colorama import Fore
from datetime import datetime
from bancoDados import dataBase
import platform


class Login:
    """Classe pricipal, exibe opções e faz testes"""
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
    def login(self):
        """Se for igual a 1, checa se os dados estão no banco de dados"""
        c = dataBase()
        if c.execute(f"SELECT * FROM tabela WHERE user = '{self.usuario}' and password = '{self.senha}';"):
            print(Fore.GREEN + "Bem vindo!\n") #
            # envio de e-mail
            msg = f"Um login no SO {platform.system()} foi efetuado em {datetime.now()}"
            email = Mail(msg)
            email.sendMail()
        else:
            print(Fore.RED + "Usuário não cadastrado ou login incorreto.\nPor favor, tente novamente.")
    
class ExibePainel:
    """Exibe a tela inicial para interação com o usuário"""
    def exibicao(self):
        print()
        print(Fore.LIGHTBLUE_EX + "-" * 40)
        print(" " * 15 ,"Bem vindo!")
        print("Por favor, escolha uma das opções abaixo:")
        print()
        print("-" * 40)
        print(Fore.LIGHTYELLOW_EX + "+"," " * 5,"1 - Para acessar" ," " * 13, "+")
        print(Fore.LIGHTCYAN_EX + "+"," " * 4," 2 - Para cadastrar usuário" ," " * 3, "+")
        print(Fore.LIGHTRED_EX + "+"," " * 5,"3 - Para excluir a conta" ," " * 5, "+")
        print("-" * 40)
        print(Fore.LIGHTGREEN_EX + """                 ┈┈┈╲┈┈┈┈╱
                ┈┈┈╱     ▔▔╲
                ┈┈┃┈▇┈┈▇┈┃
                ╭╮┣━━━━━━┫╭╮
                ┃┃┃┈┈┈┈┈┈┃┃┃
                ╰╯┃┈┈┈┈┈┈┃╰╯
                ┈┈╰┓┏━━┓┏╯
                ┈┈┈╰╯┈┈╰╯
                           """)
        print(Fore.LIGHTBLACK_EX + "-" * 40)
        print()
        try:
            opcao = str(input(Fore.GREEN + ">>> "))
            print()
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            if opcao == '1' or opcao == '2' or opcao == '3':
                return opcao
            else:
                print("Opção inválida")
