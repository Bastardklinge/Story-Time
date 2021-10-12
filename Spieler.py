#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 09:09:46 2021

@author: moep
"""
import time
import random
import os
class Spieler:
    
    Ablauf = ['Zeit','Ort','Person','Tat','Zeuge','Kommentar']
    
    #Die Listen öffnen
    a = open ("Zeit.txt","r")
    a = a.read()
    b = open ("Ort.txt","r")
    b = b.read()
    c = open ("Person.txt","r")
    c = c.read()
    d = open("Tat.txt", "r")
    d = d.read()
    e = open("Zeuge.txt","r")
    e = e.read()
    f = open("Kommentar.txt","r")
    f = f.read()
    
    
    #Die Listen einbinden
    Zeit = a.split("\n")
    Ort = b.split ("\n")
    Person = c.split("\n")
    Tat = d.split("\n")
    Zeuge = e.split("\n")
    Kommentar = f.split("\n")
    
    #Leere Abschnitte entfernen
    if "" in Zeit:
        Zeit.remove("")
    if "" in Ort:
        Ort.remove("")
    if "" in Person:
        Person.remove("")
    if "" in Tat:
        Tat.remove("")
    if "" in Zeuge:
        Zeuge.remove("")
    if "" in Kommentar:
        Kommentar.remove("")
    
    def __init__(self, Name, Status):

        self.__name = Name
        self.__status = Status
        self.__liste = []
        self.Zeit = []
        self.Ort = []
        self.Person = []
        self.Tat = []
        self.Zeuge = []
        self.Kommentar = []

    
    def Eingabe (self, Teil):
               
        if Teil == "Zeit":
                
            self.Zeit.append(input("Gib einen Zeitpunkt an: "))
            f = open(self.__name+'_'+Teil+'.tmp','w')
            f.write(self.Zeit[0])
            f.close()
                
                        
        if Teil == "Ort":
            
            self.Ort.append(input("Gib einen Ort an: "))
            f = open(self.__name+'_'+Teil+'.tmp','w')
            f.write(self.Ort[0])
            f.close()
                    
        if Teil == "Person":
            
            self.Person.append(input("Gib eine Person an: "))
            f = open(self.__name+'_'+Teil+'.tmp','w')
            f.write(self.Person[0])
            f.close()
            
        if Teil == "Tat":
            
            self.Tat.append(input("Gib an, was eine Person getan hat: "))
            f = open(self.__name+'_'+Teil+'.tmp','w')
            f.write(self.Tat[0])
            f.close()
                        
        if Teil == "Zeuge":
            
            self.Zeuge.append(input("Gib an, wer das ganze bezeugt hat: "))
            f = open(self.__name+'_'+Teil+'.tmp','w')
            f.write(self.Zeuge[0])
            f.close()        
            
        if Teil == "Kommentar":
            
            self.Kommentar.append(input("Gib an, was zu dem ganzen kommentiert wurde: "))
            f = open(self.__name+'_'+Teil+'.tmp','w')
            f.write(self.Kommentar[0])
            f.close()     
            
            
    def Boteingabe (self, Teil):
        
            if Teil == "Zeit":
                
                Abschnitt = random.randrange(len(Spieler.Zeit))
                self.Zeit.append(Spieler.Zeit[Abschnitt])
                Spieler.Zeit.pop(Abschnitt)
                f = open(self.__name+'_'+Teil+'.tmp','w')
                f.write(self.Zeit[0])
                f.close()
                
                        
            if Teil == "Ort":
                
                Abschnitt = random.randrange(len(Spieler.Ort))
                self.Ort.append(Spieler.Ort[Abschnitt])
                Spieler.Ort.pop(Abschnitt)
                f = open(self.__name+'_'+Teil+'.tmp','w')
                f.write(self.Ort[0])
                f.close()
                    
            if Teil == "Person":
                
                Abschnitt = random.randrange(len(Spieler.Person))
                self.Person.append(Spieler.Person[Abschnitt])
                Spieler.Person.pop(Abschnitt)
                f = open(self.__name+'_'+Teil+'.tmp','w')
                f.write(self.Person[0])
                f.close()
                        
            if Teil == "Tat":
                
                Abschnitt = random.randrange(len(Spieler.Tat))
                self.Tat.append(Spieler.Tat[Abschnitt])
                Spieler.Tat.pop(Abschnitt)
                f = open(self.__name+'_'+Teil+'.tmp','w')
                f.write(self.Tat[0])
                f.close()
                        
            if Teil == "Zeuge":
                Abschnitt = random.randrange(len(Spieler.Zeuge))
                self.Zeuge.append(Spieler.Zeuge[Abschnitt])
                Spieler.Zeuge.pop(Abschnitt)
                f = open(self.__name+'_'+Teil+'.tmp','w')
                f.write(self.Zeuge[0])
                f.close()        
            
            if Teil == "Kommentar":
                
                Abschnitt = random.randrange(len(Spieler.Kommentar))
                self.Kommentar.append(Spieler.Kommentar[Abschnitt])
                Spieler.Kommentar.pop(Abschnitt)
                f = open(self.__name+'_'+Teil+'.tmp','w')
                f.write(self.Kommentar[0])
                f.close()        
        
            
    def Ausgabe (self):
        
        Spieler.liste = []
       
        for y in Spieler.Ablauf:
        
            x = open(self.__name+'_'+y+'.tmp','r')
            x = x.read()
            Spieler.liste.append(x)
            g = open(y+ ".txt","r")
            g = g.read()
            g = g.split("\n")
          
            if x not in g:
                f = open (y+".txt","a")
                f.write("\n"+x)
                f.close()
            
            os.remove(self.__name+"_"+y+".tmp")
            
        a = open("Gespeicherte Storys.txt","a")
        a.write("\n\n"+str(self.__name)+" hat folgende Geschichte: \n\n")
            
        print ("\n"+str(self.__name )+ " hat folgende Geschichte: \n\n")
        time.sleep(1)
            
        for x in Spieler.liste:
            a.write(x + "\n")
            print (x)
            time.sleep(1)
        
        time.sleep(2)
        a.close()
