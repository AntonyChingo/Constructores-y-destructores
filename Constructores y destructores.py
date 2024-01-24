class EjemploClase:
    def __init__(self, nombre):
        """
        Constructor de la clase. Se llama automáticamente al crear un nuevo objeto.

        Parámetros:
        - nombre: str, nombre que se asignará al objeto.
        """
        self.nombre = nombre
        print(f"Objeto {self.nombre} creado.")

    def __del__(self):
        """
        Destructor de la clase. Se llama automáticamente al eliminar un objeto.
        Realiza alguna limpieza o cierre de recursos (simulado con un mensaje en este caso).
        """
        print(f"Objeto {self.nombre} destruido. Realizando limpieza.")


# Crear instancias de la clase
objeto1 = EjemploClase("Objeto1")
objeto2 = EjemploClase("Objeto2")

# Simular eliminación de un objeto (activa el destructor)
del objeto1

# Crear otro objeto
objeto3 = EjemploClase("Objeto3")

# Simular eliminación de otro objeto (activa el destructor)
del objeto2
del objeto3