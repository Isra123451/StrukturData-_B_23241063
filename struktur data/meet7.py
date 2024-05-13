# Tabel kebenaran (logika bolean)
# not and or xor

# Not

print("*****logika Not*****")
x = False
y = True
print('value x =', x)
print('**********Not')
print('value y =', y)

# OR (semua bernilai true asalkan ada true-nya)
# berlaku untuk wanita
print("*****logika OR*****")
x = False
y = False
z = x or y
print(x, 'OR' , y, '=', z)
x = False
y = True
z = x or y
print(x, 'OR' , y, '=', z)
x = True
y = False
z = x or y
print(x, 'OR' , y, '=', z)
x = True
y = True
z = x or y
print(x, 'OR' , y, '=', z)

# AND (hanya bernilai true, ketika keduanya true)
# berlaku untuk lelaki
print("*****logika AND*****")
x = False
y = False
z = x and y
print(x, 'and' , y, '=', z)
x = False
y = True
z = x or y
print(x, 'and' , y, '=', z)
x = True
y = False
z = x or y
print(x, 'and' , y, '=', z)
x = True
y = True
z = x or y
print(x, 'and' , y, '=', z)

# XOR (jika keduanya sama, hasilnya false, sisanya ber)
print("*****logika XOR*****")
x = False
y = False
z = x and y
print(x, 'XOR' , y, '=', z)
x = False
y = True
z = x or y
print(x, 'XOR' , y, '=', z)
x = True
y = False
z = x or y
print(x, 'XOR' , y, '=', z)
x = True
y = True
z = x or y
print(x, 'XOR' , y, '=', z)
