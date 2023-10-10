from src.ejercicio13 import division, calcularResto

def test_division():
    assert division(10,2) == 5
    assert division(15,3) == 5
    assert division(7,2) == 3
    
    try:
        division(10,0)
    except ZeroDivisionError:
        pass
    else:
        assert False

def test_calcularResto():
    assert calcularResto(10,2) == 0
    assert calcularResto(15,3) == 0
    assert calcularResto(7,2) == 1

    try:
        calcularResto(10,0)
    except ZeroDivisionError:
        pass
    else:
        assert False

if __name__ == "__main__":
    import pytest
    pytest.main()