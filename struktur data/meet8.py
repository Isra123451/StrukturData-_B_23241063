# perbendingan lanjutan 

# +++++ 3 -------- 9 +++++
MasukanUser = float (input ("masukan bilangan \nkurang dari 3 atau lebih dari 9 : " )) 

# ----- cek kurang dari 3
kurDar = (MasukanUser < 3 ) 
print (" kurang dari 3 =", kurDar )

# ----- cek lebih  dari 9
lebDar = (MasukanUser > 9)
print (" lebih dari 9 =", lebDar )

betul = kurDar or lebDar 
print ( "pengecekan final : ", betul  )

# 4 14 
MasukanUser = float (input ("masukan bilangan antara 4 dan 14 : ") ) 
hasil = ( 4 < MasukanUser < 14 ) 
print ( hasil )

# cek lebih dari 10 
lebDar = ( MasukanUser > 4)
print ( " lebih dari 4 =" , lebDar )

# betul 
betul = kurDar or lebDar 
print (" pengecekan final :", betul)
hasil =(4 < MasukanUser < 14)
print (hasil)