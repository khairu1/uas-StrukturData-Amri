#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math

class BangunDatar:
    def __init__(self, nama):
        self.nama = nama

    def hitung_luas(self):
        pass

class Trapesium(BangunDatar):
    def __init__(self, nama, a, b, tinggi):
        super().__init__(nama)
        self.a = a
        self.b = b
        self.tinggi = tinggi

    def hitung_luas(self):
        return ((self.a + self.b) * self.tinggi) / 2

class Lingkaran(BangunDatar):
    def __init__(self, nama, radius):
        super().__init__(nama)
        self.radius = radius

    def hitung_luas(self):
        return math.pi * self.radius**2

class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_luas(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

class Segitiga(BangunDatar):
    def __init__(self, nama, alas, tinggi):
        super().__init__(nama)
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return (self.alas * self.tinggi) / 2

class PersegiPanjang(BangunDatar):
    def __init__(self, nama, panjang, lebar):
        super().__init__(nama)
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

class Persegi(BangunDatar):
    def __init__(self, nama, sisi):
        super().__init__(nama)
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi**2

# Contoh penggunaan
trapesium = Trapesium("Trapesium", 5, 7, 4)
print(f"Luas {trapesium.nama} = {trapesium.hitung_luas()}")

lingkaran = Lingkaran("Lingkaran", 3)
print(f"Luas {lingkaran.nama} = {lingkaran.hitung_luas()}")

balok = Balok(6, 4, 5)
print(f"Luas permukaan balok = {balok.hitung_luas()}")

segitiga = Segitiga("Segitiga", 6, 8)
print(f"Luas {segitiga.nama} = {segitiga.hitung_luas()}")

persegi_panjang = PersegiPanjang("Persegi Panjang", 5, 10)
print(f"Luas {persegi_panjang.nama} = {persegi_panjang.hitung_luas()}")

persegi = Persegi("Persegi", 4)
print(f"Luas {persegi.nama} = {persegi.hitung_luas()}")


# In[ ]:




