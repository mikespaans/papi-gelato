def SorrySnapIkNiet():
    print ("Sorry, dat snap ik niet...")
OpnieuwVragenStap1 = "True" 
OpnieuwVragenStap2 = "True"
OpnieuwVragenStap3 = "True"
OnpieuwVragenSmaken = "True"
OpnieuwVragenToppings = "True"
NummerBolletje = 1
NummerBakjes = 0
NummerHoorntjes = 0
TotaalBolletjes = 0
TotaalSlagroom = 0
ToppingSlagroom = 0
ToppingSprinkels = 0
ToppingCaramel = 0
ToppingGeen = 0
AantalToppings = 0
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
        for i in range (int(HoeveelBolletjes)):
            WatVoorTopping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus ")
            if WatVoorTopping == "B":
                ToppingSlagroom += 1
                AantalToppings += 1
            elif WatVoorTopping == "C":
                ToppingSprinkels += 1
                AantalToppings += 1
            elif WatVoorTopping == "D":
                ToppingCaramel += 1
                AantalToppings += 1
            elif WatVoorTopping == "A":
                ToppingGeen += 1
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
                OpnieuwVragenStap3 = "False"
                PrijsBolletjes = float(TotaalBolletjes) * 1.10
                PrijsHoorntje = float(NummerHoorntjes) * 1.25
                PrijsBakje = float(NummerBakjes) * 0.75
                PrijsSprinkels = ToppingSprinkels * 0.30
                if HoorntjeOfBakje == "hoorntje":
                    ToppingCaramel * 0.60
                elif HoorntjeOfBakje == "bakje":
                    ToppingCaramel * 0.90
                if ToppingSlagroom >= 1:
                    TotaalSlagroom = 0.50
                TotaalTopping = TotaalSlagroom + ToppingCaramel + PrijsSprinkels
                TotaalPrijs = PrijsBolletjes + PrijsHoorntje + PrijsBakje + TotaalTopping
                

                print ('---------["Papi Gelato"]---------')
                print (" ")
                print ("Bolletje(s)       ",int(TotaalBolletjes), " * 1.10  =",PrijsBolletjes)
                if NummerHoorntjes >= 1:
                    print ("Hoorntje(s)       ",int(NummerHoorntjes)," * 1.25 = ", PrijsHoorntje )
                if NummerBakjes >= 1:
                    print ("Bakje(s)          ", int(NummerBakjes)," * 0.75 = ", PrijsBakje)
                if AantalToppings >= 1:
                    print ("Toppings           1  *",TotaalTopping," = " , TotaalTopping )
                print ("                              -------- +")
                print ("Totaal                          ",TotaalPrijs)
                print ("Bedankt en tot ziens!")

            else:
                SorrySnapIkNiet()
    else:
        SorrySnapIkNiet()