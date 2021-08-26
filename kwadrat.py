# -*- coding: utf-8 -*-
from turtle import *
import time

#################################
# przepis na rysowanie kwadratu #
#################################
def kwadrat(krok = 1):
    right(90)      # obróć się na rogu kwadratu o 90 stopni
    forward(100)   # narysuj bok o długości 100 pikseli

    if krok == 4:  # po narysowaniu kwadratu w 4 krokach
        return     # zakończ rysowanie

    kwadrat(krok + 1) # wykonaj kolejny krok rekurencji


##########################
# wykorzystanie przepisu #
##########################

# narysuj kwadrat
kwadrat()

# zaczekaj 10 sekund zanim obraz zgaśnie
time.sleep(10)
