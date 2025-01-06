from tabulate import tabulate

class View:
    def tampilkan_menu():
        print("==============================")
        print("|      Data Mahasiswa        |")
        print("==============================")
        print("| 1 | Tambah Data Mahasiswa  |")
        print("| 2 | Tampilkan Semua Data   |")
        print("| 3 | Hapus Data Mahasiswa   |")
        print("| 4 | Ubah Data Mahasiswa    |")
        print("| 5 | Cari Data Mahasiswa    |")
        print("| 6 | Keluar                 |")
        print("==============================")

    def tampilkan_mahasiswa(mahasiswa):
        if mahasiswa:
            print("\nData ditemukan:")
            print(f"Nama         : {mahasiswa.nama}")
            print(f"NIM          : {mahasiswa.nim}")
            print(f"Tugas        : {mahasiswa.tugas}")
            print(f"UTS          : {mahasiswa.uts}")
            print(f"UAS          : {mahasiswa.uas}")
            print(f"Nilai Akhir  : {mahasiswa.nilai_akhir:.2f}")
        else:
            print("Data tidak ditemukan.")

    def tampilkan_semua(mahasiswa_list):
        if not mahasiswa_list:
            print("\nBelum ada data mahasiswa.")
        else:
            print("\nData Mahasiswa:")
            print(tabulate(
                [(m.nama, m.nim, m.tugas, m.uts, m.uas, m.nilai_akhir) for m in mahasiswa_list],
                headers=("Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"),
                tablefmt="double_grid"
            )) 