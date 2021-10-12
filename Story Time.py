#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 08:32:43 2021

@author: moep
"""

import sys
import random
import time
import Spieler
import names


Alphabet = ['a','b','c','d','e','f']
Ablauf = ['Zeit','Ort','Person','Tat','Zeuge','Kommentar']


def Einstellungen():
    
    print("Stell zunächst ein, wie viele Spieler und wie viele Bots mitspielen. \n")
    n = int(input("Wie viele Spieler? "))


    for x in range(n):
        x+=1
        print('Spieler '+str(x)+", gib hier deinen Namen ein:")
        Spielerliste.append([input(),"Mensch"])

    m = int(input("Wie viele Bots? "))

    for i in range(m):
        bots.append([names.get_first_name(),"bot"])

    print("Du spielst mit: \n")

    for i in bots:
        print(i[0])
    
        if Spielerliste == []:
            Spielerliste.append(i)
    
        else:
            Spielerliste.insert(random.randrange(len(Spielerliste)),i)
    
    Spiel()
    
def Spiel():    

    time.sleep(1)

    for x in Spielerliste:
    
        if x[1] == "Mensch":
    
            print(str(x[0])+' gibt jetzt ein: \n')
    
            y = Spielerliste.index(x)   
            t = 0    
                
            while t < 6:
          
                if y >= len(Spielerliste):
                    y -= len(Spielerliste)
    
                z = Ablauf[t]
                f = Spielerliste[y]
                print(f)
                g = Spieler.Spieler(f[0],f[1])
            
                print(f[0])
                print(f[1])
           
                g.Eingabe(z)
                y += 1
                t += 1
            
            
        if x[1] == "bot":
        
            print(str(x[0])+' gibt jetzt ein: ')
    
            y = Spielerliste.index(x)   
            t = 0    
                
            while t < 6:
          
                if y >= len(Spielerliste):
                    y -= len(Spielerliste)
    
                z = Ablauf[t]
                f = Spielerliste[y]
                g = Spieler.Spieler(f[0],f[1])
            
                g.Boteingabe(z)        
   
                y += 1
                t += 1
     
    for x in Spielerliste:
        z = Spieler.Spieler(x[0],x[1])
        z.Ausgabe()

    a = int(input("\n Möchtest du... \n 1. ...noch eine Runde spielen? \n 2. ...die Spieler ändern? \n 3. ...beenden? \n\n"))
    
    if a == 1:
        Spiel()
        
    if a == 2:
        Einstellungen()

    if a == 3:
        sys.exit("Bis dann! ")        

Spielerliste = []
bots = []
print("It's Storytime! \n")
time.sleep(1)
Einstellungen()
