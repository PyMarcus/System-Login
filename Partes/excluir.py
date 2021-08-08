#!/bin/python3.9
from bancoDados import dataBase
from mail import Mail


class DelUser:
    """ exclui do banco o usuário"""
    def __init__(self, usuario, senha, email='marcus-v@outlook.com'):
        self.usuario = usuario
        self.senha = senha
        self.email = email

    def delete(self):
        bd = dataBase()
        if bd.execute(f"SELECT * FROM tabela WHERE user = '{self.usuario}' and password = '{self.senha}';"):
            bd.execute(f"DELETE FROM tabela WHERE user = '{self.usuario}';")
            bd.connection.commit()
            print('A sua conta foi excluída!')
            email = Mail(f"Sua conta foi deletada, {self.usuario}")
            email.sendMail()
        else:
            print("CREDENCIAIS INCORRETAS.")
