from personajes import jugador_del_juego


class GestorPartida:

    """ Gestion de la partida

    Attributes:
        nombre (list): lista de los jugadores creados

    """

    def __init__(self):
        self.jugadores = []

    def anadirJugador(self, nombre, type):

        """ Implementa lo que hace el jugador.

        Args:
            nombre (str): nombre del jugador a crear
            type (str): tipo de jugador

        Returns:
            list: añadir al jugador.

        """

        self.jugadores.append(jugador_del_juego(nombre, type))

    def VotacionDia(self, NombreVotado):

        """ Determina el dia y se añade una votación

        Args:
            NombreVotado (str): nombre al quien a votado

        Returns:
            str: informacion del procreso del dia.

        """

        for j in self.jugadores:
            j: jugador_del_juego
            if j.Nombre == NombreVotado:
                if j.esta_vivo:
                    j.esta_vivo = False
                    return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
        return "Nadie fue linchado."

    def ComprobarVictoria(self):


        """ 
        
        Determina si han ganado

        Returns:
            str: Determina si han ganado o no.

        """

        list = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        dict = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)

        if list >= dict:
            return "¡Victoria de los Lobos!"
        elif list == 0:
            return "¡Victoria de los Aldeanos!"
        return "La partida debe continuar..."
