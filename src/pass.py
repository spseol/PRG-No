#!/usr/bin/env python3
# Soubor:  pass.py
# Datum:   12.10.2017 13:18
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Popis:   Program kontroluje sílu hesla
############################################################################

heslo = input('zadej své heslo > ') 

MALA = 'qwertyuiopasdfghjklzxcvbnm'
VELKA = MALA.upper()
SPEC ='!@#$%^&*()[]{}\\|-+" \'~'
CISLA = '0123456789'

if len(heslo) < 8:
    print('heslo je příliš krátké')
    exit(1)

jeMALA = False
jeVELKA = False
jeSPEC = 0 
jeCISLA = 0
for znak in heslo:
    if znak in MALA:
        jeMALA = True
    jeVELKA = (znak in VELKA) or jeVELKA
    jeSPEC |=  znak in SPEC
    if znak in CISLA:
        jeCISLA = True

print(jeMALA, jeVELKA, jeSPEC, jeCISLA)
if jeMALA + jeVELKA + jeSPEC + jeCISLA >=3:
    print("Heslo je v pořádku")
    exit(0)
else:
    print("Heslo je příliš jednoduché")
    exit(3)

