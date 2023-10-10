from src.ejercicio7 import suma

def test_suma():
    assert suma(5,10,15) == 30
    assert suma(-2,-3,-5) == -10
    assert suma(8-4,6) == 10
    assert suma(0,10,0) == 10
    assert suma(1000,2000,3000) == 6000
if __name__ == "__main__":
    import pytest
    pytest.main()