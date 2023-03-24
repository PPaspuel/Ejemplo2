
def suma (a,b):
    if(a > 0 and b > 0):
        t = a + b
        return t
    else:
        print("Los numeros ingresados son menores que 0")


prueba = suma(5,9)
print("El resultado es :"+ str(prueba))