from src.ejercicio14 import CalcularPedido

def test_CalcularPedido():
    resultado = CalcularPedido(5,3)
    assert resultado == 675

    resultado = CalcularPedido(0,10)
    assert resultado == 750

if __name__ == "__main__":
    import pytest
    pytest.main()