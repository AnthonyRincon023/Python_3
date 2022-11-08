
class Alumno():
    
    def __init__(self):
        self.nombre=input("ingrese su nombre: ") 
        self.nota=int(input("ingrese su nota: ")) 

    def mostrar(self):
        print("Nombre: " ,self.nombre)    
        print("Nota: ",self.nota)

    def Valoracion(self):
        if self.nota >=3:
            print(f"{self.nombre}, ha aprobado")
        else:    
            print(f"{self.nombre}, ha reprobado")     
         
alumno1 = Alumno()
alumno1.mostrar()
alumno1.Valoracion()
    
             
        