from src.ejercicio6 import calcularImporteBase

def test_calcularImporteBase():
    assert calcularImporteBase(110.0) == 99.0
    assert calcularImporteBase(120.0) == 108.0
    assert calcularImporteBase(105.0) == 94.5
if __name__ == "__main__":
    import pytest
    pytest.main()