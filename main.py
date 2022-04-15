def dinheiro_inicial():
    # cedulas
    c_10 = int(input("Cedulas de 10: "))
    c_5 = int(input("Cedulas de 5: "))
    c_2 = int(input("Cedulas de 2: "))
    c_1 = int(input("Cedulas de 1: "))
    # moedas
    m_50 = int(input("Moedas de 50: "))
    m_25 = int(input("Moedas de 25: "))
    m_10 = int(input("Moedas de 10: "))
    m_5 = int(input("Moedas de 5: "))
    return [c_10, c_5, c_2, c_1, m_50, m_25, m_10, m_5]

def estoque_inicial():
    q_ref = int(input("Estoque inicial de refrigerante: "))
    q_agu = int(input("Estoque inicial de agua: "))
    q_cho = int(input("Estoque inicial de chocolate: "))
    q_sal = int(input("Estoque inicial de salgadinho: "))
    return (q_ref, q_agu, q_cho, q_sal)

def preco():
    p_ref = int(input("Preco do refrigerante: "))
    p_agu = int(input("Preco da agua: "))
    p_cho = int(input("Preco do chocolate: "))
    p_sal = int(input("Preco do salgadinho: "))
    return (p_ref, p_agu, p_cho, p_sal)

def compra_valida(saldo, estoque, preco, cm):
    if estoque == 0:
        return -1
    if preco > saldo:
        return -2
    saldo - preco = troco



def processo_escolha (saldo, q, p, cm):
    cv = compra_valida(saldo, q, p, cm)
    if cv == 1:
        cm
        return (saldo - preco, q - 1, cm)
    if cv == -1:
        print("Produto indisponivel")
        return(saldo, q, cm)
    if cv == -2:
        print("Saldo insuficiente")
        return(saldo, q, cm)
    if cv == -3:
        print("Troco indisponivel")
        return(saldo, q, cm)

if __name__ == 'main':

    cm = dinheiro_inicial()
    (q_ref, q_agu, q_cho, q_sal) = estoque_inicial()
    (p_ref, p_agu, p_cho, p_sal) = preco()
    saldo = 0
    b = int(input(("Botao: "))

    while (b != 0):
        if b > 0:
            saldo = saldo + b
        elif b == -1:
            (saldo, q_ref, cm) = processo_escolha(saldo, q_ref, p_ref, cm)
        elif b == -2:
            (saldo, q_agu, cm) = processo_escolha(saldo, q_agu, p_agu, cm)
        elif b == -3:
            (saldo, q_cho, cm) = processo_escolha(saldo, q_cho, p_cho, cm)
        elif b == -4:
            (saldo, q_sal, cm) = processo_escolha(saldo, q_sal, p_sal, cm)
        elif b == -5:
            troco


        b = int(input(("Botao: "))



