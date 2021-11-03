def SorrySnapIkNiet():
    print ("Sorry, dat snap ik niet...")
OpnieuwVragenStap1 = "True" 
OpnieuwVragenStap2 = "True"
OpnieuwVragenStap3 = "True"
OnpieuwVragenSmaken = "True"
NummerBolletje = 1
NummerBakjes = 0
NummerHoorntjes = 0
TotaalBolletjes = 0
print ("Welkom bij Papi Gelato.")
#Stap 1
while OpnieuwVragenStap1 == "True":
    HoeveelBolletjes = input("Hoeveel bolletjes wilt u? ")
    GetalOfWoord = HoeveelBolletjes.isdigit()
    OpnieuwVragenStap3 = "True"
    TotaalBolletjes += int(HoeveelBolletjes)
    NummerBolletje = 1
    if GetalOfWoord == True:
        while OnpieuwVragenSmaken == "True":
            for i in range (int(HoeveelBolletjes)):
                SmaakBolletje = input("Welke smaak wilt u voor bolletje nummer " + str(NummerBolletje) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
                NummerBolletje = NummerBolletje + 1
                if SmaakBolletje == "A" or SmaakBolletje == "C" or SmaakBolletje == "M" or SmaakBolletje == "V":
                    OnpieuwVragenSmaken = "False"
                else:
                    SorrySnapIkNiet()
        
        if int(HoeveelBolletjes) <= 8 and int(HoeveelBolletjes) >= 4:
            OpnieuwVragenStap1 = "False"
            print ("Dan krijgt u van mij een bakje met",HoeveelBolletjes,"bolletjes")
            HoorntjeOfBakje = 'Bakje'
            NummerBakjes += 1

        elif int(HoeveelBolletjes) <= 3:
            OpnieuwVragenStap1 = "False"
            #Stap 2
            while OpnieuwVragenStap2 == "True":
                BakjeOfHoorntje = input("Wilt u deze "+ str(HoeveelBolletjes) +  " bolletje(s) in A) een hoorntje of B) een bakje? ")
                if BakjeOfHoorntje == "A" or BakjeOfHoorntje == "B":
                    OpnieuwVragenStap2 = "False"
                    
                    if BakjeOfHoorntje == "A":
                        HoorntjeOfBakje = 'hoorntje'
                        NummerHoorntjes += 1
                    else:
                        HoorntjeOfBakje = 'bakje'
                        NummerBakjes += 1
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
                OnpieuwVragenSmaken = "True"

            elif NogMeerBestellen == "N":
                print ("Bedankt en tot ziens!")
                OpnieuwVragenStap3 = "False"
                PrijsBolletjes = float(TotaalBolletjes) * 1.10
                PrijsHoorntje = float(NummerHoorntjes) * 1.25
                PrijsBakje = float(NummerBakjes) * 0.75
                TotaalPrijs = PrijsBolletjes + PrijsHoorntje + PrijsBakje

                print ('---------["Papi Gelato"]---------')
                print (" ")
                print ("Bolletje(s)       ",int(TotaalBolletjes), " * 1.10  = " ,PrijsBolletjes)
                if NummerHoorntjes >= 1:
                    print ("Hoorntje(s)       ",int(NummerHoorntjes)," * 1.25 = ", PrijsHoorntje )
                if NummerBakjes >= 1:
                    print ("Bakje(s)          ", int(NummerBakjes)," * 0.75 = ", PrijsBakje)
                print ("                              -------- +")
                print ("Totaal                          ",TotaalPrijs)

            else:
                SorrySnapIkNiet()
    else:
        SorrySnapIkNiet()