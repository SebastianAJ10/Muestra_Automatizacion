from app import suma, saludo

def test_suma_numeros_positivos():
    a, b = 5, 3
    resultado = suma(a, b)
    assert resultado == 8, f'Se esperaba 8, se obtuvo {resultado}'

def test_suma_numeros_negativos():
    assert suma(-2, -3) == -5

def test_suma_cero():
    assert suma(0, 5) == 5

def test_saludo_contiene_nombre():
    resultado = saludo('Maria')
    assert 'Maria' in resultado, 'El saludo debe contener el nombre'

def test_saludo_es_cadena():
    assert isinstance(saludo('Carlos'), str)
