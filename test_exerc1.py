def calcular_valor_com_desconto(valor_unitario, quantidade):
    desconto = 1

    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    valor_com_desconto = valor_unitario * desconto * quantidade
    return valor_com_desconto

def test_calcular_valor_com_desconto():
    resultado = calcular_valor_com_desconto(10.0, 5)
    assert resultado == 50.0

    resultado = calcular_valor_com_desconto(10.0, 50)
    assert resultado == 475.0

    resultado = calcular_valor_com_desconto(10.0, 500)
    assert resultado == 4500.0

    resultado = calcular_valor_com_desconto(10.0, 1500)
    assert resultado == 12750.0