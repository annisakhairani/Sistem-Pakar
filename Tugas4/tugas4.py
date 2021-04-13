# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:25:33 2021

@author: ASUS
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
#%%
# Generate semua variabel
# * Kualitas dan layanan pada rentang subjektif [0, 10]
# * Tip memiliki rentang [0, 25] dalam satuan poin persentase
x_uas = np.arange(0, 5, 1)
x_un = np.arange(350, 630, 1)
x_utbk  = np.arange(0, 750, 1)
#%%
# Generate fuzzy membership functions
uas_rendah = fuzz.trapmf(x_uas,[0, 0.5, 1, 2])
uas_sedang = fuzz.trapmf(x_uas,[1, 2, 3, 4])
uas_tinggi = fuzz.trapmf(x_uas,[3, 4, 4, 4.5])

un_rendah = fuzz.trapmf(x_un,[0, 350, 400, 480])
un_sedang = fuzz.trimf(x_un,[400, 480, 530])
un_tinggi = fuzz.trapmf(x_un,[480, 530, 600, 630])

utbk_rendah = fuzz.trapmf(x_utbk,[0, 0, 300, 450])
utbk_sedang = fuzz.trapmf(x_utbk,[300, 350, 650, 750])
utbk_tinggi = fuzz.trapmf(x_utbk,[650, 680, 700, 750])

R = 20
S = 50
T = 100
#%%
# Visualize these universes and membership functions//membuat visualisasi grafik
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 10))

ax0.plot(x_uas, uas_rendah, 'b', linewidth=1.5, label='Rendah')
ax0.plot(x_uas, uas_sedang, 'g', linewidth=1.5, label='Sedang')
ax0.plot(x_uas, uas_tinggi, 'r', linewidth=1.5, label='Tinggi')
ax0.set_title('Index Prestasi Siswa')
ax0.legend()

ax1.plot(x_un, un_rendah, 'b', linewidth=1.5, label='Rendah')
ax1.plot(x_un, un_sedang, 'g', linewidth=1.5, label='Sedang')
ax1.plot(x_un, un_tinggi, 'r', linewidth=1.5, label='Tinggi')
ax1.set_title('Index Nilai UN')
ax1.legend()

ax2.plot(x_utbk, utbk_rendah, 'b', linewidth=1.5, label='Rendah')
ax2.plot(x_utbk, utbk_sedang, 'g', linewidth=1.5, label='Sedang')
ax2.plot(x_utbk, utbk_tinggi, 'r', linewidth=1.5, label='Tinggi')
ax2.set_title('Index UTBK')
ax2.legend()

ax3.plot([3, 3],[0, T], 'b', linewidth=1.5, label= 'Tinggi')
ax3.plot([2, 2],[0, S], 'g', linewidth=1.5, label= 'Sedang')
ax3.plot([1, 1],[0, R], 'r', linewidth=1.5, label= 'Rendah')
ax3.set_title('Singleton Sugeno')
ax3.legend()
#%%
##Family
R=20
S=50
T=100
M=[(R,R,R,R,S,T,R,T,T),(R,S,S,S,S,T,T,T,T),(R,T,S,T,S,T,T,T,T)]
#%%
# We need the activation of our fuzzy membership functions at these values.
# The exact values 6.5 and 9.8 do not exist on our universes…
# This is what fuzz.interp_membership exists for!
##input crisp
in_uas = 3.3
in_un = 490
in_utbk = 320
#%%
#fuzzification
in_1 =[]
in_1.append(fuzz.interp_membership(x_uas, uas_rendah, in_uas))
in_1.append(fuzz.interp_membership(x_uas, uas_sedang, in_uas))
in_1.append(fuzz.interp_membership(x_uas, uas_tinggi, in_uas))

in_2 =[]
in_2.append(fuzz.interp_membership(x_un, un_rendah, in_un))
in_2.append(fuzz.interp_membership(x_un, un_sedang, in_un))
in_2.append(fuzz.interp_membership(x_un, un_tinggi, in_un))

in_3 =[]
in_3.append(fuzz.interp_membership(x_utbk, utbk_rendah, in_utbk))
in_3.append(fuzz.interp_membership(x_utbk, utbk_sedang, in_utbk))
in_3.append(fuzz.interp_membership(x_utbk, utbk_tinggi, in_utbk))

print("Derajat Keanggotaan Nilai uas")  
if in_1[0]>0:  
    print("Rendah : "+ str(in_1[0]))  
if in_1[1]>0:  
    print("Sedang : "+ str(in_1[1]))  
if in_1[2]>0:  
    print("Tinggi : "+ str(in_1[2]))  
    
print("")  
print("Derajat Keanggotaan Nilai un")  
if in_2[0]>0:  
    print("Rendah : "+ str(in_2[0]))  
if in_2[1]>0:  
    print("Sedang : "+ str(in_2[1]))  
if in_2[2]>0:  
    print("Tinggi : "+ str(in_2[2]))

print("")  
print("Derajat Keanggotaan Nilai utbk")  
if in_3[0]>0:  
    print("Rendah : "+ str(in_3[0]))  
if in_3[1]>0:  
    print("Sedang : "+ str(in_3[1]))  
if in_3[2]>0:  
    print("Rendah : "+ str(in_3[2]))  
#%%
print("Matriks Nilai uas")  
print(in_1)  
print("")  
print("Matriks Nilai un")  
print(in_2)  
print("Matriks Nilai utbk")  
print(in_3)  
#%%
#Inferensi dan Defazzifikasi dengan Metode Sugeno  
#Penyebut  
rul =[]  
for i in range(3) :  
    for j in range (3) :  
        rule = fuzz.relation_min(in_1[i], in_2[j])  
        rul.append(rule)  
penyebut=np.sum(rul)  
  
#Pembilang  
rul =[]  
for i in range(3) :  
    for j in range(3) :  
        rule=fuzz.relation_min(in_1[i], in_2[j])  
        rulxx=rule*M[i][j]  
        rul.append(rulxx)  
pembilang=np.sum(rul)  
hasil = pembilang/penyebut  
  
print ("Index Kelayakan Diterima Di Fakultas : "+ str(hasil))  
if hasil >=0 and hasil <=20 :  
    za = (abs(hasil - 0)/(20-0))*100  
    zb = (abs(hasil - 20)/(20-0))*100  
    print("Tidak Lulus : "+ '{:2.2f}'.format(zb)+" %")  
    print("Tidak Lulus : "+ '{:2.2f}'.format(za)+" %")  
if hasil >=20 and hasil <=50 :  
    za = (abs(hasil - 20)/(50-20))*100  
    zb = (abs(hasil - 50)/(50-20))*100  
    print("Tidak Lulus : "+ '{:2.2f}'.format(zb)+" %")  
    print("Waiting List : "+ '{:2.2f}'.format(za)+" %")  
if hasil >=50 and hasil <=100 :  
    za = (abs(hasil - 50)/(100-50))*100  
    zb = (abs(hasil - 100)/(100-50))*100  
    print("Waiting List : "+ '{:2.2f}'.format(zb)+" %")  
    print("Lulus : "+ '{:2.2f}'.format(za)+" %") 