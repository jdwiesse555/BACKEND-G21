class Auto:
    
    def __init__(self,modelo,limite):
        self.modelo = modelo
        self.limite = limite
        self.velocidad= 0

    
    def acelerar(self):
        self.velocidad =  self.velocidad + 10
        print(f"velocidad : {self.velocidad} ")
        
dd = Auto("vw",120)    
dd.acelerar()

dd.acelerar()