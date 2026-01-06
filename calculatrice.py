print("======================================== Calculatrice ========================================")

cont = True
while cont==True: 
    print()
    print("1 pour addition, 2 pour soustraction, 3 pour multiplication, 4 pour division, autre pour quitter : ")
    choix = int(input("Vous choisissez : "))
    liste = [1,2,3,4]

    if choix in liste:
        a = int(input("premier nombre ? : "))
        b = int(input("deuxième nombre ? : "))
        match choix:
            case 1:
                print("Le résultat est : ", a+b)
            case 2:
                print("Le résultat est : ", a-b)
            case 3:
                print("Le résultat est : ", a*b)
            case 4:
                print("Le résultat est : ", a/b)
        choix2=int(input("Voulez vous refaire un calcul ? 0 pour OUI, autre pour NON : "))
        if choix2!=0:
            cont=False

    if choix not in liste or not cont:
        print("FIN.")
        print("==============================================================================================")
        cont=False