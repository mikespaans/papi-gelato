def SorrySnapIkNiet():
    print ("Sorry, dat snap ik niet...")
OpnieuwVragenStap1 = "True" 
OpnieuwVragenStap2 = "True"
OpnieuwVragenStap3 = "True"
OnpieuwVragenSmaken = "True"
NummerBolletje = 1
print ("Welkom bij Papi Gelato.")
#Stap 1
while OpnieuwVragenStap1 == "True":
    HoeveelBolletjes = int(input("Hoeveel bolletjes wilt u? "))
    while OnpieuwVragenSmaken == "True":
        for i in range (HoeveelBolletjes):
            SmaakBolletje = input("Welke smaak wilt u voor bolletje nummer " + str(NummerBolletje) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
            NummerBolletje = NummerBolletje + 1
            if SmaakBolletje == ("A" or "C" or "M" or "V"):
                OnpieuwVragenSmaken = "False"
            else:
                SorrySnapIkNiet()
    OpnieuwVragenStap3 = "True"
    
    if HoeveelBolletjes <= 8 and HoeveelBolletjes >= 4:
        OpnieuwVragenStap1 = "False"
        print ("Dan krijgt u van mij een bakje met",HoeveelBolletjes,"bolletjes")
        HoorntjeOfBakje = 'Bakje'

    elif HoeveelBolletjes <= 3:
        OpnieuwVragenStap1 = "False"
        #Stap 2
        while OpnieuwVragenStap2 == "True":
            BakjeOfHoorntje = input("Wilt u deze "+ str(HoeveelBolletjes) +  " bolletje(s) in A) een hoorntje of B) een bakje? ")
            if BakjeOfHoorntje == ("A" or "B"):
                OpnieuwVragenStap2 = "False"
                
                if BakjeOfHoorntje == "A":
                    HoorntjeOfBakje = 'hoorntje'
                else:
                    HoorntjeOfBakje = 'bakje'
            else:
                SorrySnapIkNiet()
    elif HoeveelBolletjes > 8:
        print ("Sorry, zulke grote bakken hebben we niet")
        
    else:
        SorrySnapIkNiet()
                #Stap 3
    while OpnieuwVragenStap3 == "True":
        NogMeerBestellen = input("Hier is uw " + HoorntjeOfBakje + " met "+ str(HoeveelBolletjes) +" bolletjes. Wilt u nog meer bestellen? (J/N) ")
        
        if NogMeerBestellen == "J":
            OpnieuwVragenStap1 = "True"
            OpnieuwVragenStap2 = "True"
            OpnieuwVragenStap3 = "False"

        elif NogMeerBestellen == "N":
            print ("Bedankt en tot ziens!")
            OpnieuwVragenStap3 = "False"

        else:
            SorrySnapIkNiet()