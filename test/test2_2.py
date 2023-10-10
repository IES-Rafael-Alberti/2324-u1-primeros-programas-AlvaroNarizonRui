import pytest
from src.ejercicio2 import calcularImporte

def test_calcularImporte():
    assert calcularImporte(5,10) == 50
    assert calcularImporte(0,0) == 0
if __name__ == "__main__":
    import pytest
    pytest.main()
