class personaje:
    #atributos de la clase
    #nombre="Default"
    #fuerza=0
    #inteligencia=0
    #defensa=0
    #vida=0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,posima):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.vida=vida
        self.posima=posima    
        #codigo que cambia atributos segun la posima, lo pongo aqui para que todos lo hereden y se ejecute al inicializar los atributos
        if posima==1: #el uno es para la vida
            self.vida= (self.vida)+20
        elif posima==2: #este para multiplicar el ataque y tenga 50% mas
            self.fuerza= int(self.fuerza * 1.5)
        elif posima == 3: #para tener mas inteligencia, se le suma 60
            self.inteligencia= self.inteligencia +60
        else:
            pass #sino no hace ni mais
    #importante, para mostrar el nombre y que no salga la direccion del objeto se usa losiguiente
    def __repr__(self):
        return f"{self.nombre}: Vida {self.vida}"
    
    
    #¿Qué es self? es una referencia al mismo objeto
    #que el el metodo init? constructor que inicializa los atributos de un objeto
    #pq se usa doble guion bajo? Dunder. porque es un metodo magico.
    #cuando se ejecuta el metodo init? Autom. al crear una nueva instacia u objeto
    #¿Que es polimorfismo ejemplo? un mismo metodo va a tener diferente comportamiento dependiendo de que objeto lo llame
    
    
    
    def imprimir_atributos(self):
        print(self.nombre)
        print("-fuerza:",self.fuerza)
        print("-inteligencia:",self.inteligencia)
        print("-defensa:",self.defensa)
        print("-vida:",self.vida)
    
    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def está_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida=0
        print(self.nombre,"ha muerto")
        
    def dañar(self,enemigo):
        return self.fuerza - enemigo.defensa 
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        if daño<0:
            enemigo.defensa=enemigo.defensa-self.fuerza
            print(self.nombre,"Ha hecho",self.fuerza,"puntos de daño a la defensa a",enemigo.nombre)
            print("la defensa de", enemigo.nombre, "es", enemigo.defensa)
        else:
            enemigo.vida = enemigo.vida- daño
            enemigo.defensa= enemigo.defensa *0
            if enemigo.vida<0:
                enemigo.morir()
            print(self.nombre,"Ha hecho",daño,"puntos de daño a",enemigo.nombre)
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
            
class Guerrero(personaje):
    #sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,espada,escudo,posima):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida,posima)
        self.espada=espada
        self.escudo=escudo
        self.defensa= defensa*escudo
        
    #sobreescribir imprecion de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-espada:",self.espada)
        
    #sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
    #escoger espada
    def escoger_navaja(self):
        opcion= int(input("escoge la espada de energia: \n (1) Espada normal, daño 10, \n (2) Espada dañada, daño 6\n>>>>"))
        if opcion ==1 :
            self.espada= 10
        elif opcion == 2:
            self.espada= 6
        else:
            print("valor invalido, intente de nuevo")
            #vuelve a ejecutar el metodo
            self.escoger_navaja()

class Mago(personaje):
    #sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,libro,posima):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida,posima)
        self.libro=libro
        
    #sobreescribir imprecion de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-libro:",self.libro)
        
    #sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
    #escoger espada
    def escoger_libro(self):
        opcion= int(input("escoge el mejor libro: \n (1) libro de magia negra , daño 10, \n (2) libro normal, daño 6\n>>>>"))
        if opcion ==1 :
            self.libro= 10
        elif opcion == 2:
            self.libro= 6
        else:
            print("valor invalido, intente de nuevo")
            #vuelve a ejecutar el metodo
            self.escoger_libro()
            
def personaje_con_mayor_vida(personajes):
    """
    devuelve el que tenga vida maxima entre los personajes de una lista
    """
    return max(personajes, key=lambda p: p.vida)
#aqui pasan varias cosas, lambda es como una funcion pero en chiquito, solo se ejecuta una ves, max compara y muestra el maximo de una lista
#key= lambda es para comparar, primero ponemos personajes pq es lo que vamos a comparar, luego key= lambda para hacer la funcion chiquita,
#p, es para la variable que le vamos a pasar, luego esa variable le va a agragar.vida, va a comparar y devolver el que tenga mas vida

def suma_inteligencia(personajes):
    """
    Esto papito va a sumar las inteligencias de todos
    """
    return sum(chavo.inteligencia for chavo in personajes)

def vida_mayor_k(personajes,numero):
    mayores_q=[]
    
    for chavo in personajes:
        if chavo.vida>numero:
            mayores_q.append(chavo)
    return mayores_q
        
mi_personaje= personaje("master chif",20,15,10,100,2)
arturoSuarez = Guerrero("Arutro",20,15,10,100, 5,2,0)
gandalf = Mago("gandalf",20,15,10,100, 5,0)

#los guardamos en una lista para poder compararlos
personajes = [mi_personaje, arturoSuarez, gandalf]

#atributos antes de la tragedia
mi_personaje.imprimir_atributos()
gandalf.imprimir_atributos()
arturoSuarez.imprimir_atributos()

#ataque a lo desgraciado
mi_personaje.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(mi_personaje)

#atributos despues del desmadre
mi_personaje.imprimir_atributos()
gandalf.imprimir_atributos()
arturoSuarez.imprimir_atributos()

personaje_mayor_vida = personaje_con_mayor_vida(personajes)
print(f"El personaje con mayor vida es: {personaje_mayor_vida}")

total_inteligencias = suma_inteligencia(personajes)
print(f"La suma total de inteligencias es: {total_inteligencias}")

numero2= int(input(" intruduce el valor de vida mayor q \n ***"))
personajes_mayor_k= vida_mayor_k(personajes,numero2)
if len(personajes_mayor_k)==0:
    print(f"nadia tiene mas de {numero2}")
else:
    print(f"los personajes con mas vida que eso son {personajes_mayor_k}")

#print(f"El valor de espada es: {arturoSuarez.espada}")
#variable del constructor 

#mi_personaje.imprimir_atributos()
mi_enemigo= personaje("El malo",10,50,45,100,0)
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.imprimir_atributos()

# mi_personaje.subir_nivel(15,20,30)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()
#modificando valores de los atributos
#mi_personaje.nombre="jhon 117"
#mi_personaje.fuerza=200000
#mi_personaje.inteligencia=44
#mi_personaje.defensa=44
#mi_personaje.vida=1

#print("El nombre de mi personaje es: ",mi_personaje.nombre)
#print("La fuerza mi personaje es: ",mi_personaje.fuerza)
#print("La inteligencia de mi personaje es: ",mi_personaje.inteligencia)
#print("La defensa de mi personaje es: ",mi_personaje.defensa)
#print("La vida de mi personaje es: ",mi_personaje.vida)