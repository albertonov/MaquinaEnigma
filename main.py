from Rotor import Rotor


def cifrarLetra(letra, rotorI, rotorC, rotorD, listaLetrasClavija, listaTuplasClavijero):
    alfabeto=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    reflecor=["Y", "R", "U", "H", "Q", "S", "L", "D", "P", "X", "N", "G", "O", "K", "M", "I", "E", "B", "F", "Z", "C", "W", "V", "J", "A", "T"]

    inputChar = letra
    rotor1 = rotorI.alfabetorotor
    rotor2 = rotorC.alfabetorotor
    rotor3 = rotorD.alfabetorotor


    clave1= getNumero(rotorI.clave,alfabeto)
    clave2= getNumero(rotorC.clave,alfabeto)
    clave3= getNumero(rotorD.clave,alfabeto)



    #CLAVIJERO ENTRADA
    inputChar = checkLetraInClavijero(inputChar, listaLetrasClavija, listaTuplasClavijero)





    #del input al tercer rotor
    clave3 += 1
    a = getNumero(inputChar, alfabeto)                  #r18
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


    offset3 = clave3-clave2
    if(offset3<0):
        offset3 = offset3 +26
    d = (c + offset3)%26
    e = getNumero(alfabeto[d], rotor3)

    offsetOutput = getOffset(clave3, alfabeto[e])

    salida = alfabeto[offsetOutput]

    salida = checkLetraInClavijero(salida, listaLetrasClavija, listaTuplasClavijero)

    #CLAVIJERO SALIDA
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

def checkLetraInClavijero(letra, listaLetrasClavija, listaTuplasClavijero):
    if (letra in listaLetrasClavija):
        for tupla in listaTuplasClavijero:
            if letra in tupla:
                if letra == tupla[0]:
                    letra = tupla[1]
                else:
                    letra = tupla [0]
    return letra


if __name__ == '__main__':
    ##################### INTRODUCCION DE DATOS #################################
    numeroRotorI = int(input("¿Que rotor ira en el lado izquierdo? (1, 2, 3): "))
    c1 = input("Introduce la clave rotor izquierda (Letra): ")
    rotorI = Rotor(numeroRotorI, c1.upper())


    numeroRotorC = int(input("¿Que rotor ira en el lado central? (1, 2, 3): "))
    c2 = input("Introduce la clave rotor central (Letra): ")
    rotorC = Rotor(numeroRotorC, c2.upper())

    numeroRotorD = int(input("¿Que rotor ira en el lado derecho? (1, 2, 3): "))
    c3 = input("Introduce la clave rotor derecho (Letra): ")
    rotorD = Rotor(numeroRotorD, c3.upper())

    clavijaSalida = False
    listaLetrasClavija = []
    listaTuplasClavijero = []
    while(not clavijaSalida):
        entrada = input("Clavijero: Introduce dos letras separadas por un guion (A-B). (ESC para terminar de introducir): ")
        if entrada == "ESC":
            clavijaSalida = True
        else:
            l1 = entrada[0]
            l2 = entrada[2]
            if l1 in listaLetrasClavija or l2 in listaLetrasClavija:
                print("Esta letra ya esta introducida!")
            else:
                listaLetrasClavija.append(l1)
                listaLetrasClavija.append(l2)
                listaTuplasClavijero.append((l1, l2))
                a = 0

    cadena = input("Introduce una cadena de texto: ")





    ##################### CIFRADO DE LETRAS #################################
    resultado = []
    doblepaso = False
    if (rotorC.clave ==rotorC.claveDesplazamiento):
        doblepaso = True
    for letra in cadena:
        cifrado = cifrarLetra(letra, rotorI,rotorC,rotorD, listaLetrasClavija, listaTuplasClavijero)
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

