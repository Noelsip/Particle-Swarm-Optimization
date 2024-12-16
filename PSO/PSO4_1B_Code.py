import random
import math

# Fungsi X
def func(x):
    return (-3 * x * math.sin(x))

# Inisialisasi variabel-variabel lainnya
c1 = 1
c2 = 1/2
r1 = r2 = random.randint(0,1)
w = 1
Gbest = 0
Pbesti = []

#inisialisasi vo,x1 awal, x1 sebelumnya, y1 awal, y1 sebelumnya, vi setelah iterasi
v0 = 0
xi = {}
xi_before = {}
vi = {}

for i in range(10):
    xi[f"x{i+1}"] = random.uniform(0, math.pi)
    xi_before[f"x{i+1}"] = 0
    vi[f"v{i+1}"] = v0

# Fungsi untuk mencari Gbest dengan membandingkan semua fungsi(x) lalu mengambil nilai x dari fungsi yangmenghasilkan nilai paling kecil
def x_minimum(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    global Gbest
    
    # Membuat list dari nilai x
    x_values = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
    
    # Menyimpan nilai fungsi pertama untuk inisialisasi
    min_value = func(x_values[0])
    Gbest = x_values[0]
    
    # Loop untuk mencari nilai x dengan fungsi terkecil
    for x in x_values[1:]:
        current_value = func(x)
        if current_value < min_value:
            min_value = current_value
            Gbest = x



# Fungsi untuk yang akan mengambil langsung nilai xi dan menympannya kedalam array Pbesti jika sedang dalam iterasi pertama
def fx_minimum_iterasi1(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    for i in range(10):
        Pbesti.append(func(xi[f"x{i+1}"]))

# Fungsi untuk mengambil nilai xi dan menyimpannya kedalam Pbesti dengan cara membandikan antara nilai fungsi f(x) iterasi sekarang dengan iterasi sebelumnya
def fx_minimum_selanjutnya(x1_before,x1,x2_before,x2,x3_before,x3,x4_before,x4,x5_before,x5,x6_before,x6,x7_before,x7,x8_before,x8,x9_before,x9,x10_before,x10):
    for i in range(10):
        if func(xi[f"x{i+1}"]) < func(xi_before[f"x{i+1}"]):
            Pbesti.append(xi[f"x{i+1}"])
        else:
            Pbesti.append(xi_before[f"x{i+1}"])

# Fungsi untuk mencari nilai vi
def vi_func(vimin1,xi,i):
    return (w * vimin1)+(c1*r1*((Pbesti[i]) - xi))+(c2*r2*((Gbest) - xi))

n = int(input(f"Masukan Jumlah Iterasi :"))
print()

# Looping berdasarakan jumlah iterasi yang diinginkan
for index in range(n) :
    print()
    print("\033[0;31m"+ f"Iterasi ke {index+1}" + "\033[0m")
    
    # Pengosongan array Pbesti
    Pbesti.clear()

    # Kondisional statetement yang mana jika index nya sama dengan 0 fungsi fx_minimum_iterasi1 akan dijalankan jika tidak terpenuhi fx_minimum_selanjutnya yang dijalankan
    if index == 0 :
        fx_minimum_iterasi1(xi["x1"],xi["x2"],xi["x3"],xi["x4"],xi["x5"],xi["x6"],xi["x7"],xi["x8"],xi["x9"],xi["x10"])
    else:
        fx_minimum_selanjutnya(xi_before["x1"],xi["x1"],xi_before["x2"],xi["x2"],xi_before["x3"],xi["x3"],xi_before["x4"],xi["x4"],xi_before["x5"],xi["x5"],xi_before["x6"],xi["x6"],xi_before["x7"],xi["x7"],xi_before["x8"],xi["x8"],xi_before["x9"],xi["x9"],xi_before["x10"],xi["x10"])

    # Memanggil fungsi x_minimum
    x_minimum(Pbesti[0],Pbesti[1],Pbesti[2],Pbesti[3],Pbesti[4],Pbesti[5],Pbesti[6],Pbesti[7],Pbesti[8],Pbesti[9])

    for i in range(10):
        # Update nilai vi berdasarkan fungsi vi_func
        vi[f"v{i+1}"] = vi_func(vi[f"v{i+1}"],xi[f"x{i+1}"],i)
        
        # Update nilai xi penampungan (xi_before) dengan nilai dari xi iterasi sekarang
        xi_before[f"x{i+1}"] = xi[f"x{i+1}"]
        
        # Update nilai dari xi iterasi sekarang
        xi[f"x{i+1}"] = xi[f"x{i+1}"] + vi[f"v{i+1}"]
        
        # Menampilkan nilai xi, vi, Pbesti, Gbest, dan nilai minimum f(Gbest)
        print(f"nilai x{i+1}: {xi[f'x{i+1}']:.2f}\t\t\t\tnilai f(x{i+1}): {func(xi[f'x{i+1}']):.2f}")
        print(f"nilai v{i+1}: {vi[f'v{i+1}']:.2f}\t\t\t\tnilai Pbesti: {Pbesti[i]:.2f}")

    print()
    print(f"Nilai Gbest: {Gbest:.2f}")
    print(f"Nilai Minimum f({Gbest:.2f}): {func(Gbest):.2f}")
    print()