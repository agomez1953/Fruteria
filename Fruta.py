class Fruta:

    def __init__(self,sabor,pelada,cantidad):
        self.sabor = sabor
        self.pelada = pelada
        self.cantidad = cantidad

    def pelar(self):
        if self.pelada:
            self.pelada = True

        elif self.pelada:
            self.pelada = False

        return self.pelada

    def cortar(self, cantidad: int):
        if self.pelada and cantidad > 1:
            cantidad -= 1
            return cantidad

    def licuar(self, cantidad: int):
        if self.pelda and cantidad > 0:
            cantidad +=1
            return cantidad