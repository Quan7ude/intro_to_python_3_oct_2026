data_karyawan = [
{
"nama" : "John",
"gaji" : 500000,
"tahunlahir" : "1992",
},
{
"nama" : "Budi",
"gaji" : 400000,
"tahunlahir" : "1997",
},
{
"nama" : "Lula",
"gaji" : 350000,
"tahunlahir" : "1995",    
},
{
"nama" : "Alkes",
"gaji" : 67000,
"tahunlahir" : "1990",
},
]

# void
def template_print(nama,gaji,usia):
    print(f"nama : {nama}")
    print(f"gaji : {gaji}")
    print(f"usia : {usia}","tahun")
    print ("===============================")

def rumus_usia (tahunlahir:int):
    usia = 2026 - int(tahunlahir)
    return usia

data_karyawan[0]["usia"] = rumus_usia(data_karyawan[0]["tahunlahir"])
data_karyawan[1]["usia"] = rumus_usia(data_karyawan[1]["tahunlahir"])
data_karyawan[2]["usia"] = rumus_usia(data_karyawan[2]["tahunlahir"])
data_karyawan[3]["usia"] = rumus_usia(data_karyawan[3]["tahunlahir"])

print ("=========data karyawan===========")
template_print(data_karyawan[0]["nama"],data_karyawan[0]["gaji"],usia=data_karyawan[0]["usia"])
template_print(data_karyawan[1]["nama"],data_karyawan[1]["gaji"],usia=data_karyawan[1]["usia"])
template_print(data_karyawan[2]["nama"],data_karyawan[2]["gaji"],usia=data_karyawan[2]["usia"])
template_print(data_karyawan[3]["nama"],data_karyawan[3]["gaji"],usia=data_karyawan[3]["usia"])
