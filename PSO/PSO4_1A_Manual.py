import math
# Fungsi f(x)
def func(x):
    return (-3 * x * math.sin(x))

#inisialisasi variabel xi awal untuk iterasi pertama
xi = {
    "x0" : 1,
    "x1" : math.pi/2,
    "x2" : math.pi,
}

#inisialisasi penampungan variabel xi-1 untuk perbandingan mencari Pbestix
xi_before={
    "x0" : 0,
    "x1" : 0,
    "x2" : 0,
}

#inisialisasi vo
v0 = 0

#inisialisasi vi setelah terjadi iterasi
vi = {
    "v1":v0,
    "v2":v0,
    "v3":v0,
}

#inisialisasi variabel-variabel lainnya
c1 = 1/2
c2 = 1
r1 = r2 = 1
w = 1
Gbest = 0
Pbesti = []

#fungsi untuk mencari Gbest dengan membandingkan semua fungsi(x) lalu mengambil nilai x dari fungsi yangmenghasilkan nilai paling kecil
def x_minimum(x0,x1,x2):
    global Gbest
    if func(x0)<=func(x1) and func(x0)<=func(x2):
        Gbest = x0
    elif func(x1)<=func(x0) and func(x1)<=func(x2):
        Gbest = x1
    elif func(x2)<=func(x0) and func(x2)<=func(x1):
        Gbest = x2

#fungsi untuk yang akan mengambil langsung nilai xi dan menympannya kedalam array Pbesti jika sedang dalam iterasi pertama
def fx_minimum_iterasi1(x0,x1,x2):
    Pbesti.append(x0)
    Pbesti.append(x1)
    Pbesti.append(x2)

# fungsi untuk mengambil nilai xi dan menyimpannya kedalam Pbesti dengan cara membandikan antara nilai fungsi f(x) iterasi sekarang dengan iterasi sebelumnya
def fx_minimum_selanjutnya(x0_before,x0,x1_before,x1,x2_before,x2):
    if func(x0)<=func(x0_before):
        Pbesti.append(x0)
    else :
        Pbesti.append(x0_before)
    if func(x1)<=func(x1_before):
        Pbesti.append(x1)
    else :
        Pbesti.append(x1_before)

    if func(x2)<=func(x2_before):
        Pbesti.append(x2)
    else :
        Pbesti.append(x2_before)
    
#fungsi untuk mencari nilai vi
def vi_func(vimin1,xi,i):
    return (w * vimin1)+(c1*r1*((Pbesti[i]) - xi))+(c2*r2*((Gbest) - xi))

n = int(input("masukkan jumlah iterasi: "))
print()

#Looping berdasarkan jumlah iterasi yang diinginkan
for index in range(n):
    print("\033[0;31m"+f"iterasi ke-{index+1}"+"\033[0m")
    
    #Pengosongan array Pbesti
    Pbesti.clear()

    #Kondisional statetement yang mana jika index nya sama dengan 0 fungsi fx_minimum_iterasi1 akan dijalankan jika tidak terpenuhi fx_minimum_selanjutnya yang dijalankan
    if index == 0 :
        fx_minimum_iterasi1(xi["x0"],xi["x1"],xi["x2"])
    else:
        fx_minimum_selanjutnya(xi_before["x0"],xi["x0"],xi_before["x1"],xi["x1"],xi_before["x2"],xi["x2"])

    #Memanggil fungsi x_minimum
    x_minimum(Pbesti[0],Pbesti[1],Pbesti[2])

    #update nilai vi berdasarkan fungsi vi_func
    vi["v1"]= vi_func(vi["v1"],xi["x0"],0)
    vi["v2"] = vi_func(vi["v2"],xi["x1"],1)
    vi["v3"] = vi_func(vi["v3"],xi["x2"],2)

    #Update nilai xi penampungan (xi_before) dengan nilai dari xi iterasi sekarang
    xi_before["x0"] = xi["x0"]
    xi_before["x1"] = xi["x1"]
    xi_before["x2"] = xi["x2"]
    

    #update nilai dari xi iterasi sekarang
    xi["x0"] = xi_before["x0"] + vi["v1"]
    xi["x1"] = xi_before["x1"] + vi["v2"]
    xi["x2"] = xi_before["x2"] + vi["v3"]

    #Menampilkan nilai xi iterasi sekarang
    for i in range(3):
        print(f"Nilai x{i+1} : {xi[f'x{i}']}")
        print(f"Nilai f(x{i+1}): {func(xi[f'x{i}'])}")
        print()
    

print(f"Nilai Gbest: {Gbest}")
print(f"Nilai minimum f(x): {func(Gbest)}")