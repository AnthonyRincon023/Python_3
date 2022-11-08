class calculadora():

    def __init__(self):
        self.num1 = int(input("Ingrese el primer numero "))
        self.num2 = int(input("Ingrese el segundo numero "))
    
    def suma(self):
        suma = self.num1+self.num2
        print("El resultado de la suma es: ", suma)
    def resta(self):
        resta = self.num1-self.num2
        print("El resultado de la resta es ",resta)
    def multiplicacion(self):
        multiplicacion = self.num1*self.num2
        print("El resultado de la multiplicacion es ",multiplicacion)    

    def division(self):
        division = self.num1/self.num2
        print("El resultado de la division es: ",division)
        
usuario = calculadora()
usuario.suma()
usuario.resta()
usuario.multiplicacion()
usuario.division()
