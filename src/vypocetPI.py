#!/usr/bin/env python3
# Soubor:  vypocetPI.py
# Datum:   16.11.2017 12:51
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
# Licence: GNU/GPL
# Úloha:
#                  4   4   4   4
#         pi = 4 - - + - - - + - - ...
#                  3   5   7   9
#
############################################################################
try:
    print("3.1415926535897932384626433832795028841971")
    pi = 4
    print(pi, end='')
    znam = -1
    jmen = 3
    i = 1
    while 4/jmen > 1e-9:
        pi += znam * 4 / jmen
        jmen += 2
        znam *= -1
        i += 1
        if i > 100000:
            print("\r{}                                   ".format(pi), end='')
            i = 0
    print()

except KeyboardInterrupt:
    exit(1)
