print("========= Program 1 =========")
print("PROGRAM MNEGHITUNG LABAH PERUSAHAAN DENGAN MODAL AWAL 100 JUTA")
print("")
print("Nama  : WANDA BELINGGA PUTRA")
print("NIM   : 311810751")
print("Kelas : TI.18.B.2")
print("")
print("Catatan : ")
print("Laba perusahaan bulan ke- 1 dan 2 = 0%")
print("Laba perusahaan bulan ke- 3 dan 4 = 1%")
print("Laba perusahaan bulan ke- 5 dan 6 = 5%")
print("Laba perusahaan bulan ke- 7 dan 8 = 3%")

a=100000000
for x in range(1,9):
    if (x>=1and x<=2):
        b=a*0
        print("Laba bulan ke ",x," : ",b)
    if (x>=3and x<=4):
        c=a*0.1
        print("Laba bulan ke ",x," : ",c)
    if (x>=5 and x<=6):
        d=a*0.5
        print("Laba bulan ke ",x," : ",d)