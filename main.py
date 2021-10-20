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
def celMaiMicNr(l,c):
    '''
    Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    :param l: o lista de numere intregi
    :param c: o cifra citita de la tastatura
    :return: None, daca niciun nr nu are ultima cifra c. Altfel, returneaza cel mai mic nr care are ult cif egeala cu c
    '''
    ok=0
    for x in l:
        if x%10==c:
            if ok==0:
                min=x
                ok=1
            elif x<min:
                min=x
    if ok==0:
        return None
    return min

def testcelMaiMicNr():
    assert celMaiMicNr([1, 6, 34, 68, 40, 48, 20],8)==48
    assert celMaiMicNr([1,12,22],3)==None
    assert celMaiMicNr([1,11,21,2,222],2)==2
def is_prime(n):
    '''
    Determina daca un numar natural este prim
    :param n: un numar natural
    :return: True, daca numarul este prim. Returneaza False in caz contrar
    '''
    if n<2:
      return False
    if n==2:
      return True
    for i in range(2,n//2+1):
      if n%i==0:
        return False
    return True
def test_is_prime():
    assert is_prime(2)==True
    assert is_prime(3)==True
    assert is_prime(4)==False
def is_superprime(n):
    '''
    Determina daca un numar este superprim
    :param n: un numar natural citit de la tastatura
    :return: True, daca numarul citit de la tastatura este superprim. False, in caz contrar.
    '''
    if n<2:
        return False
    while n!=0:
        if is_prime(n)==False:
            return False
        else:
            n=n//10
    return True
def test_is_superprime():
    assert is_superprime(15)==False
    assert is_superprime(101)==False
    assert is_superprime(233)==True
    assert is_superprime(237)==False
def listaSuperPrime(l):
    '''
    Afișarea tuturor numerelor din listă care sunt superprime.
    :param l: o lista de numere
    :return: o noua lista cu numerele superprime
    '''
    rezultat=[]
    for x in l:
        if x>0 and is_superprime(x):
            rezultat.append(x)
    return rezultat
def testlistaSuperPrime():
    assert listaSuperPrime([123,233])==[233]
    assert listaSuperPrime([])==[]
    assert listaSuperPrime([123,173,239])==[239]
def main():
    l=[]
    testcelMaiMicNr()
    testnumereNegative()
    test_is_prime()
    test_is_superprime()
    testlistaSuperPrime()
    while True:
        print("1. Citire lista")
        print("2. Afișarea tuturor numerelor negative nenule din listă")
        print("3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
        print("4. Afișarea tuturor numerelor din listă care sunt superprime.")
        print("x. Iesire")
        optiune=input("Dati optiunea: ")
        if optiune=="1":
            l=citireLista()
        elif optiune=="2":
            print(numereNegative(l))
        elif optiune=="3":
            c=int(input("Dati cifra de la tastatura: "))
            if celMaiMicNr(l,c)==None:
                print("Niciun numar nu are ultima cifra data")
            else:
                print(celMaiMicNr(l,c))
        elif optiune=="4":
            print(listaSuperPrime(l))
        elif optiune=="x":
            break
        else:
            print("Optiune invalida")
main()
