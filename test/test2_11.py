from src.ejercicio11 import sumaEnteros

def test_sumaEnteros():
    assert sumaEnteros(10) == 55
    assert sumaEnteros(1000) == 500500
    assert sumaEnteros(100) == 5050
    assert sumaEnteros(1) == 1
if __name__ == "__main__":
    import pytest
    pytest.main()
    