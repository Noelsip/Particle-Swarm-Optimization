import random
import math

# Fungsi X
def func(x):
    return (3 * x * math.sin(x))

# Inisialisasi variabel-variabel lainnya
c1 = 1
c2 = 1/2
r1 = r2 = random.randint(0,1)
w = 1
Gbest = 0
Pbesti = []

# Inisialisasi variabel xi awal untuk iterasi pertama
xi = {
    "x1" : random.uniform(0, math.pi),
    "x2" : random.uniform(0, math.pi),
    "x3" : random.uniform(0, math.pi),
    "x4" : random.uniform(0, math.pi),
    "x5" : random.uniform(0, math.pi),
    "x6" : random.uniform(0, math.pi),
    "x7" : random.uniform(0, math.pi),
    "x8" : random.uniform(0, math.pi),
    "x9" : random.uniform(0, math.pi),
    "x10": random.uniform(0, math.pi)
}

# Inisialisasi penampungan variabel xi-1 untuk perbandingan mencari Pbestix
xi_before={
    "x1" : 0,
    "x2" : 0,
    "x3" : 0,
    "x4" : 0,
    "x5" : 0,
    "x6" : 0,
    "x7" : 0,
    "x8" : 0,
    "x9" : 0,
    "x10": 0
}

# Inisialisasi vo
v0 = 0

# Inisialisasi vi setelah terjadi iterasi
vi = {
    "v1":v0,
    "v2":v0,
    "v3":v0,
    "v4":v0,
    "v5":v0,
    "v6":v0,
    "v7":v0,
    "v8":v0,
    "v9":v0,
    "v10":v0
}

# Fungsi untuk mencari Gbest dengan membandingkan semua fungsi(x) lalu mengambil nilai x dari fungsi yangmenghasilkan nilai paling kecil
def x_minimum(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    global Gbest
    if func(x1)<=func(x2) and func(x1)<=func(x3) and func(x1)<=func(x4) and func(x1)<=func(x5) and func(x1)<=func(x6) and func(x1)<=func(x7) and func(x1)<=func(x8) and func(x1)<=func(x9) and func(x1)<=func(x10) :
        Gbest = x1
    elif func(x2)<=func(x1) and func(x2)<=func(x3) and func(x2)<=func(x4) and func(x2)<=func(x5) and func(x2)<=func(x6) and func(x2)<=func(x7) and func(x2)<=func(x8) and func(x2)<=func(x9) and func(x2)<=func(x10) :
        Gbest = x2
    elif func(x3)<=func(x1) and func(x3)<=func(x2) and func(x3)<=func(x4) and func(x3)<=func(x5) and func(x3)<=func(x6) and func(x3)<=func(x7) and func(x3)<=func(x8) and func(x3)<=func(x9) and func(x3)<=func(x10) :
        Gbest = x3
    elif func(x4)<=func(x1) and func(x4)<=func(x2) and func(x4)<=func(x3) and func(x4)<=func(x5) and func(x4)<=func(x6) and func(x4)<=func(x7) and func(x4)<=func(x8) and func(x4)<=func(x9) and func(x4)<=func(x10) :
        Gbest = x4
    elif func(x5)<=func(x1) and func(x5)<=func(x2) and func(x5)<=func(x4) and func(x5)<=func(x3) and func(x5)<=func(x6) and func(x5)<=func(x7) and func(x5)<=func(x8) and func(x5)<=func(x9) and func(x5)<=func(x10) :
        Gbest = x5
    elif func(x6)<=func(x1) and func(x6)<=func(x2) and func(x6)<=func(x4) and func(x6)<=func(x5) and func(x6)<=func(x3) and func(x6)<=func(x7) and func(x6)<=func(x8) and func(x6)<=func(x9) and func(x6)<=func(x10) :
        Gbest = x6
    elif func(x7)<=func(x1) and func(x7)<=func(x2) and func(x7)<=func(x4) and func(x7)<=func(x5) and func(x7)<=func(x6) and func(x7)<=func(x3) and func(x7)<=func(x8) and func(x7)<=func(x9) and func(x7)<=func(x10) :
        Gbest = x7
    elif func(x8)<=func(x1) and func(x8)<=func(x2) and func(x8)<=func(x4) and func(x8)<=func(x5) and func(x8)<=func(x6) and func(x8)<=func(x7) and func(x8)<=func(x3) and func(x8)<=func(x9) and func(x8)<=func(x10) :
        Gbest = x8
    elif func(x9)<=func(x1) and func(x9)<=func(x2) and func(x9)<=func(x4) and func(x9)<=func(x5) and func(x9)<=func(x6) and func(x9)<=func(x7) and func(x9)<=func(x8) and func(x9)<=func(x3) and func(x9)<=func(x10) :
        Gbest = x9
    elif func(x10)<=func(x1) and func(x10)<=func(x2) and func(x10)<=func(x4) and func(x10)<=func(x5) and func(x10)<=func(x6) and func(x10)<=func(x7) and func(x10)<=func(x8) and func(x10)<=func(x9) and func(x10)<=func(x3) :
        Gbest = x10

# Fungsi untuk yang akan mengambil langsung nilai xi dan menympannya kedalam array Pbesti jika sedang dalam iterasi pertama
def fx_minimum_iterasi1(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    Pbesti.append(x1)
    Pbesti.append(x2)
    Pbesti.append(x3)
    Pbesti.append(x4)
    Pbesti.append(x5)
    Pbesti.append(x6)
    Pbesti.append(x7)
    Pbesti.append(x8)
    Pbesti.append(x9)
    Pbesti.append(x10)

# Fungsi untuk mengambil nilai xi dan menyimpannya kedalam Pbesti dengan cara membandikan antara nilai fungsi f(x) iterasi sekarang dengan iterasi sebelumnya
def fx_minimum_selanjutnya(x1_before,x1,x2_before,x2,x3_before,x3,x4_before,x4,x5_before,x5,x6_before,x6,x7_before,x7,x8_before,x8,x9_before,x9,x10_before,x10):
    if func(x1)<=func(x1_before):
        Pbesti.append(x1)
    else :
        Pbesti.append(x1_before)
    if func(x2)<=func(x2_before):
        Pbesti.append(x2)
    else :
        Pbesti.append(x2_before)
    if func(x3)<=func(x3_before):
        Pbesti.append(x3)
    else :
        Pbesti.append(x3_before)
    if func(x4)<=func(x4_before):
        Pbesti.append(x4)
    else :
        Pbesti.append(x4_before)
    if func(x4)<=func(x4_before):
        Pbesti.append(x4)
    else :
        Pbesti.append(x4_before)
    if func(x5)<=func(x5_before):
        Pbesti.append(x5)
    else :
        Pbesti.append(x5_before)
    if func(x6)<=func(x6_before):
        Pbesti.append(x6)
    else :
        Pbesti.append(x6_before)
    if func(x7)<=func(x7_before):
        Pbesti.append(x7)
    else :
        Pbesti.append(x7_before)
    if func(x8)<=func(x8_before):
        Pbesti.append(x8)
    else :
        Pbesti.append(x8_before)
    if func(x9)<=func(x9_before):
        Pbesti.append(x9)
    else :
        Pbesti.append(x9_before)
    if func(x10)<=func(x10_before):
        Pbesti.append(x10)
    else :
        Pbesti.append(x10_before)

# Fungsi untuk mencari nilai vi
def vi_func(vimin1,xi,i):
    return (w * vimin1)+(c1*r1*((Pbesti[i]) - xi))+(c2*r2*((Gbest) - xi))

n = int(input(f"Masukan Jumlah Iterasi :"))
print()

# Looping berdasarakan jumlah iterasi yang diinginkan
for index in range(n) :
    # Pengosongan array Pbesti
    Pbesti.clear()

    # Kondisional statetement yang mana jika index nya sama dengan 0 fungsi fx_minimum_iterasi1 akan dijalankan jika tidak terpenuhi fx_minimum_selanjutnya yang dijalankan
    if index == 0 :
        fx_minimum_iterasi1(xi["x1"],xi["x2"],xi["x3"],xi["x4"],xi["x5"],xi["x6"],xi["x7"],xi["x8"],xi["x9"],xi["x10"])
    else:
        fx_minimum_selanjutnya(xi_before["x1"],xi["x1"],xi_before["x2"],xi["x2"],xi_before["x3"],xi["x3"],xi_before["x4"],xi["x4"],xi_before["x5"],xi["x5"],xi_before["x6"],xi["x6"],xi_before["x7"],xi["x7"],xi_before["x8"],xi["x8"],xi_before["x9"],xi["x9"],xi_before["x10"],xi["x10"])

    # Memanggil fungsi x_minimum
    x_minimum(Pbesti[0],Pbesti[1],Pbesti[2],Pbesti[3],Pbesti[4],Pbesti[5],Pbesti[6],Pbesti[7],Pbesti[8],Pbesti[9])

    # Update nilai vi berdasarkan fungsi vi_func
    vi["v1"]= vi_func(vi["v1"],xi["x1"],0)
    vi["v2"] = vi_func(vi["v2"],xi["x2"],1)
    vi["v3"] = vi_func(vi["v3"],xi["x3"],2)
    vi["v4"]= vi_func(vi["v4"],xi["x4"],3)
    vi["v5"] = vi_func(vi["v5"],xi["x5"],4)
    vi["v6"] = vi_func(vi["v6"],xi["x6"],5)
    vi["v7"]= vi_func(vi["v7"],xi["x7"],6)
    vi["v8"] = vi_func(vi["v8"],xi["x8"],7)
    vi["v9"] = vi_func(vi["v9"],xi["x9"],8)
    vi["v10"] = vi_func(vi["v10"],xi["x10"],9)

    # Update nilai xi penampungan (xi_before) dengan nilai dari xi iterasi sekarang
    xi_before["x1"] = xi["x1"]
    xi_before["x2"] = xi["x2"]
    xi_before["x3"] = xi["x3"]
    xi_before["x4"] = xi["x4"]
    xi_before["x5"] = xi["x5"]
    xi_before["x6"] = xi["x6"]
    xi_before["x7"] = xi["x7"]
    xi_before["x8"] = xi["x2"]
    xi_before["x9"] = xi["x9"]
    xi_before["x10"] = xi["x10"]

    # Update nilai dari xi iterasi sekarang
    xi["x1"] = xi_before["x1"] + vi["v1"]
    xi["x2"] = xi_before["x2"] + vi["v2"]
    xi["x3"] = xi_before["x3"] + vi["v3"]
    xi["x4"] = xi_before["x4"] + vi["v4"]
    xi["x5"] = xi_before["x5"] + vi["v5"]
    xi["x6"] = xi_before["x6"] + vi["v6"]
    xi["x7"] = xi_before["x7"] + vi["v7"]
    xi["x8"] = xi_before["x8"] + vi["v8"]
    xi["x9"] = xi_before["x9"] + vi["v9"]
    xi["x10"] = xi_before["x10"] + vi["v10"]
    
    print(f"iterasi ke-{index+1}")
    
    for i in range(10):
        print(f"nilai x{i+1}: {xi['x1']} \t\t nilai f(x{i+1}): {func(xi['x1'])}")

    print()
    print(f"Nilai Gbest: {Gbest}")
    print(f"Nilai Minimum f(x): {func(Gbest)}")
    print()