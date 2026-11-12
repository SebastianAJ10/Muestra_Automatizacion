def suma(numero_a, numero_b):
    return numero_a + numero_b


def saludo(nombre):
    return f'Hola, {nombre}. Bienvenido al mundo de GitHub Actions.'


if __name__ == '__main__':
    print(f'Resultado de 5+3 = {suma(5, 3)}')
    print(saludo('Estudiante'))
