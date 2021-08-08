from cryptography.fernet import Fernet


chave = Fernet.generate_key()
cifra = Fernet(chave)


def criptografa(senha):
    """Criptografa a senha"""
    global chave
    global cifra

    pw = senha
    # gera chave aleatória
    texto = cifra.encrypt(f"{pw}".encode())  # criptografa sha256
    return texto
    
def descriptografa(senha):
    """Descriptografa a senha"""
    global chave
    global cifra

    funcao = criptografa(senha)
    texto_normal = cifra.decrypt(funcao) # descriptografa
    return texto_normal.decode()
