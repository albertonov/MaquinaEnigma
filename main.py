from Rotor import Rotor


def cifrarLetra(letra, c1, c2, c3, rotor1, rotor2, rotor3):
    alfabeto=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    reflecor=["Y", "R", "U", "H", "Q", "S", "L", "D", "P", "X", "N", "G", "O", "K", "M", "I", "E", "B", "F", "Z", "C", "W", "V", "J", "A", "T"]


    clave1= getNumero(c1,alfabeto)
    clave2= getNumero(c2,alfabeto)
    clave3= getNumero(c3,alfabeto)


    clave3 +=1


    #del input al tercer rotor
    a = getNumero(letra, alfabeto)                  #r18
    b = getNumero(alfabeto[clave3-1], alfabeto)     #c3
    c = (a+b+1)%26                                  #21u
    l3= rotor3[c]


    #calculamos ofset tercer roto
    offset3 = getOffset(clave3, l3)


    #del tercer rotor al segundo
    d = (clave2 + offset3)%26    #g6
    e = getNumero(rotor2[d], alfabeto)
    l2=alfabeto[e]

    offset2 = getOffset(clave2, l2)

    f = (clave1+offset2)%26
    g = getNumero(rotor1[f], alfabeto)
    l1=alfabeto[g]

    offset1 = getOffset(clave1,l1)

    h = (getNumero(reflecor[offset1], alfabeto) +clave1)%26

    a = getNumero(alfabeto[h], rotor1)

    offset2 = clave2-clave1
    if (offset2 <0):
        offset2 = offset2 + 26
    b = (a + offset2)%26
    c = getNumero(alfabeto[b], rotor2)
    #print(rotor2[c] + "->" + alfabeto[c])

    offset3 = clave3-clave2
    if(offset3<0):
        offset3 = offset3 +26
    d = (c + offset3)%26
    e = getNumero(alfabeto[d], rotor3)
    #print(rotor3[e] + "->" + alfabeto[e])

    offsetOutput = getOffset(clave3, alfabeto[e])

    salida = alfabeto[offsetOutput]
    return salida
#Funcion auxiliar que devuelve el numero de una letra en el abecedario
def getNumero(letra,alf):
    numero = 0
    for element in alf:
        if element == letra:
            return numero
        numero +=1
    return -1
#Funcion auxiliar que calcula el desplazamiento que existe entre una clave y una letra dadas
def getOffset(clave, letra):
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    encontrado = False
    offset = 0
    aux = clave
    while(not encontrado):
        if letra == alfabeto[aux%26]:
            encontrado = True
        else:
            offset += 1
            aux += 1
    return offset


if __name__ == '__main__':

    numeroRotorI = int(input("¿Que rotor ira en el lado izquierdo? (1, 2, 3): "))
    c1 = input("Introduce la clave rotor izquierda: ")
    rotorI = Rotor(numeroRotorI, c1)


    numeroRotorC = int(input("¿Que rotor ira en el lado central? (1, 2, 3): "))
    c2 = input("Introduce la clave rotor central: ")
    rotorC = Rotor(numeroRotorC, c2)

    numeroRotorD = int(input("¿Que rotor ira en el lado derecho? (1, 2, 3): "))
    c3 = input("Introduce la clave rotor derecho: ")
    rotorD = Rotor(numeroRotorD, c3)

    cadena = input("Introduce una cadena de texto: ")

    #Cifrado de letras
    resultado = []
    doblepaso = False
    if (rotorC.clave ==rotorC.claveDesplazamiento):
        doblepaso = True
    for letra in cadena:
        cifrado = cifrarLetra(letra, rotorI.clave,rotorC.clave,rotorD.clave,rotorI.alfabetorotor, rotorC.alfabetorotor,rotorD.alfabetorotor)
        resultado.append(cifrado)

        rotorD.nextLetra()
        if (doblepaso):
            rotorC.nextLetra()
            doblepaso = False
            rotorI.nextLetra()
        if(rotorD.clave == rotorD.claveDesplazamiento):
            rotorC.nextLetra()
            if (rotorC.clave==rotorC.claveDesplazamiento):
                doblepaso = True





    print("Original: " + cadena)
    print("Cifrado: "+''.join(resultado))
    print("Nuevo Valor de las claves: "+rotorI.clave + rotorC.clave + rotorD.clave)

