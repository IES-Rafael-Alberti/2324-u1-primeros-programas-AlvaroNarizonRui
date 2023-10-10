from src.ejercicio15 import LeerDinero, calcularInteres

def test_LeerDinero():
    resultado = LeerDinero(1000.0)
    assert resultado == 1000.0
def test_calcularInteres():
    resultado = calcularInteres(1000.0,4.0)
    assert resultado == 960.0

if __name__ == "__main__":
    import pytest
    pytest.main()