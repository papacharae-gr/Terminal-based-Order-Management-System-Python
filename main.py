

trapezi = int(input("Τραπέζι Παραγγελίας:"))  #to programma zitaei apo to xristi na eisagei ton arithmo tou trapeziou kai to apothikevei sti metavliti trapezi



print("Επιλογές:\n---------") #tiponei ti lexi epiloges

name = ["Chicken Burger", "Ham Burger", "Green Burger", "Club Sandwich", "Σαλάτα ceasar’s", "Κινόα με Λαχανικά"] #lista me ta onomata ton proionton

description = ["Burger με κοτόπουλο, bacon, τυρί edam, τομάτα, μαρούλι με μαγιονέζα",
               "Burger με μπιφτέκι, τυρί, κέτσαπ, μουστάρδα",
               "Burger με ζουμερό μπιφτέκι, τυρί, φρέσκια τομάτα, μαρούλι, κρεμμύδι, πίκλες, κέτσαπ και dressing sauce",
               "Club sandwich με 3 πλούσιες στρώσεις Philadelphia σε φρυγανισμένο ψωμί του τοστ με ζουμερό κοτόπουλο φιλέρο, bacon, τομάτα, μαρούλι και τηγανητές πατάτες",
               "Δροσερή πράσινη σαλάτα με ζουμερό κοτόπουλου σε βάση μαρουλιού, με καλαμπόκι, κρουτόν, τριμμένο τυρί και vinaigreve ελαιόλαδου",
               "Δροσερή σαλάτα με κινόα, κόκκινη πιπεριά, τοματίνια, αγγούρι, δυόσμο, φρέσκο μαϊντανό και sauce λαδολέμονο"] #lista me tis perigrafes kathe proiontos

price = [4.20, 2.85, 4.20, 10.90, 6.90, 6.30] #lista me tis times ton proionton

order_choice = [] #keni lista opou tha apothikeutoun oi epiloges proionton tou xristi

order_cost = [] #keni lista pou tha apothikeutoun oi times ton proionton p epelexe o xristis

posotita_list = [] #keni lista opou tha apothikeutei i posotita pou epithimei o xristis

axia = [] #keni opou tha apothikeutei i axia tis paragelias

posotita = 0 #metavliti pou tha apothikeutei i posotita me arxiki timi 0

total_order = [] #lista pou tha apothikeutei i paragelia



def epiloges():     #dilosi sinartisis me tis epiloges tou programmatos
    print("[1] Έναρξη Παραγγελίας")
    print("[2] Εμφάνιση Παραγγελίας")
    print("[3] Αφαίρεση προιόντος από την παραγγελία")
    print("[4] Πληρωμή")
    print("[5] Έξοδος")


def menu():     #dilosi sinartisis me tis epiloges ton proionton pou exei o xristis
    print("Επιλογή #0: Chicken Burger")
    print("Επιλογή #1: Ham Burger")
    print("Επιλογή #2: Green Burger")
    print("Επιλογή #3: Club Sandwich")
    print("Επιλογή #4: Σαλάτα ceasar’s")
    print("Επιλογή #5: Κινόα με Λαχανικά")


option = 10 #dilosi metavlitis option kai arxikopoiisi me tixaia timi != 0

while option !=0:

    epiloges() #emfanisi tou menou epiloges
    option = int(input("Παρακαλώ εισάγετε την επιλογή σας:")) #o xristis eisagi tin epilogi tou apo to menu epilogon
    quest = "α"     #arxikopoiisi tis metavlitis quest me mia tixaia timi oste na einai alithis

    while quest != "ο":  #alithis while gia na ektelestei o akolouthos kodikas

        if option == 1: #1i epilogi tou menu
            menu()
            proion = int(input("Εισάγετε τον αριθμό προϊόντος από το μενού:"))


            if proion == 0:  #sinthiki pou eisagei sti lista ta proionta analoga me tin eisagogi tou xristi
                order_choice.append(name[0])
                order_cost.append(price[0])


            elif proion == 1:
                order_choice.append(name[1])
                order_cost.append(price[1])


            elif proion == 2:
                order_choice.append(name[2])
                order_cost.append(price[2])


            elif proion == 3:
                order_choice.append(name[3])
                order_cost.append(price[3])


            elif proion == 4:
                order_choice.append(name[4])
                order_cost.append(price[4])


            elif proion == 5:
                order_choice.append(name[5])
                order_cost.append(price[5])


            else:
                print("Αυτή η επιλογή δεν υπάρχει στο μενού")

            posotita = int(input("Εισάγετε ποσότητα:"))
            posotita_list.append(posotita)
            axia = axia + [price[proion] * posotita]
            #axia = axia + (price[proion] * posotita)
            total_order = order_choice,posotita_list,order_cost,axia


            quest = str(input("Επιθυμείτε να εισάγετε άλλο (ν/ο): "))





        elif option == 2: #deuteri epologi menu

            i = 0

            print("{:<3s}{:<20s}{:<5s}{:<8s}{:<8s}".format("α/α", "  ΟΝΟΜΑ", "ΤΜΧ", "ΤΙΜΗ", "ΑΞΙΑ"))
            print("-" * 45)

            # Tiponei ta stoixia tis listas order_choice
            for i in range(len(order_choice)):
                print("{:<3d}{:<20s}{:<5d}{:<8.2f}{:<8.2f}".format(i + 1, order_choice[i], posotita_list[i],order_cost[i], axia[i]))


            break


        elif option == 3: #epilogi 3 tou menu

            i = 0

            print("{:<3s}{:<20s}{:<5s}{:<8s}{:<8s}".format("α/α", "  ΟΝΟΜΑ", "ΤΜΧ", "ΤΙΜΗ", "ΑΞΙΑ"))
            print("-" * 45)


            for i in range(len(order_choice)):
                print("{:<3d}{:<20s}{:<5d}{:<8.2f}{:<8.2f}".format(i + 1, order_choice[i], posotita_list[i],order_cost[i], axia[i]))

            afairesi_proiontos = int(input("Επιλέξτε γραμμή προϊόντος προς αφαίρεση:"))
            quest_2 = str(input("Παρακαλώ επιβεβαιώστε την αφαίρεση (ν/ο)"))

            if quest_2 == "ν":

                if afairesi_proiontos >= 0 and afairesi_proiontos < len(order_choice): #diagrafi proionton simfona me tin eisagogi xristi
                    order_choice.pop(afairesi_proiontos)
                    posotita_list.pop(afairesi_proiontos)
                    order_cost.pop(afairesi_proiontos)
                    axia.pop(afairesi_proiontos)

                else:
                    print("Μη Έγγυρη Επιλογή!")

                    break


            else:

                break

            print("Το προϊόν αφαιρέθηκε επιτυχώς από το καλάθι αγορών.")
            break



        elif option == 4:

            i = 0

            print("{:<3s}{:<20s}{:<5s}{:<8s}{:<8s}".format("α/α", "  ΟΝΟΜΑ", "ΤΜΧ", "ΤΙΜΗ", "ΑΞΙΑ"))
            print("-" * 45)

            # Print the order details
            for i in range(len(order_choice)):
                print("{:<3d}{:<20s}{:<5d}{:<8.2f}{:<8.2f}".format(i + 1, order_choice[i], posotita_list[i],order_cost[i], axia[i]))

            quest_3 = str(input("Παρακαλώ επιβεβαιώστε την αγορά (ν/ο):"))

            if quest_3 == "ν":
                sinoliki_axia = sum(axia)
                print("Παρακαλούμε πληρώστε ",sinoliki_axia)
                quest_4 = str(input("Μετρητά ή κάρτα (μ/κ):"))

                if quest_4 == "μ":
                    poso = float(input("Εισάγετε αριθμό χρημάτων:"))

                    resta = 0
                    for a in axia:
                        r = sinoliki_axia - poso
                        apoliti_timi_resta = abs(r)
                        resta = apoliti_timi_resta


                    print("Τα ρέστα που πρέπει να δώσετε στον πελάτη είναι:",resta,"€")
                    print("Σας ευχαριστούμε για την αγορά σας!")

                elif quest_4 == "κ":

                    print("Σας ευχαριστούμε για την αγορά σας!")
                    break

                else:
                    break

            break

        elif option == 5:
            print("Thank you for using my app!")
            exit()


        else:
            print("Μη Έγγυρη Επιλογή!")
            break



