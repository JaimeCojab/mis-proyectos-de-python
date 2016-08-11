from random import randint

maquina = randint (1,3)
persona = input ("si quieres sacar piedra elije 1 \nsi quieres tijera elije 2 \nsi quieres papel elije 3\n")

if maquina == 1 and persona == 2:
    print "maquina saco piedra\ntu sacaste tijera\nperdiste ):"
elif maquina == 1 and persona == 3:
    print "maquina saco piedra \ntu sacaste papel \nganaste (:"
elif maquina == 2 and persona == 1:
    print "maquina saco tijera\ntu sacaste piedra \nganaste (:"
elif maquina == 2 and persona == 3:
    print "maquina saco tijera\ntu sacaste papel \nperdiste ):"
elif maquina == 3 and persona == 1:
    print "maquina saco papel \ntu sacaste piedra \nperdiste ):"
elif maquina == 3 and persona == 2:
    print "maquina saco papel \ntu sacaste tijera \nganaste (:"
elif maquina == persona:
    print "la maquina saco el mismo \nnumero que tu \nempate /:"
