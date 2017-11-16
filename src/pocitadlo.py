#!/usr/bin/env python3
# Datum:   02.11.2017 13:13
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Popis:   počítá výskyty znaků v textu
############################################################################
import sys
# nejdřiv se naučíme pracovat se slovnikem
"""
slovnik = {}             # prazdny slovnik
slovnik[1] = 'cilo'
slovnik['slovo'] = 'retezec'
slovnik[3.1415927] = 'realne cislo'

for k in slovnik.keys():
    print(k, "->", slovnik[k])

# print(slovnik['abc'])
print(slovnik.get('abc'))
"""


# text = input('zadej mi sem text >>> ')
with open('input.txt') as f:
    text = f.read()

pocitadlo = {}
for c in text:
    if c < 'A' or c > 'Z':
        continue  # cykluv v tomto místě skočí na další obrátku
    c = c.upper()
    if pocitadlo.get(c):  # klič existuje
        pocitadlo[c] += 1
    else:                 # klič neexistuje
        pocitadlo[c] = 1

maximum = max(pocitadlo.values())

for k in sorted(pocitadlo.keys()):
    print(k, ":",
          "{:10d}".format(pocitadlo.get(k)),
          '#' * (30 * pocitadlo[k]//maximum))
