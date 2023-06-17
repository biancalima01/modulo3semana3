import pytest
from exercicio2 import cardapio

def calcular_total_pedidos(pedidos):
    total = 0.0
    for codigo in pedidos:
        if codigo == 100:
            total += 9.00
        elif codigo == 101:
            total += 11.00
        elif codigo == 102:
            total += 12.00
        elif codigo == 103:
            total += 12.00
        elif codigo == 104:
            total += 14.00
        elif codigo == 105:
            total += 17.00
        elif codigo == 200:
            total += 5.00
        elif codigo == 201:
            total += 4.00
    return total

def test_calcular_total_pedidos():
    assert calcular_total_pedidos([100, 101, 102, 103, 104, 105, 200, 201]) == 84.00
    assert calcular_total_pedidos([100, 102, 104]) == 35.00
    assert calcular_total_pedidos([201, 201, 201, 201]) == 16.00