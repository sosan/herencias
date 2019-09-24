"""
HERENCIAS

"""


# supèrclase
class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca {0}\nModelo {1}\nEn Marcha: {2}\nAcelera: {3} \nFrenar: {4}".format(
            self.marca,
            self.modelo,
            self.enmarcha,
            self.acelera,
            self.frena
            # self.caballito # ERROR DE CONCEPTO

        ))


class Moto(Vehiculos):
    # variable global dentro de las clases
    g_caballito = True

    # sobreescritura de metodos. @OVERRIDE
    def estado(self):
        print("HEREDADO Marca {0}\nModelo {1}\nEn Marcha: {2}\nAcelera: {3} \nFrenar: {4}\n cABALLITO: {5} ".format(
            self.marca,
            self.modelo,
            self.enmarcha,
            self.acelera,
            self.frena,
            self.g_caballito  # AQUI YA NO ES UN ERROR DE CONCEPTO
        ))


class Furgoneta(Vehiculos):
    def carga(self, carga):
        self.cargado = carga
        if (self.cargado == True):
            return "La furgo esta cargada"
        else:
            return "La furgo no esta cargada"


# clases electricos, superclase ya que no hereda de ninguna otra clase
# lo mas general posible.
class VElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargaEnergia(self):
        self.cargando = True


# herencia multiple, Velectricos sobreesxribiria vehiculos
class BicicletaElectrica(VElectricos, Vehiculos):
    pass
    # def __init__(self):
    # vehiculos.


# entrada principal
def run():
    # mimoto = Moto("suzisi", "mmkkk")
    # print(mimoto.estado())

    miFurgo = Furgoneta("Renault", "canguro")
    miFurgo.arrancar()
    miFurgo.estado()
    print(miFurgo.carga(True))


if __name__ == '__main__':
    run()
