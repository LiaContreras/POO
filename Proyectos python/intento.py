class Personaje:
    # Constructor de la clase
    def _init_(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.inventario = {"vida": 0, "fuerza": 0, "inteligencia": 0}

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
        print("-Inventario:", self.inventario)
    
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
        enemigo.recibir_daño(daño)
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)

    def recibir_daño(self, daño):
        self.vida = max(0, self.vida - daño)

    def usar_pocion(self, tipo):
        if self.inventario[tipo] > 0:
            if tipo == "vida":
                self.vida += 50
                print(self.nombre, "ha usado una poción de vida y ha recuperado 50 puntos de vida.")
            elif tipo == "fuerza":
                incremento = self.fuerza * 0.5
                self.fuerza += incremento
                print(self.nombre, f"ha usado una poción de fuerza. Su fuerza ha aumentado en {incremento:.2f}.")
            elif tipo == "inteligencia":
                incremento = self.inteligencia * 0.5
                self.inteligencia += incremento
                print(self.nombre, f"ha usado una poción de inteligencia. Su inteligencia ha aumentado en {incremento:.2f}.")
            self.inventario[tipo] -= 1
        else:
            print(self.nombre, "no tiene pociones de", tipo, "disponibles.")

class Guerrero(Personaje):
    # Sobrescribir constructor
    def _init_(self, nombre, fuerza, inteligencia, defensa, vida, espada, escudo):
        super()._init_(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.escudo = escudo
        self.vida_escudo = defensa * escudo

    # Sobrescribir impresión
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.espada)
        print("-Escudo:", self.escudo, "(Vida del escudo:", self.vida_escudo, ")")

    # Sobrescribir cálculo de daño
    def dmg(self, enemigo):
        return max(0, self.fuerza * self.espada - enemigo.defensa)

    # Sobrescribir recibir daño para manejar el escudo
    def recibir_daño(self, daño):
        if self.vida_escudo > 0:
            if daño < self.vida_escudo:
                self.vida_escudo -= daño
                print(self.nombre, "ha absorbido el daño con el escudo. Vida del escudo restante:", self.vida_escudo)
            elif daño == self.vida_escudo:
                self.vida_escudo = 0
                print(self.nombre, "ha perdido el escudo. Ahora está desprotegido.")
            else:
                daño_restante = daño - self.vida_escudo
                self.vida_escudo = 0
                print(self.nombre, "ha perdido el escudo. Daño restante aplicado a la vida:", daño_restante)
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
        print(f"\n{personaje1.nombre} ha ganado el combate.")
    else:
        print(f"\n{personaje2.nombre} ha ganado el combate.")

# Ejemplo de uso
if _name_ == "_main_":
    tlatoani = Guerrero("**Apocalipto**", 50, 70, 30, 100, 5, 5)
    merlin = Guerrero("*Merlin**", 20, 15, 10, 100, 3, 3)

    # Añadir pociones al inventario
    tlatoani.inventario = {"vida": 2, "fuerza": 1, "inteligencia": 0}
    merlin.inventario = {"vida": 1, "fuerza": 0, "inteligencia": 2}

    tlatoani.imprimir_atributos()
    merlin.imprimir_atributos()

    # Usar pociones
    tlatoani.usar_pocion("fuerza")
    merlin.usar_pocion("inteligencia")

    combate(tlatoani, merlin)

    tlatoani.imprimir_atributos()
    merlin.imprimir_atributos()