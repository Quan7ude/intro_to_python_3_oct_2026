# CRUD
#  C = Create
#  R = Read
#  U = Update
#  D = Delete
data_makanan= ["nasi goreng", "mie goreng", "sate ayam", "sate kambing", "soto ayam"]
data_makanan.append("bakso")
print(f"all data : {data_makanan}")


data_kelas = {
        "ketua_kelas" : "Budi",
        "jurusan" : ["IPA","IPS","Bahasa"],
        "tingkat_kelas" : 11,
}

print (f"jurusan kelas : {data_kelas ["jurusan"][1]}")
# update
data_kelas ["jurusan"] = "IPA"
print (f"data all : {data_kelas}")
# delete
del data_kelas ["tingkat_kelas"]
print (f"data all : {data_kelas}")
data_kelas["tingkat_kelas"] = 12
print (f"data all : {data_kelas}")
