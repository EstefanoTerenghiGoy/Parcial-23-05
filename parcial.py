

def calcular_promedio(lista, valor): #Parametros formales
    """
    Dada una lista de numeros y un valor, calcula el promedio de la lista.
    Devuelve True en caso de que el promedio sea mayor que el valor,
    y False en caso contrario
    """
    es_mayor = True
    total = 0
    for num in lista:
        total += num
    promedio = total / len(lista)
    
    return promedio > valor
    
    

lista = [10, 20, 30, 40] #Parametro actual
valor = 28               #Parametro actual

calcular_mayor = calcular_promedio(lista, valor) #Invocación de la función

if calcular_mayor: 
    print("El promedio es mayor que el valor")
else:
    print("El valor es mayor que el promedio")