vida_picachu = 100
vida_giglypuff = 110
ataque_picachu = 45
ataque_giglypuff = 35

turno = True

while vida_picachu > 0 or vida_giglypuff > 0:
    if turno == True:
        vida_giglypuff = vida_giglypuff - ataque_picachu
        print "vida jigly"+ str (vida_giglypuff)
        turno = False
    if vida_picachu < 0 or vida_giglypuff < 0:
        break
    if turno == False:
        vida_picachu = vida_picachu - ataque_giglypuff
        print "vida pika"+ str (vida_picachu)
        turno = True

if vida_picachu < 0 :
    print "Gano Jiglypuff"
elif vida_giglypuff < 0:
    print "Gano pikachu"
