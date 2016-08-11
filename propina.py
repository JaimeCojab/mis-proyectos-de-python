# -*- coding: utf-8 -*-
cuenta = input ("Cuanto fue el total")
propina_porcentaje = 0.15

def total (cuenta):
    multi = cuenta * propina_porcentaje
    total = cuenta + multi
    return total, multi

print "la propina es " + str(total(cuenta)[1])
print "el total es " + str(total(cuenta)[0])
