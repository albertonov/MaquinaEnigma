import random
import string


def cifrarLetra(letra, c1, c2, c3):
    alfabeto=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    rotor3 = ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"] #INF
    rotor2 = ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"]
    rotor1 = ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"]
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


    #print(alfabeto[offset1]+"->REFLECTOR"+"->"+reflecor[offset1])

    h = (getNumero(reflecor[offset1], alfabeto) +clave1)%26


    a = getNumero(alfabeto[h], rotor1)
    #print(rotor1[a] +"->"+alfabeto[a])

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
    print(letra + "->" + salida)

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

    for x in range(6):
        letra = random.choice(string.ascii_letters).upper()
        c1 = random.choice(string.ascii_letters).upper()
        c2 = random.choice(string.ascii_letters).upper()
        c3 = random.choice(string.ascii_letters).upper()
        print(letra+c1+c2+c3)
        cifrarLetra(letra,c1,c2,c3)
        print("------------")