#Skapa en version av det klassiska spelet Hangman.
# Datorn väljer ett slumpmässigt ord från en fördefinierad lista av ord.
# Spelet visar hur många bokstäver ordet består av, men inte vilka bokstäver som är rätt.
# Spelaren ska gissa en bokstav i taget, och datorn ger feedback om bokstaven finns i ordet eller inte.
# Spelet fortsätter tills spelaren har gissat hela ordet eller har gjort tillräckligt många felaktiga gissningar.


import random
from ordlista import ORD
    
def slumpa_ord():
    choise = random.choice(ORD)
    return choise


def visa_ord():
    valt_ord = slumpa_ord().lower()
    print ("TEST ",valt_ord)
    res = len(valt_ord)
    
# Huvudloop
    rakna_bokstav=0
    total_fel = 0
    max_fel= 5  
    redan_gissadord =""
    redan_gissade = ""
    
    while True:
        #print(f"\n Fel: {total_fel}/{max_fel}")
        print("Gissade bokstäver:", ", ".join(sorted(redan_gissade)) or "(0)")
        
   
        gissar = input("Gissa en bokstav (a-ö): ").strip().lower()

        # Kolla att användaren skrev exakt en bokstav
        if len (gissar) != 1 or not gissar.isalpha():
            
            total_fel += 1
            print ("Skrev exakt en bokstav === ", total_fel)

        # Kolla om bokstaven redan gissats
        elif gissar in redan_gissade:
            
            total_fel +=1
            print("Bokstaven redan gissad === ", total_fel)

        # Annars är gissningen giltig
        else:
            redan_gissade= redan_gissade + gissar

            if gissar in valt_ord:
                print("rätt gissat")

                antal = valt_ord.count(gissar)
                rakna_bokstav = rakna_bokstav+antal

            else:
                print("fel gissat")
                total_fel += 1
                print ("Fel gissat === ", total_fel)

#Om spelaren gör för många fel
        if total_fel  >= max_fel:
            print("Max chans görd =========================================\n")
            break

# Kontrollera om alla bokstäver i ordet är gissade
        if (rakna_bokstav == res): 
            print("\ngrattis du hittade rätt ord ====================== ",valt_ord) 
            break  

if __name__ == '__main__':   
    print("Välkomna") 
    print("Ordet består av bokstäver") 

    visa_ord() 

    #mainloop()