from src.ejercicio10 import operacion

def test_operacion():
    resultado_esperado = ((3+2) / (2*5))**2
    assert operacion() == resultado_esperado

if __name__ == "__main__":
    import pytest
    pytest.main()