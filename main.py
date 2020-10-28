





def caminoIda(letra, clave1, clave2, clave3):

    letra ="A"
    clave1=0
    clave2=0
    clave3=0


    clave3 +=1

    alfabeto=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    rotor3 = ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"]
    rotor2 = ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"]
    rotor1 = ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"]

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

    print(alfabeto[c])
    print(rotor3[c])
    print(offset3)
    print(alfabeto[d])
    print(rotor2[d])
    print(offset2)
    print(alfabeto[f])
    print(rotor1[f])
    print(offset1)

def getNumero(letra,alf):
    numero = 0
    for element in alf:
        if element == letra:
            return numero
        numero +=1
    return -1

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

    caminoIda(1,1,1,1)
