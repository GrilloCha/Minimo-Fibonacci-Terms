#Codigo hecho por: Carlos Téllez

# Verificamos si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Generamos la serie de Fibonacci hasta el valor k
# Los elementos no primos los agregamos a una lista
def fibonacci(k, lista): 
    f = 1
    aux = 1

    while f + aux <= k:
        temp = f
        f = f + aux
        if not es_primo(f):
            lista.append(f)
        aux = temp

    return f

# Encontramos cuántos elementos se necesitan para llegar a k restando desde los más grandes
def restar(k, lista):
    lista_ordenada = sorted(lista, reverse=True)
    #sorted devuelve lista ordenada segun parametros indicados
    cont = 0
    usado = [] 

    for valor in lista_ordenada:
        while k - valor >= 0:
            k -= valor
            cont += 1
            usado.append(valor)

    return cont, usado

# Función principal
def funcion():
    lista = []
    lista.append(1)
    lista.append(1)
    k = int(input("Dame el número a calcular: "))
    f = fibonacci(k, lista)

    print("Números de Fibonacci NO primos hasta", k, ":")
    print(lista)

    cantidad, usados = restar(k, lista)
    print(f"\nPara llegar a {k}, se necesitan {cantidad} elementos de la lista (por suma):")
    print(usados)

funcion()
