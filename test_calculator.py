import calculator

def test_addition():
    assert 4 == calculator.add(2, 2)

def test_substraction():
    assert 3 == calculator.subtract(6, 3)

def test_multiplication():
    assert 100 == calculator.multiply(10, 10)