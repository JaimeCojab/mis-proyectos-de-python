class Alumno(object):

    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion
    def mostrar_nombre(self):
        return "El alumno se llama %s" % self.nombre

a = Alumno("Juan", 25, 10)
print a.mostrar_nombre()
