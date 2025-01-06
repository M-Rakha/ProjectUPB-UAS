# Class Data

Berfungsi untuk merepresentasikan data mahasiswa.

Attributes:

- nama: Nama mahasiswa.

- nim: Nomor Induk Mahasiswa (NIM).

- tugas: Nilai tugas.

- uts: Nilai Ujian Tengah Semester (UTS).

- uas: Nilai Ujian Akhir Semester (UAS).

- nilai_akhir: Nilai akhir mahasiswa yang dihitung otomatis.

Method :

- hitung_nilai_akhir: Menghitung nilai akhir dengan formula

# Class Process

Berfungsi untuk memproses operasi pada data mahasiswa.

Attributes:

- mahasiswa_list: List yang menyimpan objek mahasiswa.

Methods:

- tambah_mahasiswa: Menambahkan data mahasiswa baru ke mahasiswa_list.

- hapus_mahasiswa Menghapus data mahasiswa berdasarkan NIM.

- ubah_mahasiswa: Mengubah data mahasiswa berdasarkan NIM (dapat mengubah sebagian data saja).

- cari_mahasiswa: Mencari data mahasiswa berdasarkan NIM.

# Class View

Berfungsi untuk menampilkan data ke pengguna.

Static Methods:

- tampilkan_menu: Menampilkan menu utama.

- tampilkan_mahasiswa: Menampilkan detail satu mahasiswa (jika ditemukan).

- tampilkan_semua: Menampilkan semua data mahasiswa dalam bentuk tabel menggunakan library tabulate.

# Fungsi main

Berfungsi sebagai titik masuk program dan mengatur alur kerja.

Alur Kerja:

- Tampilkan menu utama: Memanggil View.tampilkan_menu.

- Pilihan pengguna:

1: Tambah data mahasiswa (input data, lalu diproses dengan tambah_mahasiswa).

2: Tampilkan semua data mahasiswa (gunakan tampilkan_semua).

3: Hapus mahasiswa berdasarkan NIM (gunakan hapus_mahasiswa).

4: Ubah data mahasiswa (gunakan ubah_mahasiswa).

5: Cari mahasiswa berdasarkan NIM (gunakan cari_mahasiswa).

6: Keluar dari program.

- Jika pilihan tidak valid, akan ditampilkan pesan kesalahan.

## Hasil Code Data

![gambar](https://github.com/M-Rakha/ProjectUPB-UAS/blob/7605a666f857aee05ae1888e1e0328937c5ac345/class%20data%20code.png)

## Hasil Code View

![gambar](https://github.com/M-Rakha/ProjectUPB-UAS/blob/0ead244875f7fd173623bc61b56bc39c4720ac6c/class%20view%20code.png)

## Hasil Code Process

![gambar](https://github.com/M-Rakha/ProjectUPB-UAS/blob/63fc55f97a8aef695f85c3d03ea9ede3283e32ca/class%20process%20code.png)

## Hasil Code Main

![gambar](https://github.com/M-Rakha/ProjectUPB-UAS/blob/d0f4c140a1b1031d9c5e52955a5891af6e80472c/class%20main.py%20code.png)

## Hasil Run Main



