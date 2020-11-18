import itertools
from main import  *






if __name__ == '__main__':


    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    diccionario = ["AMBIGUO", "OBVIO", "TRIVIAL", "ESTUPENDO", "ESTHER", "LECHUGA", "LUGAR", "PACIFICO", "PRIMERA", "HOLA", "MUNDO", "SEÑORA", "CALABAZA", "HERPES", "CELULA", "PORRO", "SUAVES", "ALBACETE", "FIESTA", "PATATA"]


    combinationLetters  = itertools.combinations(alfabeto, 2)#Obtener todas las combinaciones de dos letras sin repeticion

    pairsLetters = []

    for comb in combinationLetters:     #Pasar a lista todas las combinaciones
        a = []
        a.append(comb)
        pairsLetters.append(a)
        a=[]

    cifrado = []
    posiblesSoluciones=[]
    mensaje = "MSZXNXFPYDMHOVZWJZIRWULDGSDHUIPAERZLGOFFPBOVILGTIQJHUTNTSZCCBNCLLATPNLGIAJWJ"
    i = 0
    for c1 in alfabeto:
        for c2 in alfabeto:
            for c3 in alfabeto:
                for pares in pairsLetters:
                    par = pares[0]                                          # Solo para que la estructura de datos coincida con el programa original
                    listaLetrasClavija = [par[0], par[1]]                   # Idem
                    listaTuplasClavijero = pares                        # Idem
                    for letra in mensaje:
                        cifrado.append(cifrarLetra(letra, Rotor(1, c1), Rotor(2, c2), Rotor(3, c3), listaLetrasClavija, listaTuplasClavijero))
                        cadena = "".join(cifrado)
                    #print(str(i) + c1 + c2 + c3 + par[0] + par[1] + ":  " + "".join(cifrado))
                    for termino in diccionario:                             #Comprobar si el mensaje cifrado tiene un termino del diccionario
                        if termino in cadena:
                            i += 1
                            print(str(i) + c1 + c2 + c3 + par[0] + par[1]  +":  "+ "".join(cifrado))
                            posiblesSoluciones.append(cifrado)
                    cifrado = []                                            #Limpiar la cadena donde se almacena el cifrado






