class Jugador_Del_Juego:

    """Crea el juego y sus jugadores

    Attributes:
        nombre (str): nombre del jugador
        rol (str): crea el rol del jugador
        esta_vivo (bool): estado del jugador
    """

    def __init__(self, nombre, Rol):
        self.Nombre = nombre
        self.rol = Rol
        self.esta_vivo = True

    def AccionNocturna(self, objetivo=None):

        """ Implementa lo que hace el jugador.

        Args:
            objetivo (object): El objetivo al cual va a cazar

        Returns:
            str: Acciones del juego.

        """

        if not self.esta_vivo:
            return f"{self.Nombre} está muerto."

        if self.rol == "lobo":
            if objetivo:
                objetivo.esta_vivo = False
                return f"El lobo {self.Nombre} ha eliminado a {objetivo.Nombre}."
        elif self.rol == "vidente":
            if objetivo:
                return f"La vidente {self.Nombre} ve que {objetivo.Nombre} es {objetivo.rol}."
        elif self.rol == "aldeano":
            return f"El aldeano {self.Nombre} duerme profundamente."
        return "Rol desconocido."
