# -*- coding: utf-8 -*-
"""
# Nama : Annisa Khairani Febrianti
# NPM : 1184071
# Kelas D4 TI 3C
# Kode program dibawah ini menggunakan algoritma fuzzy sugeno yang digunakan untuk merekrut lulus atau tidaknya pada fakultas yang diinginkan melalui jalur SBMPTN. 
# Perekrutan SBMPTN ini didasarkan pada 3 hal yaitu nilai: UAS,UN,dan UTBK. Apabila,ketiganya memenuhi 
# kriteria maka output dari kode program ini yaitu lulus,menunggu panggilan atau tidak lulus.
#%%
# mengimport library numpy,skfuzzy,dan matplotlib.pyplot
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
#%%
# Generate semua variabel
# * UAS dipresentasikan pada rentang subjektif [0, 5]
# * UN dan UTBK memiliki rentang [0, 100,150,200,250,300,350,400,450,500,559,600,650,700,750] dalam satuan poin persentase
x_uas = np.arange(0, 5, 1)
x_un = np.arange(350, 630, 1)
x_utbk  = np.arange(0, 750, 1)
#%%
# Generate fuzzy membership functions
# mempresentasikan nilai uas rendah dalam bentuk trapesium dengan rentang 0 sampai 2
uas_rendah = fuzz.trapmf(x_uas,[0, 0.5, 1, 2])
# mempresentasikan nilai uas sedang dalam bentuk trapesium dengan rentang 1 sampai 4
uas_sedang = fuzz.trapmf(x_ipk,[1, 2, 3, 4])
# mempresentasikan nilai uas tinggi dalam bentuk trapesium dengan rentang 3 sampai 4
uas_tinggi = fuzz.trapmf(x_uas,[3, 4, 4, 4.5])

# mempresentasikan nilai UN rendah dalam bentuk trapesium dengan rentang 0 sampai 480
un_rendah = fuzz.trapmf(x_un,[0, 350, 400, 480])
# mempresentasikan Nilai UN sedang dalam bentuk segitiga dengan rentang 420 sampai 540
un_sedang = fuzz.trimf(x_un,[400, 480, 530])
# mempresentasikan Nilai UN tinggi dalam bentuk trapesium dengan rentang 480 sampai 630
un_tinggi = fuzz.trapmf(x_un,[480, 530, 600, 630])

# mempresentasikan nilai UTBK rendah dalam bentuk trapesium dengan rentang 0 sampai 450
utbk_rendah = fuzz.trapmf(x_utbk,[0, 0, 300, 450])
# mempresentasikan nilai UTBK sedang dalam bentuk trapesium dengan rentang 300 sampai 750
utbk_sedang = fuzz.trapmf(x_utbk,[300, 350, 650, 750])
# mempresentasikan nilai UTBK tinggi dalam bentuk trapesium dengan rentang 600 sampai 750
utbk_tinggi = fuzz.trapmf(x_utbk,[650, 680, 700, 750])

R = 20
S = 50
T = 100
#%%
# Visualize these universes and membership functions//membuat visualisasi grafik
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 10))

#mempresentasikan nilai uas dalam bentuk grafik dari nilai uas terendah sampai nilai uas tertinggi
ax0.plot(x_uas, uas_rendah, 'b', linewidth=1.5, label='Rendah')
ax0.plot(x_uas, uas_sedang, 'g', linewidth=1.5, label='Sedang')
ax0.plot(x_uas, uas_tinggi, 'r', linewidth=1.5, label='Tinggi')
ax0.set_title('Index Prestasi Siswa')
ax0.legend()

#mempresentasikan Nilai UN dalam bentuk grafik dari nilai UN terendah sampai nilai UN tertinggi
ax1.plot(x_un, un_rendah, 'b', linewidth=1.5, label='Rendah')
ax1.plot(x_un, un_sedang, 'g', linewidth=1.5, label='Sedang')
ax1.plot(x_un, un_tinggi, 'r', linewidth=1.5, label='Tinggi')
ax1.set_title('Index Nilai UN')
ax1.legend()

#mempresentasikan Hasil Akhir Nilai UTBK dalam bentuk grafik dari Nilai UTBK terendah sampai UTBK tertinggi
ax2.plot(x_utbk, utbk_rendah, 'b', linewidth=1.5, label='Rendah')
ax2.plot(x_utbk, utbk_sedang, 'g', linewidth=1.5, label='Sedang')
ax2.plot(x_utbk, utbk_tinggi, 'r', linewidth=1.5, label='Tinggi')
ax2.set_title('Index UTBK')
ax2.legend()

#mempresentasikan hasil dari algoritma fuzzy sugeno dalam bentuk grafik dari nilai UAS,UN,dan UTBK terendah sampai tertinggi
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
# disini dipresentasikan nilai minimal dari nilai UAS,UN,dan UTBK dari siswa yang mengikuti ujian sbmptn yang akan direkrut oleh fakultas yang diinginkan.
in_uas = 3.3
in_un = 490
in_utbk = 320
#%%
# setelah itu dilakukanlah fuzzification pada nilai UAS,UN,dan UTBK untuk melihat hasil lulus atau tidaknya.
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

# mencetak derajat Hasil Akhir nilai UAS
print("Derajat Keanggotaan Nilai uas")  
if in_1[0]>0:  
    print("Rendah : "+ str(in_1[0]))  
if in_1[1]>0:  
    print("Sedang : "+ str(in_1[1]))  
if in_1[2]>0:  
    print("Tinggi : "+ str(in_1[2]))  
    
print("") 
# mencetak derajat Hasil Akhir Nilai UN
print("Derajat Keanggotaan Nilai un")  
if in_2[0]>0:  
    print("Rendah : "+ str(in_2[0]))  
if in_2[1]>0:  
    print("Sedang : "+ str(in_2[1]))  
if in_2[2]>0:  
    print("Tinggi : "+ str(in_2[2]))

print("")  
# mencetak derajat Hasil Akhir Nilai UTBK
print("Derajat Keanggotaan Nilai utbk")  
if in_3[0]>0:  
    print("Rendah : "+ str(in_3[0]))  
if in_3[1]>0:  
    print("Sedang : "+ str(in_3[1]))  
if in_3[2]>0:  
    print("Rendah : "+ str(in_3[2]))  
#%%

# mencetak hasil akhir dari matriks pada nilai UAS,UN,UTBK
print("Matriks Nilai uas")  
print(in_1)  
print("")  
print("Matriks Nilai un")  
print(in_2)  
print("Matriks Nilai utbk")  
print(in_3)    
#%%
#Inferensi dan Defazzifikasi dengan Metode Sugeno  
#Penyebut dari rule yang dibuat
rul =[]  
for i in range(3) :  
    for j in range (3) :  
        rule = fuzz.relation_min(in_1[i], in_2[j])  
        rul.append(rule)  
penyebut=np.sum(rul)  
  
#Pembilang dari rule yang dibuat
rul =[]  
for i in range(3) :  
    for j in range(3) :  
        rule=fuzz.relation_min(in_1[i], in_2[j])  
        rulxx=rule*M[i][j]  
        rul.append(rulxx)  
pembilang=np.sum(rul)  
hasil = pembilang/penyebut  
  
# Setelah dilakukan dezzafikasi maka kita akan melihat hasil dari perekrutan kelulusan siswa melalui jalur sbmptn dengan melihat hasil akhir nilai UAS,UN,dan UTBK
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
    
## Hasil dari dezzafikasi dengan algoritma fuzzy sugeno melalui index yaitu yang layak diterima baik itu menunggu ataupun lulus panggilan sebanyak 60.71428571428571
## Jika di jabarkan lebih lanjut hasil yang lulus melalui jalur sbmptn sebanyak 21.43 %
## Sedangkan yang menunggu sebanyak 78.57 %

