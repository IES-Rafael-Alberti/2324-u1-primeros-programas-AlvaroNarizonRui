import pytest
from src.ejercicio4 import conversorFahrenheit

def test_conversorFahrenheit():
    assert conversorFahrenheit(0) == 32.0
    assert conversorFahrenheit(-10) == 14.0
    assert conversorFahrenheit(100) == 212.0
    assert conversorFahrenheit(37) == 98.6
if __name__ == "__main__":
    import pytest
    pytest.main()