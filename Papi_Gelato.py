OpnieuwVragenStap1 = "True" 
OpnieuwVragenStap2 = "True"
OpnieuwVragenStap3 = "True"
print ("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
#Stap 1
while OpnieuwVragenStap1 == "True":
    HoeveelBolletjes = int(input("Hoeveel bolletjes wilt u? "))
    
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
                print ("Sorry, dat snap ik niet...")
    elif HoeveelBolletjes > 8:
        print ("Sorry, zulke grote bakken hebben we niet")
        
    else:
        print ("Sorry, dat snap ik niet...")
                #Stap 3
    while OpnieuwVragenStap3 == "True":
        NogMeerBestellen = input("Hier is uw " + HoorntjeOfBakje + " met "+ str(HoeveelBolletjes) +" bolletjes. Wilt u nog meer bestellen? (J/N) ")
        if NogMeerBestellen == "J":
            OpnieuwVragenStap1 = "True"
            OpnieuwVragenStap3 = "False"

        elif NogMeerBestellen == "N":
            print ("Bedankt en tot ziens!")
            OpnieuwVragenStap3 = "False"

        else:
            print ("Sorry dat snap ik niet")
            

        
    

   