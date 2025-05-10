def idade_u (atual,ano):
    s = atual - ano
    return s
if __name__ == '__main__':
    n = int(input("Digite o ano atual:"))
    i  = int(input("Digite seu ano de nascimento:"))
    v_retorno  = idade_u(n,i)
    print(f"Você tem {v_retorno} anos")