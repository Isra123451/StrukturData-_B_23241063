#tabel kebenaran (logika bolean)
# not and or xor

# NOT

print("*logika NOT*")
x = False
y = True
print('value dari x = ', x)
print('***NOT')
print('value dari y = ', y)

# login OR(semua bernilai true asalkan ada true-nya)
# hanya untuk wanita 
print("<<<<<logika OR>>>>>")
x = False
y = False 
z = x or y 
print(x, ' OR', y, 'adi', z)
x = False
y = True
z = x or y 
print(x, 'OR', y, 'adi', z)
x = True
y = False
z = x or y 
print(x, 'OR', y, 'adi', z)
x = True
y = True
z = x or y 
print(x, 'OR', y, 'adi', z)

# logika AND(hanya bernilai true, ketika keduanya true)
# berlaku untuk laki laki
print("<<<<<logika AND>>>>>")
x = False
y = False
z = x and y
print(x, 'and', y, 'adi', z)
x = False
y = True
z = x and y 
print(x, 'and', y, 'adi', z)
x = True
y = False
z = x and y 
print(x, 'and', y, 'adi', z)
x = True
y = True
z = x and y 
print(x, 'and', y, 'adi', z)

# logika XOR(jika keduanya sama hasilnya false,sisanya bernilai true)
#
print("<<<<<logika XOR>>>>>")
x = False
y = False
z = x ^ y
print(x, 'XOR', y, 'adi', z)
x = False
y = True
z = x ^ y 
print(x, 'XOR', y, 'adi', z)
x = True
y = False
z = x ^ y 
print(x, 'XOR', y, 'adi', z)
x = True
y = True
z = x and y 
print(x, 'and', y, 'adi', z)