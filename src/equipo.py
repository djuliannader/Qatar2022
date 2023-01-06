

class seleccion():
    def __init__(self, nombre:str, confederacion:str, bombo:int):
        self.nombre=nombre
        self.confederacion=confederacion
        self.bombo=bombo
        self.local=False

    def add_local(self):
        self.local=True

