#!/bin/python3.9
from mail import Mail
from bancoDados import dataBase
from criptografaBD import criptografa


class Cadastro:
    def __init__(self, usuario, senha, email):
        """Faz o cadastro do usuário conforme as credenciais solicitadas"""
        self.usuario = usuario
        self.senha = senha
        self.email = email

    def cadastrar(self):
        bd = dataBase()
        # insere os dados no banco de dados:
        if bd.execute(f"SELECT * FROM tabela WHERE user = '{self.usuario}';"):
            print("Usuário já cadastrado\nPor favor, use outro nome")
        else:
            bd.execute(f"INSERT INTO tabela (user, password) VALUES ('{self.usuario}', '{self.senha}');")
            bd.connection.commit()
            print('Cadastro efetuado')
            # envia o e-mail:
            email = Mail(f"Obrigado por cadastra-se em nosso sistema!\nSeu usuário de acesso: {self.usuario}", self.email)
            email.sendMail()
