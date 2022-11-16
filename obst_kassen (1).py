#!/usr/bin/env python
# coding: utf-8

# In[7]:


aepfel_im_lager = 20
birnen_im_lager = 10
bananen_im_lager = 5

bestell_aepfel = 0
bestell_birne = 0
bestell_bananen = 0

preis_aepfel = 1
preis_birne = 0.50
preis_bananen = 0.70

summe = 0.0
geld = 0.0
rueckgeld = 0.0

print ("Kasse Obstladen")
print ("               ")

bestell_aepfel = int(input("Wie viel Äpfel hätten Sie gern: "))
if bestell_aepfel <= aepfel_im_lager:
    print(bestell_aepfel, "sind jetzt im Warenkorb ")
else:
    print(" Tut mir leid , wir haben nicht mehr genug im Lager")

print()
    
bestell_birne = int(input("Wie viel Birne hätten Sie gern: "))
if bestell_birne <= birnen_im_lager:
    print(bestell_birne, "sind jetzt im Warenkorb ")
else:
    print(" Tut mir leid , wir haben nicht mehr genug im Lager")
print()

bestell_bananen = int(input("Wie viel Banane hätten Sie gern: "))
if bestell_bananen <= bananen_im_lager:
    print(bestell_bananen, "sind jetzt im Warenkorb ")
else:
    print(" Tut mir leid , wir haben nicht mehr genug im Lager")

summe = (bestell_aepfel * preis_aepfel) + (bestell_birne * preis_birne) + (bestell_bananen * preis_bananen)
print()
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print()
print("Ihre Gesamtbetrag ist :           EUR", "%.2f" % summe)
print()

geld = float(input("Mit wie viel Geld werden sie bezahlen: "))
print()

rueckgeld = geld - summe
while True:
    if geld < summe:
        print("Bitte mehr geld reinzufügen")
        geld = float(input("Mit wie viel Geld werden sie bezahlen: "))
    else:
        print("Sie Bekommen", "%.2f" % rueckgeld, "EUR")
        break

'''print("Sie Bekommen", "%.2f" % rueckgeld, "EUR")'''
print()
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print()

print("Vielen Dank für Ihreren Einkauf :D")


# 
