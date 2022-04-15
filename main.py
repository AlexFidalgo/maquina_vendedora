#produtos: refrigerante, agua, chocolate, salgadinhos
#botoes: 1, 2, 3, 4, 5
# 1: compra refrigerante
# 2: compra agua
# 3: compra chocolate
# 4: compra salgadinho
# 5: devolve troco

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
    return (c_10, c_5, c_2, c_1, m_50, m_25, m_10, m_5)

def estoque_inicial():
    q_ref = int(input("Estoque inicial de refrigerante: "))
    q_agu = int(input("Estoque inicial de agua: "))
    q_cho = int(input("Estoque inicial de chocolate: "))
    q_sal = int(input("Estoque inicial de salgadinho: "))
    return (q_ref, q_agu, q_cho, q_sal)
