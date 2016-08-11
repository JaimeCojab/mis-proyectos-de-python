from random import randint

maquina = randint (1,10)
usuario = None
while usuario != maquina:
    usuario = input ("elige un numero del 1 al \n10 y trata de adivinar el numero que\nesta pensando la computadora\n")
    if usuario == maquina:
        print "adivinaste el numero"
    else:
        print "no es el numero"
