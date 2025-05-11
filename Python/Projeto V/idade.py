from datetime import datetime

def idade_u(atual, ano):
    s = atual.year - ano.year - ((atual.month, atual.day) < (ano.month, ano.day))
    return s

if __name__ == '__main__':
    n = datetime.now()
    i = int(input("Digite seu ano de nascimento:"))
    data_nascimento = datetime(i, 1, 1)
    v_retorno = idade_u(n, data_nascimento)
    print(f"Você tem {v_retorno} anos")