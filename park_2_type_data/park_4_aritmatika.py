a = 2
b = 4
#  penjumlahan
hasil = a + b
print (f"hasil penjumlahan {a} + {b} = {hasil}")
# pengurangan
hasil = a - b
print (f"hasil pengurangan {a} - {b} = {hasil}")
# perkalian
hasil = a * b
print (f"hasil perkalian {a} * {b} = {hasil}")
# pembagian
hasil = a / b
print (f"hasil pembagian {a} / {b} = {hasil}")
# contoh casting integer
hasil = a // b
print (f"hasil pembagian integer {a} // {b} = {hasil}")
# modulus
hasil = a % b
print (f"hasil modulus {a} % {b} = {hasil}")    

# penggunaan elif

nilai = 57
if nilai >= 80:
    print ("nilai anda A")
elif nilai >= 70:
    print ("nilai anda B")
elif nilai >= 60:
    print ("nilai anda C")
elif nilai >= 50:
    print ("nilai anda D")
else:
    print ("anda tidak lulus")

# match and case
print ("=====match and case=====")
print ("====Menu====")
print ("1. Menu 1")
print ("2. Menu 2")
print ("3. Exit")

select = input ("pilih menu : ")
match select:
    case "1":
        print ("anda memilih menu 1")
    case "2":
        print ("anda memilih menu 2")
    case "3":
        print ("anda memilih menu 3")
    case _:
        print ("anda memilih menu exit")
