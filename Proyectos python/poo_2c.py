class Personaje:
    #atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    
#el personaje es el constructor
#variable del constructor vacío
mi_personaje = Personaje()
#modificando valores de los tributos
mi_personaje.nombre = "EstebanDido"
mi_personaje.fuerza = 300
mi_personaje.inteligencia = -2
mi_personaje.defensa = 30
mi_personaje.vida = 2

print("El nombre de mi personaje es:",mi_personaje.nombre)
print("El fuerza de mi personaje es:",mi_personaje.fuerza)
print("El inteligencia de mi personaje es:",mi_personaje.inteligencia)
print("El defensa de mi personaje es:",mi_personaje.defensa)
print("El vida de mi personaje es:",mi_personaje.vida)