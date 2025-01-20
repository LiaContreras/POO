class Personaje:
    # Constructor de la clase
    #atributos de la clase
    #nombre="Default"
    #fuerza=0
    #inteligencia=0
    #defensa=0
    #vida=0
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
        print(self.nombre, "Se murió:(")
        return self.vida <= 0

    def dmg(self, enemigo):
        # Si la defensa del enemigo es mayor o igual que la fuerza del atacante, el daño es 0
        return max(0, self.fuerza - enemigo.defensa)

    def atacar(self, enemigo):
        daño = self.dmg(enemigo)
        enemigo.recibir_daño(daño)
        print(self.nombre, "Ha realizado", daño, "puntos de daño a:", enemigo.nombre)

    def recibir_daño(self, daño):
        self.vida = max(0, self.vida - daño)

class Guerrero(Personaje):
    # Sobrescribir constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada, escudo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.escudo = escudo
        self.vida_escudo = defensa * escudo

    # Sobrescribir impresión
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.espada)
        print("-Escudo:", self.escudo, "(Su protección de escudo es:", self.vida_escudo, ")")

    # Sobrescribir cálculo de daño
    def dmg(self, enemigo):
        return max(0, self.fuerza * self.espada - enemigo.defensa)

    # Sobrescribir recibir daño para manejar el escudo
    def recibir_daño(self, daño):
        if self.vida_escudo > 0:
            if daño < self.vida_escudo:
                self.vida_escudo -= daño
                print(self.nombre, "Ha absorbido el daño con el escudo. Protección del escudo restante:", self.vida_escudo)
            elif daño == self.vida_escudo:
                self.vida_escudo = 0
                print(self.nombre, "Ha perdido el escudo. Ahora está desprotegido. Cuidado!!!")
            else:
                daño_restante = daño - self.vida_escudo
                self.vida_escudo = 0
                print(self.nombre, "Ha perdido el escudo. Daño restante aplicado a la vida:", daño_restante)
                super().recibir_daño(daño_restante)
        else:
            super().recibir_daño(daño)

# Método de combate por turnos
def combate(personaje1, personaje2):
    turno = 1
    while personaje1.esta_vivo() and personaje2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        personaje1.atacar(personaje2)
        if personaje2.esta_vivo():
            personaje2.atacar(personaje1)
        turno += 1

    if personaje1.esta_vivo():
        print(f"\n{personaje1.nombre} Ganó el combate.")
    else:
        print(f"\n{personaje2.nombre} Ganó el combate.")

class Mago (Personaje):
    #Sobrescribir constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    #Sobrescribir impresion
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Libro:", self.libro)

    def elegir_arma(self):
        opcion = int(input("Elige un arma: \n(1)Hechizoz de programacion, dmg 10 \n(2)Recetario de chaya, dmg 6\n<<"))
        if opcion == 1:
            self.libro = 10
        elif opcion == 2:
            self.libro == 5
        else:
            print("Opcion no valida")
            self.elegir_arma()

    #Sobrescribir calculo de dmg
    def dmg(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

# Función para manejar las pociones
def usar_pocion(personaje, tipo_pocion):
    if tipo_pocion == "vida":
        personaje.vida += 20
        print(f"{personaje.nombre} Ha usado una poción de vida. Su vida actual es: {personaje.vida}")
    elif tipo_pocion == "fuerza":
        personaje.fuerza = int(personaje.fuerza * 1.5)
        print(f"{personaje.nombre} Ha usado una poción de fuerza. Su fuerza actual es: {personaje.fuerza}")
    elif tipo_pocion == "inteligencia":
        personaje.inteligencia = int(personaje.inteligencia * 1.5)
        print(f"{personaje.nombre} Ha usado una poción de inteligencia. Su inteligencia actual es: {personaje.inteligencia}")
    else:
        print("Tipo de poción no válido:(.")

# Función para encontrar el personaje con mayor vida
def personaje_con_mayor_vida(personajes):
    """
    devuelve el que tenga vida maxima entre los personajes de una lista
    """
    return max(personajes, key=lambda p: p.vida)
# Función para calcular la suma total de inteligencia de todos los personajes
def suma_total_inteligencia(personajes):
    return sum(p.inteligencia for p in personajes)

# Función para filtrar personajes con vida mayor a un valor dado
def filtrar_personajes_por_vida(personajes, valor_vida):
    personajes_filtrados = [p for p in personajes if p.vida > valor_vida]
    if personajes_filtrados:
        print(f"\nPersonajes que contiene mayor vida mayor a {valor_vida}:")
        for p in personajes_filtrados:
            print(f"- {p.nombre}: {p.vida} de vida")
    else:
        print(f"No hay personajes con vida mayor a {valor_vida}.")

# Ejemplo de uso
if __name__ == "__main__":
    esteban = Guerrero("---EsteBandido---", 1, 70, 5, 100, 5, 2)
    angelito = Mago("---Angelito---", 1, 1, 10, 111, 7)
    el_suarez = Personaje("---Suarez---", 40, 15, 10, 120)

    personajes = [esteban, angelito, el_suarez]

    personaje_mas_vida = personaje_con_mayor_vida(personajes)
    print(f"\nEl personaje con mayor vida es: {personaje_mas_vida.nombre} con {personaje_mas_vida.vida} de vida.")

    suma_inteligencia = suma_total_inteligencia(personajes)
    print(f"La suma total de la inteligencia de todos los personajes es: {suma_inteligencia}")

    valor_vida = int(input("Coloca cualquier valor de vida para filtrar los personajes: "))
    filtrar_personajes_por_vida(personajes, valor_vida)

    usar_pocion(esteban, "vida")
    usar_pocion(angelito, "fuerza")
    usar_pocion(angelito, "inteligencia")

    el_suarez.imprimir_atributos()
    esteban.imprimir_atributos()
    angelito.imprimir_atributos()
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

#CLASE APUNTES:
#aqui pasan varias cosas, lambda es como una funcion pero en chiquito, solo se ejecuta una ves, max compara y muestra el maximo de una lista
#key= lambda es para comparar, primero ponemos personajes pq es lo que vamos a comparar, luego key= lambda para hacer la funcion chiquita,
#p, es para la variable que le vamos a pasar, luego esa variable le va a agragar.vida, va a comparar y devolver el que tenga mas vida
#¿Qué es self? es una referencia al mismo objeto
#¿Qué el el metodo init? constructor que inicializa los atributos de un objeto
#¿Porqué se usa doble guion bajo? Dunder. porque es un metodo magico.
#¿Cuándo se ejecuta el metodo init? Autom. al crear una nueva instacia u objeto
#¿Qué es polimorfismo ejemplo? un mismo metodo va a tener diferente comportamiento dependiendo de que objeto lo llame