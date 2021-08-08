#!/bin/python3.9
from mail import Mail
from colorama import Fore
from datetime import date, datetime
from cadastro import Cadastro
from bancoDados import dataBase
from criptografaBD import criptografa
import getpass
import sys
from excluir import DelUser
from login import ExibePainel, Login



if __name__ == '__main__':
    exibir_login = ExibePainel()
    escolhido = exibir_login.exibicao()
    if escolhido == '1':
        # para o usuário já cadastrado, faz login
        try:
            user = str(input('Usuário: '))
            pw = getpass.getpass('Senha: ')
        except ValueError or TypeError:
            print('Algo deu errado...')
        else:
            acesso = Login(user, pw)
            acesso.login()
    elif escolhido == '2':
        # faz o cadastro do usuário
        try:
            ok = True
            contador = 0
            user = str(input("Por favor, escolha um Usuário para cadastrar: "))
            mail = str(input("Por favor, informe-nos um e-mail: "))
            while ok:
                pw = getpass.getpass('Crie uma senha: ')
                pw2 = getpass.getpass('Reinsira a senha: ')
                if pw == pw2:
                    ok = False
                else:
                    print('As senhas não são iguais!')
                contador += 1
                if contador == 3:  # a pessoa tem 3 chances para refazer a senha
                    print("Número de tentativas excedido, por favor, repita toda a operação!")
                    ok = False
                    sys.exit(1)
        except ValueError:
            pass
        else:
            cadastro = Cadastro(user, pw2, email=mail)
            cadastro.cadastrar()
    elif escolhido == '3':
        # exclui a conta
        try:
            user = str(input("Digite o nome da sua conta: "))
            senha = getpass.getpass("Digite a senha, por favor: ")
            maiil = str(input("Informe seu e-mail: "))
        except ValueError:
            pass
        else:
            questao = str(input("Você tem certeza? (s/S/N/n) "))
            if questao == 'S' or questao == 's':
                delete = DelUser(user, senha, email=maiil)
                delete.delete()
            elif questao == 'N' or questao == 'n':
                print("Cancelado")
            else:
                print("Por favor, Dê uma resposta válida")
                print("Nada foi alterado")
                print()
