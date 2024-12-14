# 🔵Tugas Akhir Mata Kuliah Pengantar Probabilitas dan Optimasi

## 🔴Particle Swarm Optimization (PSO)
Particle Swarm Optimization (PSO) adalah algoritma optimasi berbasis metaheuristik yang meniru perilaku sosial kelompok, seperti kawanan burung atau ikan, untuk menemukan solusi optimal dalam sebuah ruang pencarian.
PSO pertama kali diperkenalkan oleh Kennedy dan Eberhart pada tahun 1995 dan digunakan secara luas dalam berbagai aplikasi optimasi.

### Konsep Dasar
PSO melibatkan partikel-partikel yang bergerak dalam ruang pencarian untuk menemukan solusi terbaik. Setiap partikel merepresentasikan kandidat solusi dan memiliki atribut:

1. Posisi (𝑥): Merepresentasikan solusi saat ini.
2. Kecepatan (𝑣): Menentukan arah dan jarak pergerakan partikel.
3. Personal Best (𝑝best): Posisi terbaik yang pernah dicapai partikel.
4. Global Best (𝑔best): Posisi terbaik yang pernah dicapai oleh semua partikel dalam populasi.

### Mekanisme Kerja
PSO menggunakan iterasi untuk memperbarui posisi dan kecepatan partikel. Prosesnya meliputi:
1. Inisialisasi:
   * Tentukan jumlah partikel.
   * Inisialisasi posisi dan kecepatan secara acak dalam ruang pencarian.
2. Evaluasi:
   * Hitung nilai fungsi objektif untuk setiap partikel berdasarkan posisinya.
3. Perbarui Posisi Terbaik:
   * Perbarui 𝑝best jika posisi saat ini lebih baik dari posisi terbaik sebelumnya.
   * Perbarui 𝑔best jika ada partikel dengan posisi yang lebih baik dari 𝑔best.
4. Perbarui Kecepatan dan Posisi: Kecepatan setiap partikel diperbarui menggunakan formula:
   ```
   vi = w ⋅ vi + c1 ⋅ r1 ⋅ (pbest,i − xi) + c2 ⋅ r2 ⋅ (gbest − xi)
   ```
   * w: Inersia untuk mengontrol pengaruh kecepatan sebelumnya.
   * 𝑐1,𝑐2: Faktor akselerasi untuk menarik partikel ke 𝑝best dan 𝑔best.
   * 𝑟1,𝑟2: Bilangan acak antara 0 dan 1.

Posisi diperbarui menggunakan formula:
  ```
  𝑥𝑖=𝑥𝑖 + 𝑣𝑖
  ```
 
5. Cek Kriteria Penghentian:
   * Iterasi dihentikan jika tercapai jumlah iterasi maksimum atau solusi optimal ditemukan.
6. Ulangi:
   * Lakukan proses dari evaluasi hingga perbaruan kecepatan dan posisi sampai kriteria penghentian terpenuhi.

## 🔴Algoritma Djikstra
Algoritma Dijkstra adalah algoritma yang digunakan untuk menemukan jalur terpendek dari satu simpul (node) ke semua simpul lain dalam graf berbobot.
Algoritma ini dirancang oleh Edsger W. Dijkstra pada tahun 1956 dan sering digunakan dalam aplikasi seperti sistem navigasi, jaringan komputer, dan perencanaan rute.

### Karakteristik Algoritma
1. Graf yang digunakan
   * Graf berbobot(weighted graph), di mana setiap sisi memiliki bobot atau jarak
   * Bobot tidak boleh negatif (karena sifat algoritma tidak mendukung)
2. Sifat Jalur Pendek
   * Algoritma ini memastikan bahwa jalur terpendek dari simpul awal ke simpul lain ditemukan dengan menggunakan bobot terkecil
3. Metode
   * Menggunakan pendekatan greedy untuk memilih simpul yang memiliki jarak terkecil dari simpul awal pada setiap langkah
### Langkah-langkah Algoritma Djikstra
1. Inisialisasi:
   * Tetapkan jarak awal dari simpul awal ke dirinya sendiri sebagai ``` 0 ```.
   * Tetapkan jarak ke semua simpul lain sebagai ``` ∞ ```
   * Simpan semua simpul yang belum dikunjungi
2. Pilih Simpul dengan Jarak Terpendek:
   * Pilih simpul yang belum dikunjungi dengan jarak minimum dari simpul awal.
   * Tandai simpul ini sebagai telah dikunjungi
3. Perbarui Jarak:
   * Untuk setiap simpul tetangga dari simpul yang dipilih, perbarui jaraknya jika jalur baru melalui simpul ini lebih dari pendek
     dibandingkan jalur sebelumnya.
4. Ulangi
   * Ulangi langkah 2 dan 3 hingga semua simpul telah dikunjungi atau jarak ke simpul tujuan ditemukan
5. Hasil Akhir
   * Setelah selesai, jarak terpendek ke semua simpul dari simpul awal tersedia
  
### Contoh
Misalkan ada graf seperti berikut:
```
A ---1--- B
|         |
4         2
|         |
C ---1--- D
```

  * Simpul awal: ``` A ```
  * Tujuan: Semua simpul lain.

Langkah:
1. Inisialisasi Jarak:
   ```
   A = 0, B = ∞ , C = ∞, D = ∞
   ```
2. Pilih ```A```(jarak 0), perbarui jarak tetangganya:
   ```
   B = 1, C = 4, D = ∞
   ```
3. Pilih ```B```(jarak 1), perbarui jarak tetangganya:
   ```
   C = 4, D = 3
   ```
4. Pilih ```D```(jarak 3), tidak ada pembaruan karena semua tetangga sudah diperiksa
5. Pilih ```C```(jarak 4), selesai.

Hasil:
```
A -> B : 1
A -> C : 4
A -> D : 3
```
