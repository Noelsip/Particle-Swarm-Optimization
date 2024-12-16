import random

#fungsi f(X,y)
def func(x,y):
    return ((2*x + y**2 - 5)**2 + (x**2 + y - 3)**2 )

#inisialisasi variabel xi awal untuk iterasi pertama
xi = {
    "x0" : 1,
    "x1" : -1,
    "x2" : 2
}

#inisialisasi penampungan variabel xi-1 untuk perbandingan mencari Pbestix
xi_before={
    "x0" : 0,
    "x1" : 0,
    "x2" : 0,
}

#inisialisasi variabel yi awal untuk iterasi pertama
yi = {
    "y0" : 1,
    "y1" : -1,
    "y2" : 1
}

#inisialisasi penampungan variabel yi-1 untuk perbandingan mencari Pbestiy
yi_before={
    "y0" : 0,
    "y1" : 0,
    "y2" : 0,
}

#inisialisasi vo
v0 = 0

#inisialisasi vix setelah terjadi iterasi
vix = {
    "v0":v0,
    "v1":v0,
    "v2":v0,
}

##inisialisasi vix setelah terjadi iterasi
viy = {
    "v0":v0,
    "v1":v0,
    "v2":v0,
}

#inisialisasi variabel-variabel lainnya
c1 = 1
c2 = 1/2
r1= r2 = 1
w = 1
Gbestx = 0
Gbesty = 0
Pbestix=[]
Pbestiy=[]

#fungsi untuk mencari Gbestx dan Gbesty dengan membandingkan semua fungsi(x,y) lalu mengambil nilai x & y dari fungsi yang menghasilkan nilai paling kecil
def xy_mininum(x0,x1,x2,y0,y1,y2):
    global Gbestx
    global Gbesty
    if func(x0,y0)<=func(x1,y1) and func(x0,y0)<=func(x2,y2):
        Gbestx = x0
        Gbesty = y0
    if func(x1,y1)<=func(x0,y0) and func(x1,y1)<=func(x2,y2):
        Gbestx = x1
        Gbesty = y1
    if func(x2,y2)<=func(x1,y1) and func(x2,y2)<=func(x0,y0):
        Gbestx = x2
        Gbesty = y2

#fungsi untuk yang akan mengambil langsung nilai xi & yi dan menympannya kedalam array Pbestix dan Pbestiy jika sedang dalam iterasi pertama
def fxy_minimum_iterasi1(x0,x1,x2,y0,y1,y2):
    Pbestix.append(x0)
    Pbestix.append(x1)
    Pbestix.append(x2)
    Pbestiy.append(y0)
    Pbestiy.append(y1)
    Pbestiy.append(y2)

# fungsi untuk mengambil nilai xi & yi dan menyimpannya kedalam Pbestix dan Pbestiy dengan cara membandikan antara nilai fungsi f(x,y) iterasi sekarang dengan iterasi sebelumnya
def fxy_minimum_selanjutnya(x0_before,x0,x1_before,x1,x2_before,x2,y0_before,y0,y1_before,y1,y2_before,y2):
    if func(x0,y0)<=func(x0_before,y0_before):
        Pbestix.append(x0)
        Pbestiy.append(y0)
    else :
        Pbestix.append(x0_before)
        Pbestiy.append(y0_before)
    if func(x1,y1)<=func(x1_before,y1_before):
        Pbestix.append(x1)
        Pbestiy.append(y1)
    else :
        Pbestix.append(x1_before)
        Pbestiy.append(y1_before)
    if func(x2,y2)<=func(x2_before,y2_before):
        Pbestix.append(x2)
        Pbestiy.append(y2)
    else :
        Pbestix.append(x2_before)
        Pbestiy.append(y2_before)

#fungsi untuk mencari nilai vix
def vix_func(vixmin1,xi,i):
    return (w * vixmin1)+(c1*r1*(Pbestix[i] - xi))+(c2*r2*(Gbestx-xi))

#fungsi untuk mencari nilai viy
def viy_func(viymin1,yi,i):
    return (w * viymin1)+(c1*r1*(Pbestiy[i] - yi))+(c2*r2*(Gbesty-yi))

n = int(input("masukkan jumlah iterasi: "))
print()

#Looping berdasarkan jumlah iterasi yang diinginkan
for index in range(n):
    print("\033[0;31m"+f"iterasi ke-{index+1}"+"\033[0m")
    
    #Pengosongan array Pbestix dan Pbestiy
    Pbestix.clear()
    Pbestiy.clear()

    #Kondisional statetement yang mana jika index nya sama dengan 0 fungsi fxy_minimum_iterasi1 akan dijalankan jika tidak terpenuhi fxy_minimum_selanjutnya yang dijalankan
    if index == 0 :
        fxy_minimum_iterasi1(xi["x0"],xi["x1"],xi["x2"],yi["y0"],yi["y1"],yi["y2"])
    else:
        fxy_minimum_selanjutnya(xi_before["x0"],xi["x0"],xi_before["x1"],xi["x1"],xi_before["x2"],xi["x2"],yi_before["y0"],yi["y0"],yi_before["y1"],yi["y1"],yi_before["y2"],yi["y2"])

    #Memanggil fungsi xy_minimum
    xy_mininum(Pbestix[0],Pbestix[1],Pbestix[2],Pbestiy[0],Pbestiy[1],Pbestiy[2])

    #update nilai vix berdasarkan fungsi vix_func
    for i in range(0,3):
        vix[f'v{i}'] = vix_func(vix[f'v{i}'],xi[f'x{i}'],i)
    # vix["v0"] = vix_func(vix["v0"],xi["x0"],0)
    # vix["v1"] = vix_func(vix["v1"],xi["x1"],1)
    # vix["v2"] = vix_func(vix["v2"],xi["x2"],2)
    
    #update nilai viy berdasarkan fungsi viy_func
    for i in range(0,3):
        viy[f'v{i}'] = viy_func(viy[f'v{i}'],yi[f'y{i}'],i)
    # viy["v0"] = viy_func(viy["v0"],yi["y0"],0)
    # viy["v1"] = viy_func(viy["v1"],yi["y1"],1)
    # viy["v2"] = viy_func(viy["v2"],yi["y2"],2)
    
    #Update nilai xi penampungan (xi_before) dengan nilai dari xi iterasi sekarang
    for i in range(0,3):
        xi_before[f'x{i}'] = xi[f'x{i}']
    # xi_before["x0"] = xi["x0"]
    # xi_before["x1"] = xi["x1"]
    # xi_before["x2"] = xi["x2"]
    
    #updata nilai dari xi iterasi sekarang'
    for i in range(0,3):
        xi[f'x{i}'] = xi_before[f'x{i}'] + vix[f'v{i}']
    # xi["x0"] = xi_before["x0"] + vix["v0"]
    # xi["x1"] = xi_before["x1"] + vix["v1"]
    # xi["x2"] = xi_before["x2"] + vix["v2"]
    
    #Update nilai yi penampungan (yi_before) dengan nilai dari yi iterasi sekarang
    for i in range(0,3):
        yi_before[f'y{i}'] = yi[f'y{i}']
    # yi_before["y0"] = yi["y0"]
    # yi_before["y1"] = yi["y1"]
    # yi_before["y2"] = yi["y2"]
    
    #update nilai dari yi iterasi sekarang
    for i in range(0,3):
        yi[f'y{i}'] = yi_before[f'y{i}'] + viy[f'v{i}']
    # yi["y0"] = yi_before["y0"] + viy["v0"]
    # yi["y1"] = yi_before["y1"] + viy["v1"]
    # yi["y2"] = yi_before["y2"] + viy["v2"]
    
    #Menampilkan nilai xi iterasi sekarang
    for i in range(0,3):
        print(f"Nilai (x{i},y{i}): {xi[f'x{i}']},"+f"{yi[f'y{i}']:.2f}")
        print(f"Nilai f(x{i},y{i}): {func(xi[f'x{i}'],yi[f'y{i}']):.2f}")
        print(f"Nilai vi(x{i},y{i}): {vix[f'v{i}']},"+f"{viy[f'v{i}']:.2f}")
        print()

print(f"Nilai Gbest: ({Gbestx:.2f}, {Gbesty:.2f})")
print(f"Nilai minimum f({Gbestx:.2f}, {Gbesty:.2f}): {func(Gbestx,Gbesty):.2f}")