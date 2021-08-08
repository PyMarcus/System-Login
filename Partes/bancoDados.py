#!/bin/python3.9
import pymysql

# login , tabela, user, password, quando

def dataBase():
        """Inicia conexão com o banco de dados oferecendo um cursor"""
        with open('./.pwBD.txt', 'r') as f:
            senha = f.readlines()[0]  # lê arquivo de senha para acessar o banco de dados
        conexao = pymysql.connect(host='localhost', user='root', database='login')
        cursor = conexao.cursor()
        cursor.execute('SELECT database();')  # seleciona o banco de dados pré-definido 
        return cursor
