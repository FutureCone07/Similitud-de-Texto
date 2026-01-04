frase1 = input("ingrese su primer frase:").lower()
frase2 = input("ingrese su segunda frase:").lower()

#Funcion para buscar cuantas palabras existen en nuestro arreglo
def contar_palabras(fraseParaAnalizar):
    recuento_palabras = {}
    for palabra in fraseParaAnalizar.split():
        if palabra in recuento_palabras:
            recuento_palabras[palabra] += 1
        else:
            recuento_palabras[palabra] = 1
    return recuento_palabras
#Calcular el Producto Punto
def calcular_producto_punto(arreglo1, arreglo2):
    pP = 0
    for clv,value in arreglo1.items():
        value2 = arreglo2.get(clv, 0)
        if value2 > 0:
            pP += value * value2
    return pP
#Calcular la magnitud
def calcular_magnitud(arreglo):
    magnitud = 0
    for clv,value in arreglo.items():
        magnitud += (value**2)
    return magnitud ** 0.5

#Aplicar la formula
resultado1 = contar_palabras(frase2)
resultado2 = contar_palabras(frase1)
producto_punto = calcular_producto_punto(resultado1,resultado2)
moduloA =calcular_magnitud(resultado1)
moduloB = calcular_magnitud(resultado2)
similitud = ((producto_punto)/(moduloA*moduloB))*100
print(round(similitud,2),"% de similitud")


