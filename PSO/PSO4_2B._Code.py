import random

#fungsi f(X,y)
def func(x,y):
    return ((2*x + y**2 - 5)**2 + (x**2 + y - 3)**2 )

#inisialisasi variabel-variabel lainnya
c1=1
c2=1/2
r1= r2 = random.randint(0,1)
w=1
Gbest=0
besti=0
Pbestix=[]
Pbestiy=[]

#inisialisasi vo,x1 awal, x1 sebelumnya, y1 awal, y1 sebelumnya, vix dan viy setelah iterasi
v0 = 0
xi = {}
yi = {}
xi_before = {}
yi_before = {}
vix = {}
viy = {}

for i in range(10):
    xi[f"x{i+1}"] = random.uniform(-5, 5)
    yi[f"y{i+1}"] = random.uniform(-5, 5)
    xi_before[f"x{i+1}"] = 0
    yi_before[f"y{i+1}"] = 0
    vix[f"v{i+1}"] = v0
    viy[f"v{i+1}"] = v0

#fungsi untuk mencari Gbestx dan Gbesty dengan membandingkan semua fungsi(x,y) lalu mengambil nilai x & y dari fungsi yang menghasilkan nilai paling kecil
def xy_mininum(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10):
    global Gbestx
    global Gbesty
    
    # Menyimpan nilai x dan y dalam list
    x_vals = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
    y_vals = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10]
    
    # Inisialisasi Gbestx dan Gbesty dengan nilai pertama
    Gbestx = x1
    Gbesty = y1
    
    # Iterasi untuk membandingkan setiap nilai xi dan yi
    for i in range(10):
        if func(x_vals[i], y_vals[i]) < func(Gbestx, Gbesty):
            Gbestx = x_vals[i]
            Gbesty = y_vals[i]


#fungsi untuk yang akan mengambil langsung nilai xi & yi dan menympannya kedalam array Pbestix dan Pbestiy jika sedang dalam iterasi pertama
def fxy_minimum_iterasi1(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10):
    for i in range(10):
        Pbestix.append(xi[f"x{i+1}"])
        Pbestiy.append(yi[f"y{i+1}"])

# fungsi untuk mengambil nilai xi & yi dan menyimpannya kedalam Pbestix dan Pbestiy dengan cara membandikan antara nilai fungsi f(x,y) iterasi sekarang dengan iterasi sebelumnya
def fxy_minimum_selanjutnya(x1_before,x1,x2_before,x2,x3_before,x3,x4_before,x4,x5_before,x5,x6_before,x6,x7_before,x7,x8_before,x8,x9_before,x9,x10_before,x10,y1_before,y1,y2_before,y2,y3_before,y3,y4_before,y4,y5_before,y5,y6_before,y6,y7_before,y7,y8_before,y8,y9_before,y9,y10_before,y10):
    for i in range(10):
        if func(xi[f"x{i+1}"], yi[f"y{i+1}"]) <= func(xi_before[f"x{i+1}"], yi_before[f"y{i+1}"]):
            Pbestix.append(xi[f"x{i+1}"])
            Pbestiy.append(yi[f"y{i+1}"])
        else:
            Pbestix.append(xi_before[f"x{i+1}"])
            Pbestiy.append(yi_before[f"y{i+1}"])

#fungsi untuk mencari nilai vix
def vix_func(vixmin1,xi,i):
    return (w * vixmin1)+(c1*r1*(Pbestix[i] - xi)) +(c2*r2*(Gbestx-xi))
#fungsi untuk mencari nilai viy
def viy_func(viymin1,yi,i):
    return (w * viymin1)+(c1*r1*(Pbestiy[i] - yi)) +(c2*r2*(Gbesty-yi))

n = int(input("masukkan jumlah iterasi: "))


for index in range(n):
    print()
    print("\033[0;31m"+ f"Iterasi ke {index+1}" + "\033[0m")
    #Pengosongan array Pbestix dan Pbestiy
    Pbestix.clear()
    Pbestiy.clear()
    
    #Memanggil fungsi xy_minimum
    xy_mininum(xi["x1"],xi["x2"],xi["x3"],xi["x4"],xi["x5"],xi["x6"],xi["x7"],xi["x8"],xi["x9"],xi["x10"],yi["y1"],yi["y2"],yi["y3"],yi["y4"],yi["y5"],yi["y6"],yi["y7"],yi["y8"],yi["y9"],yi["y10"])

    #Kondisional statetement yang mana jika index nya sama dengan 0 fungsi fxy_minimum_iterasi1 akan dijalankan jika tidak terpenuhi fxy_minimum_selanjutnya yang dijalankan
    if index == 0 :
        fxy_minimum_iterasi1(xi["x1"],xi["x2"],xi["x3"],xi["x4"],xi["x5"],xi["x6"],xi["x7"],xi["x8"],xi["x7"],xi["x8"],yi["y1"],yi["y2"],yi["y3"],yi["y4"],yi["y5"],yi["y6"],yi["y7"],yi["y8"],yi["y9"],yi["y10"])
    else:
        fxy_minimum_selanjutnya(xi_before["x1"],xi["x1"],xi_before["x2"],xi["x2"],xi_before["x3"],xi["x3"],xi_before["x4"],xi["x4"],xi_before["x5"],xi["x5"],xi_before["x6"],xi["x6"],xi_before["x7"],xi["x7"],xi_before["x8"],xi["x8"],xi_before["x9"],xi["x9"],xi_before["x10"],xi["x10"],yi_before["y1"],yi["y1"],yi_before["y2"],yi["y2"],yi_before["y3"],yi["y3"],yi_before["y4"],yi["y4"],xi_before["x5"],xi["x5"],xi_before["x6"],xi["x6"],xi_before["x7"],xi["x7"],xi_before["x8"],xi["x8"],xi_before["x9"],xi["x9"],xi_before["x10"],xi["x10"],)

    #update nilai vix berdasarkan fungsi vix_func
    for i in range(0,10):
        vix[f"v{i+1}"] = vix_func(vix[f"v{i+1}"],xi[f"x{i+1}"],i)

        #update nilai viy berdasarkan fungsi viy_func
        viy[f"v{i+1}"] = viy_func(viy[f"v{i+1}"],yi[f"y{i+1}"],i)

    #Update nilai xi penampungan (xi_before) dengan nilai dari xi iterasi sekarang
    for i in range(10):
        xi_before[f"x{i+1}"] = xi[f"x{i+1}"]

        #updata nilai dari xi iterasi sekarang
        xi[f"x{i+1}"] = xi_before[f"x{i+1}"] + vix[f"v{i+1}"]

        #Update nilai yi penampungan (yi_before) dengan nilai dari yi iterasi sekarang
        yi_before[f"y{i+1}"] = yi[f"y{i+1}"]

        #update nilai dari yi iterasi sekarang
        yi[f"y{i+1}"] = yi_before[f"y{i+1}"] + viy[f"v{i+1}"]

        #Menampilkan nilai xi dan yi iterasi sekarang
        print(f"Nilai x{i+1},y{i+1}: [{xi[f'x{i+1}']:.2f}],[{yi[f'y{i+1}']:.2f}]\t\t\t\tNilai f(x{i+1},y{i+1}): {func(xi[f'x{i+1}'],yi[f'y{i+1}']):.2f}")
        print(f"Nilai v{i+1}: [{vix[f'v{i+1}']:.2f}],[{viy[f'v{i+1}']:.2f}]     \t\t\t\tNilai Pbesti(x{i+1},y{i+1}): [{Pbestix[i]:.2f}],[{Pbestiy[i]:.2f}]")

    print()
    print(f"Nilai Gbestx: {Gbestx:.2f}")
    print(f"Nilai Gbesty: {Gbesty:.2f}")
    print(f"Nilai minimum f({Gbestx:.2f}, {Gbesty:.2f})= {func(Gbestx,Gbesty):.2f}")