#perbandingan lanjutan

# +++++3 --------9++++++++
MasukanUser = float(input ("masukan bilangan \nkurang dari 3atau \nlebih dari 9 :"))

# ----cek kurang dari 3
kurDar = (MasukanUser <3)
print ("kurang dari3 =",kurDar)

# ----cek kurang dari 9
lebDar = (MasukanUser <9)
print ("kurang dar 9 =")

betul = kurDar or lebDar 
print("pengecekan final : " , betul)


# 4 14
MasukanUser = float(input("masukan bilangan antara 4 dan 14 : "))
kurDar = (MasukanUser < 14)
print("kurang dari 14 =", kurDar)

#cek lebih dari 10 
lebDar = (MasukanUser > 4)
print("lebih dari 4 =", lebDar)

#betul 
betul = kurDar or lebDar
print("pengecekan final :", betul)
hasil = (4 < MasukanUser < 14)
print (hasil)