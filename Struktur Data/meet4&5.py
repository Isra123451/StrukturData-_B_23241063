# Inputan dari user
# aritmatika

# Belajar Inputan
# from tkinter import Y


# azzam = input("masukan kata : ")
# print("isi dari azzam :", azzam,"bertipe data :" type(azzam))

# belajar aritmatika dasar
x = 3
y = 4

# penjumlahan +
hasil = x + y
print ("x + y =",hasil)

# pengurangan -
hasil = x - y
x = 10
y = 3
print ("x - y =",hasil)

# perkalian *
hasil = x * y
x = 20
y = 2
print ("x * y =",hasil)

# pembagian /
hasil = x / y
x = 10
y = 2
print ("x / y =",hasil)

# perangkat exponen **
hasil = x ** y
print ("x ** y =",hasil)

# modulus %
hasil = x % y
print ("x % y =",hasil)

# floor division (pembulatan kebawah) //
hasil = x // y
print ("x // y =",hasil)

# aritmatika prioritals
# (), exponen, perkalian/pembagian, penjumlahan/pengurangan
x = 3
y = 4
z = 5

hasil = ( x ** y * (z + x) / y - z % x // y )
print(hasil)