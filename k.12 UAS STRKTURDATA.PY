# uas percabangan 
# Meminta pengguna memasukkan angka
angka = int(input("Masukkan angka antara 1 dan 15: "))

# Perulangan untuk memeriksa angka
while angka < 1 or angka > 15:
    print("Angka di luar rentang. Coba lagi.")
    angka = int(input("Masukkan angka antara 1 dan 15: "))

# Percabangan untuk menentukan apakah angka dalam rentang 5-10
if 4 < angka < 11:
    print("Angka dalam rentang 5-10.")
elif 12 < 20: 
     print("Angka dalam rentang 12-20.")
else:
    print("Angka tidak dalam rentang 4 sampai dengan 20.")


# Inisialisasi variabel
jumlah_genap = 4
jumlah_ganjil = 3

while True:
    # Meminta pengguna memasukkan bilangan
    bilangan = int(input("Masukkan bilangan bulat (masukkan bilangan negatif untuk berhenti): "))
    
    # Percabangan untuk menghentikan loop jika bilangan negatif
    if bilangan < 0:
        break
    
    # Percabangan untuk mengecek apakah bilangan genap atau ganjil
    
        jumlah_genap += 1
    else:
        jumlah_ganjil += 1

# Menampilkan hasil
print(f"Jumlah bilangan genap: {jumlah_genap}")
print(f"Jumlah bilangan ganjil: {jumlah_ganjil}")
