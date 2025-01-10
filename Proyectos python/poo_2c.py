class Personaje:
    #atributos de la clase
    # nombre = 'Default'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    #¿qué es self?Es una referencia al mismo objeto
    #¿qué es el metodo init? contructor que inicializa los atributos de un objeto
    #¿porque se usa doble guion bajo? dunder, porque es metodo magico
    #¿cuando se ejecuta el metodo init? autom. al crear una nueva instancia 
        
    def imprimir_atributos(self):
        print("-Nombre:",self.nombre)
        print("-Fuerza:",self.fuerza)
        print("-Inteligencia:",self.inteligencia)
        print("-Defensa:",self.defensa)
        print("-Vida:",self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligecia = self. inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto....")
        
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa 
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "Puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es:", enemigo.vida)
    
#el personaje es el constructor
#variable del constructor 
mi_personaje = Personaje("EsteBandido", 100, 50, 45, 100)
mi_personaje.imprimir_atributos()


print("Los valores han sido actualizados!")
mi_personaje.subir_nivel(15, 5, 10)
mi_personaje.imprimir_atributos()
#mi_personaje.morir()
print(mi_personaje.esta_vivo())
mi_enemigo = Personaje("Angel", 70, 100, 70, 100)
mi_personaje.atacar(mi_enemigo)


#modificando valores de los tributos
# mi_personaje.nombre = "EstebanDido"
# mi_personaje.fuerza = 300
# mi_personaje.inteligencia = -2
# mi_personaje.defensa = 30
# mi_personaje.vida = 2

# print("El nombre de mi personaje es:",mi_personaje.nombre)
# print("El fuerza de mi personaje es:",mi_personaje.fuerza)
# print("El inteligencia de mi personaje es:",mi_personaje.inteligencia)
# print("El defensa de mi personaje es:",mi_personaje.defensa)
# print("El vida de mi personaje es:",mi_personaje.vida)