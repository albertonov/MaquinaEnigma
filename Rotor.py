class Rotor:
    #Clase Rotor. Cuenta con 3 parametros:
    # clave es la clave en la que se encuentra (posicion) que va rotando dinamicamente
    # alfabetoRotor es el alfabeto propio del rotor
    # clave de Desplazamiento almacena la clave donde se va producir el desplazamiento del siguiente rotor.


    def __init__(self, numeroRotor, clave):
        alfabetorotor3 = ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G",
                          "A", "K", "M", "U", "S", "Q", "O"]  # INF
        alfabetorotor2 = ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z",
                          "N", "P", "Y", "F", "V", "O", "E"]
        alfabetorotor1 = ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S",
                          "P", "A", "I", "B", "R", "C", "J"]

        self.clave = clave
        if  numeroRotor== 1:
            self.alfabetorotor = alfabetorotor1
            self.claveDesplazamiento = "Q"
        elif numeroRotor == 2:
            self.alfabetorotor = alfabetorotor2
            self.claveDesplazamiento = "E"
        elif numeroRotor == 3:
            self.alfabetorotor = alfabetorotor3
            self.claveDesplazamiento = "V"
        else:
            print("Error al seleccionar rotor")
            exit()

    #Funcion que pasa el valor de la clave a su posicion siguiente
    def nextLetra(self):
        alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
        aux = Rotor.getNumero(self, self.clave, alfabeto)
        self.clave = alfabeto[(aux + 1) % 26]
        #return alfabeto[(aux + 1) % 26]
    #Funcion auxiliar que devuelve el numero de una letra en el abecedario
    def getNumero(self, letra, alf):
        numero = 0
        for element in alf:
            if element == letra:
                return numero
            numero += 1
        return -1