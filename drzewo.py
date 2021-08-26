# -*- coding: utf-8 -*-
from turtle import *
import time

###############################
# przepis na rysowanie drzewa #
###############################
def drzewo(dlugosc, krok = 1):
    # warunek zakończenia rekurencji po 8 krokach
    if krok == 8:
        return

    # narysowanie pnia
    forward(dlugosc)

    # rekurencyjne rysowanie kolejnych rozgałęzień,
    # które z każdym krokiem są o 20% krótsze

    # najpierw skręt w prawo i rysowanie prawej gałęzi
    right(30)
    drzewo(0.8 * dlugosc, krok+1)

    # potem skręt w lewo i rysowanie lewej gałęzi
    left(60)
    drzewo(0.8 * dlugosc, krok+1)

    # powrót żółwia do miejsca rozwidlenia gałęzi
    right(30)
    backward(dlugosc)


##########################
# wykorzystanie przepisu #
##########################

# ustawienie prędkości żółwia w skali 0-10
speed(10)

# obrót żółwia tak, aby miał głowę w górę
# i zaczął od narysowania pionowego pnia
left(90)
backward(100)

# rysowanie wg przepisu na drzewo
# zaczynając od pnia długości 100 pikseli
drzewo(100)

# zaczekaj 10 sekund zanim obraz zgaśnie
time.sleep(10)
