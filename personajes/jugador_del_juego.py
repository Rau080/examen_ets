class Jugador_Del_Juego:
    def __init__(self, nombre, Rol):
        self.Nombre = nombre
        self.rol = Rol
        self.esta_vivo = True

    def AccionNocturna(self, objetivo=None):
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
