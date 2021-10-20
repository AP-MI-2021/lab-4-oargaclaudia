def citireLista():
    l=[]
    listAsString=input("Dati lista ")
    numbersAsString=listAsString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l
def numereNegative(l):
    '''
    Afisarea tuturor numerelor negative nenule din lista
    :param l: o lista de numere intregi
    :return: o lista cu toate numerele negative nenule din lista l
    '''
    rezultat=[]
    for x in l:
        if x<0:
            rezultat.append(x)
    return rezultat
def testnumereNegative():
    assert numereNegative([-2,2,-3,0])==[-2,-3]
    assert numereNegative([])==[]
    assert numereNegative([-1,-2,-2])==[-1,-2,-2]

def main():
    l=[]
    testnumereNegative()
    while True:
        print("1. Citire lista")
        print("2. Afișarea tuturor numerelor negative nenule din listă")
        print("x. Iesire")
        optiune=input("Dati optiunea: ")
        if optiune=="1":
            l=citireLista()
        elif optiune=="2":
            print(numereNegative(l))
        elif optiune=="x":
            break
        else:
            print("Optiune invalida")
main()
