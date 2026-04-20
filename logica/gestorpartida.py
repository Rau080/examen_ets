from personajes import jugador_del_juego


class GestorPartida:
    def __init__(self):
        self.jugadores = []

    def anadirJugador(self, nombre, type):
        self.jugadores.append(jugador_del_juego(nombre, type))

    def VotacionDia(self, NombreVotado):
        for j in self.jugadores:
            j: jugador_del_juego
            if j.Nombre == NombreVotado:
                if j.esta_vivo:
                    j.esta_vivo = False
                    return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
        return "Nadie fue linchado."

    def ComprobarVictoria(self):

        list = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        dict = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)

        if list >= dict:
            return "¡Victoria de los Lobos!"
        elif list == 0:
            return "¡Victoria de los Aldeanos!"
        return "La partida debe continuar..."
