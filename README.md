# Story-Time
Ein kleines, jedoch witziges Partyspiel, in Python programmiert.
Autor: Robin Gilbert
_______________________________________________________________________

0. Notwendige Module:

import sys
import random
import time
import names
import os


1. Grundidee: 
Das Spiel basiert auf einem Partyspiel, bei dem nach einer festen Reihenfolge
verschiedene Abschnitte einer Geschichte auf ein Blatt Papier geschrieben,
umgefaltet und zum Nachbarn weitergereicht werden. Daraus ergeben sich pro
Mitspieler verschiedene und sehr unterhaltsame Geschichten. Das Format der 
Storys ist wie folgt:

Zu [jener Zeit ],
an [jenem Ort]
hat [diese Person]
[etwas] getan.
[Jemand anderes] hat es gesehen
und [reagierte].

Eine daraus resultierende Geschichte könnte wie folgt aussehen:

Am verkaterten Morgen danach
im Stall von Betlehem
hat Bill Clinton
nach zu viel Alkohol gereiert.
Der Teufel schaute zu
und rief sofort die Polizei.


2. Umsetzung:
Um das Ganze in einem Programm abzubilden, werden die einzelnen Abschnitte
separiert in Listen eingegeben, die als temporäre, individuelle Datei ge-
speichert werden. Diese Listen werden wie das Blatt papier behandelt: 
Jeweils der erste Eintrag wird in der eigenen Liste gespeichert, danach
wird die jeweils nächste Liste gefüllt.

2.1 Bots:
Alle Einträge werden zusätzlich in allgemeinen Textdateien abgespeichert.
Aus diesen Textdateien werden von den Bot-Spielern entsprechende Listen 
geladen und über einen Zufallsgenerator in die Storys eingefügt. 
Je häufiger das Spiel von menschlichen Spielern gespielt wird, desto größer
wird der "Wortschatz" der Bots und umso abwechslungsreicher das Spiel mit 
diesen.

