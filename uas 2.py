#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hitung_gaji(golongan, jam_kerja):
    gaji_pokok = 0

    if golongan == 'A':
        gaji_pokok = 10000000
    elif golongan == 'B':
        gaji_pokok = 7000000
    elif golongan == 'C':
        gaji_pokok = 5000000
    elif golongan == 'D':
        gaji_pokok = 3000000
    else:
        return "Golongan tidak valid."

    if jam_kerja > 48:
        gaji_total = gaji_pokok + (jam_kerja - 40) * (gaji_pokok / 40) * 1.5
    else:
        gaji_total = gaji_pokok

    return gaji_total


while True:
    golongan = input("Masukkan golongan (A/B/C/D): ")
    jam_kerja = int(input("Masukkan jam kerja per bulan: "))

    if golongan in ['A', 'B', 'C', 'D'] and jam_kerja >= 0:
        gaji = hitung_gaji(golongan, jam_kerja)
        print(f"Gaji total: Rp. {gaji:,.2f}")
        break
    else:
        print("Masukan tidak valid. Silakan coba lagi.")


# In[ ]:




