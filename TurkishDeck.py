# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:54:45 2019

@author: batuhan
"""
#Pytonic kart destesi
# __getitem__ ve __len__
import collections

Kart = collections.namedtuple("Kart", ["rakam", "suit"])

class Deste:
    rakamlar = [str(n) for n in range(2, 11)] + list("JQKA")
    suitler = "sinek kupa maça karo".split()
    
    def __init__(self):
        self._kart = [Kart(rakam, suit) for suit in self.suitler
                                     for rakam in self.rakamlar]
        
    def __len__(self):
        return len(self._kart)
    
    def __getitem__(self, pos):
        return self._kart[pos]
    
deneme1 = Kart("5", "maça") # output -> Kart(rakam="5", suit="maça")

# örneğin amacı Deste sınıfından len ve get için...
deste = Deste()
print(len(deste)) # output -> 52
print(deste[0], deste[-1]) # burası da __getitem__ sayesinde

# desteden rastgele bir kart seçmek için
from random import choice
print(choice(deste))

# destedeki tüm as kartları almak için.. as 12. kart
print(deste[12::13]) # 12. kartı al sonra 13 kart sonraki kartı al...

# __getitem__ sayesinde class iterable oldu
for kartlar in deste: # reversed() ile tersten yapılabilir.
    print(kartlar)
    
# belirli bir kartın destede olup olmadığı...
print(Kart("7", "maça") in deste) # true
print(Kart("15", "kako") in deste) # false

#sıralamayla yapalım.. aslar en yüksek, suitlerden de sinek, kupa, karo, maça şeklinde olcak
suit_degerleri = {"sinek" : 3, "kupa" : 2, "karo" : 1, "maça" : 0}

def sıralama(kart):
    rakam_degerleri = Deste.rakamlar.index(kart.rakam) # destedeki kartların rakamlarını indexlerine göre sıralar
    return rakam_degerleri * len(suit_degerleri) + suit_degerleri[kart.suit]

for kart in sorted(deste, key=sıralama):
    print(kart)












