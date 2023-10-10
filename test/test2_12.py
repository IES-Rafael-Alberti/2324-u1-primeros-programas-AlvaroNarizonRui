from src.ejercicio12 import calcularIMC

def test_calcularIMC():
    assert calcularIMC(70.0,1.75) == 22.86
    assert calcularIMC(45.0,1.70) == 15.57
    assert calcularIMC(60.0,1.50) == 26.67
if __name__ == "__main__":
    import pytest
    pytest.main()