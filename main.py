import random
import string


def cifrarLetra(letra, c1, c2, c3, rotor3, rotor2, rotor1):
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
    return salida

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

def nextLetra(c1):
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
    aux = getNumero(c1, alfabeto)
    return alfabeto[(aux+1)%26]
if __name__ == '__main__':
    rotor3 = ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"] #INF
    rotor2 = ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"]
    rotor1 = ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"]



    cadena = "SEDUTPERSPICIATISUNDEOMNISISTENATUSERRORSITVOLUPTATEMACCUSANTIUMDOLOREMQUELAUDANTIUMTOTAMREMAPERIAMEAQUEIPSAQUAEABILLOINVENTOREVERITATISETQUASIARCHITECTOBEATAEVITAEDICTASUNTEXPLICABONEMOENIMIPSAMVOLUPTATEMQUIAVOLUPTASSITASPERNATURAUTODITAUTFUGITSEDQUIACONSEQUUNTURMAGNIDOLORESEOSQUIRATIONEVOLUPTATEMSEQUINESCIUNTNEQUEPORROQUISQUAMESTQUIDOLOREMIPSUMQUIADOLORSITAMETCONSECTETURADIPISCIVELITSEDQUIANONNUMQUAMEIUSMODITEMPORAINCIDUNTUTLABOREETDOLOREMAGNAMALIQUAMQUAERATVOLUPTATEMUTENIMADMINIMAVENIAMQUISNOSTRUMEXERCITATIONEMULLAMCORPORISSUSCIPITLABORIOSAMNISIUTALIQUIDEXEACOMMODICONSEQUATURQUISAUTEMVELEUMIUREREPREHENDERITQUIINEAVOLUPTATEVELITESSEQUAMNIHILMOLESTIAECONSEQUATURVELILLUMQUIDOLOREMEUMFUGIATQUOVOLUPTASNULLAPARIATURATVEROEOSETACCUSAMUSETIUSTOODIODIGNISSIMOSDUCIMUSQUIBLANDITIISPRAESENTIUMVOLUPTATUMDELENITIATQUECORRUPTIQUOSDOLORESETQUASMOLESTIASEXCEPTURISINTOBCAECATICUPIDITATENONPROVIDENTSIMILIQUESUNTINCULPAQUIOFFICIADESERUNTMOLLITIAANIMIIDESTLABORUMETDOLORUMFUGAETHARUMQUIDEMRERUMFACILISESTETEXPEDITADISTINCTIONAMLIBEROTEMPORECUMSOLUTANOBISESTELIGENDIOPTIOCUMQUENIHILIMPEDITQUOMINUSIDQUODMAXIMEPLACEATFACEREPOSSIMUSOMNISVOLUPTASASSUMENDAESTOMNISDOLORREPELLENDUSTEMPORIBUSAUTEMQUIBUSDAMETAUTOFFICIISDEBITISAUTRERUMNECESSITATIBUSSAEPEEVENIETUTETVOLUPTATESREPUDIANDAESINTETMOLESTIAENONRECUSANDAEITAQUEEARUMRERUMHICTENETURASAPIENTEDELECTUSUTAUTREICIENDISVOLUPTATIBUSMAIORESALIASCONSEQUATURAUTPERFERENDISDOLORIBUSASPERIORESREPELLAT"


    c1 = "O"
    c2 = "D"
    c3 = "L"
    resultado = []
    doblepaso = False
    for letra in cadena:
        cifrado = cifrarLetra(letra, c1,c2,c3,rotor3,rotor2,rotor1)
        resultado.append(cifrado)

        c3 = nextLetra(c3)
        if (doblepaso):
            c2 = nextLetra(c2)
            doblepaso = False
            c1 = nextLetra(c1)
        if(c3 == "V"):
            c2 = nextLetra(c2)
            if (c2=="E"):
                doblepaso = True





    print(cadena)
    print(''.join(resultado))
    print(c1 + c2 + c3)

