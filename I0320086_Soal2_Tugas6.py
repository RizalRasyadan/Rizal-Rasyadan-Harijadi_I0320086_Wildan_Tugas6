x = int(input("masukan jumlah data :"))
nilai = []
angka = 0

for i in range(0,x):
    j = int(input("Masukkan data ke-%d:" %(i+1)))
    nilai.append(j)
    angka += nilai[i]
    rata2 = angka / x
print("Nilai rata-rata Anda adalah %0.2f" %rata2)