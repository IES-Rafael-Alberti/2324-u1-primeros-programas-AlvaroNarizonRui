import pytest
from src.ejercicio5 import calcularIVA

def test_calcularIVA():
    assert calcularIVA(150,21) == 181.5
    assert calcularIVA(100,21) == 121.0

if __name__ == "__main__":
    import pytest
    pytest.main()