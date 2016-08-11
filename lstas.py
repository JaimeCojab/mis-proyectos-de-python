ClaseA = []
ClaseB = []
ClaseC = []
total_alumnos = len(ClaseA) + len(ClaseB) + len(ClaseC)
print total_alumnos
while total_alumnos <= 3:
    alumno = raw_input("como te llamas? ")
    clase = raw_input("en que clase vas? ")
    if clase == "a":
        ClaseA.append(alumno)
        print "A " + str(ClaseA)
    elif clase == "b":
        ClaseB.append(alumno)
        print "B " + str(ClaseB)
    elif clase == "c":
        ClaseC.append(alumno)
        print "C " + str(ClaseC)
    total_alumnos = len(ClaseA) + len(ClaseB) + len(ClaseC)
    print total_alumnos
print ClaseA , ClaseB , ClaseC
