class Personaje:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")
        return self.vida <= 0
    
    def dmg(self, enemigo):
        # Si la defensa del enemigo es mayor o igual que la fuerza del atacante, el daño es 0
        return max(0, self.fuerza - enemigo.defensa)
    
    def atacar(self, enemigo):
        daño = self.dmg(enemigo)
        # Asegurarse de que la vida no baje de cero
        enemigo.vida = max(0, enemigo.vida - daño)
        print(self.nombre, "Ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)
        
class Guerrero(Personaje):
    
    #sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        
    #Sobreescribir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.espada)

    #Sobreescribir el cálculo de el daño
    def dañar(self, enemigo,):
        return self.fuerza*self.espada - enemigo.defensa 
    
    #escoger navaja
    def escoger_navaja(self):
        opcion = int(input("Escoge la navaja de la muerte:\n(1) Navaja Suiza, daño 10.\n(2) Navaja Pioja, daño 6.\n>>>>>"))
        if(opcion == 1):
            self.espada = 10
        elif(opcion == 2):
            self.espada = 6
        else:
            print("Valor inválido, intente nuevamente")
            #volver a escoger navaja
            self.escoger_navaja()
            
class Mago(Personaje):
    
    #sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        
    #Sobreescribir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Libro:", self.libro)

    #Sobreescribir el cálculo de el daño
    def dañar(self, enemigo,):
        return self.inteligencia*self.libro - enemigo.defensa 
    
    #escoger navaja
    def escoger_libro(self):
        opcion = int(input("Escoge el libro de la sabiduria:\n(1) Principito, daño 10.\n(2) Crepusculo, daño 6.\n>>>>>"))
        if(opcion == 1):
            self.libro = 10
        elif(opcion == 2):
            self.libro = 6
        else:
            print("Valor inválido, intente nuevamente")
            #volver a escoger navaja
            self.escoger_libro()
            
#crear todos objetos
persona = Personaje("Ángel Suarez", 20, 15, 2, 100)
arturoSuarez = Guerrero("Arturo Suárez", 20, 15, 2, 100, 5)
gandalf = Mago("Arturo", 12, 15 ,2 , 100, 5)
#Atributos antes de la tragedia
#arturoSuarez.escoger_navaja()
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()
#Ataques sin piedad
persona.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(persona)

#Atributos después de la tragedia
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()


#print("El valor de la espada es:", arturoSuarez.espada)
#polimorfismo: Un mismo método puede tener un comportamiento diferente dependiendo de el objeto que lo llame

# Ejemplo de uso
#mi_personaje = Personaje('EsteBandido', 40, 10, 30, 100)
#mi_personaje.imprimir_atributos()
#mi_enemigo = Personaje("Ángel", 70, 30, 70, 100)
#mi_personaje.atacar(mi_enemigo)
#un = asigna el valor de una variable mientras que == compara los aributos