import random


class Jugador:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def recibir_ataque(self, dano):
        dano_real = dano - self.defensa
        if dano_real > 0:
            self.vida -= dano_real
            print(f"{self.nombre} ha recibido {dano_real} puntos de daño.")
        else:
            print(f"{self.nombre} ha bloqueado el ataque.")
        
    def atacar(self, oponente):
        dano = random.randint(self.ataque - 2, self.ataque + 2)
        print(f"{self.nombre} ataca con {dano} puntos de daño.")
        oponente.recibir_ataque(dano)


class Rival:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def recibir_ataque(self, dano):
        dano_real = dano - self.defensa
        if dano_real > 0:
            self.vida -= dano_real
            print(f"{self.nombre} ha recibido {dano_real} puntos de daño.")
        else:
            print(f"{self.nombre} ha bloqueado el ataque.")
        
    def atacar(self, oponente):
        dano = random.randint(self.ataque - 2, self.ataque + 2)
        print(f"{self.nombre} ataca con {dano} puntos de daño.")
        oponente.recibir_ataque(dano)


def jugar():
    
    jugador = Jugador("Jugador", vida=100, ataque=15, defensa=5)
    rival = Rival("Rival", vida=100, ataque=12, defensa=4)

    print("¡Comienza la lucha!")

    while jugador.vida > 0 and rival.vida > 0:
        print(f"\nVida del Jugador: {jugador.vida}")
        print(f"Vida del Rival: {rival.vida}")

        
        accion = input("¿Qué deseas hacer? (atacar/defender): ").lower()

        if accion == "atacar":
            jugador.atacar(rival)
        elif accion == "defender":
            jugador.defensa += 3
            print(f"{jugador.nombre} se defiende, ahora tiene {jugador.defensa} de defensa.")
        else:
            print("Opción no válida. Debes elegir 'atacar' o 'defender'.")

        
        if rival.vida > 0:
            rival.atacar(jugador)
    
    if jugador.vida <= 0:
        print("\nEl Rival ha ganado. ¡Game Over!")
    elif rival.vida <= 0:
        print("\n¡Has derrotado al Rival! ¡Felicidades!")


if __name__ == "__main__":
    jugar()
