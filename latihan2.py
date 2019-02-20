print("=========latihan2=======")
print("Nama : WANDA BELINGGA PUTRA")
print("Nim  : 311810751")
print("kelas:TI.18.B2")
print("menampilkan bilangan berhenti ketika bilangan 0, dan menampilkan bilangan terbesar")
max=0
while True:
    a=int(input("masukan bilangan = "))
    if max < a :
        max = a
    if a==0:
        break
print("bilangan terbesarnya adalah = ",max)
