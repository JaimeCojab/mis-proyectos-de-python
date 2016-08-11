op = input ("Por favor dime que quieres hacer \n suma = 1 \n resta = 2\n mult = 3\n div = 4 \n")
x = input ("porfavor escriba un numero ")
y = input ("porfavor escriba otro numero ")
#Declaramos la funcion suma
def suma (x,y):
    a = x + y
    return str(a)
#Declaramos la funcion resta
def resta (x, y):
    b = x - y
    return str(b)
#Declaramos la funcion multiplicacion
def Mult (x, y):
    c = x * y
    return str(c)
#Declaramos la funcion Division
def div (x, y):
    d = float(x) /float (y)
    return  str(d)
#Llamamos a la funcion suma y la guardamos en una variable
suma = suma (x,y)
#Llamamos a la funcion resta y la guardamos en una variable
resta = resta (x,y)
#Llamamos a la funcion multiplicacion y la guardamos en una variable
Mult = Mult (x,y)
#Llamamos a la funcion Division y la guardamos en una variable
div = div (x,y)

#Imprimimos el resultado final en base a la eleccion del usuario
if op == 1:
    print ("suma = " + suma)
if op == 2:
    print ("resta = " + resta)
if op == 3:
    print ("mult = " + Mult)
if op == 4:
    print ("div " + div)
