from view.view import View
from process.process import Process

def main():
    proses = Process()

    while True:
        View.tampilkan_menu()
        pilihan = input("Masukkan Pilihan Menu = ").strip()

        if pilihan == "1":
            print("\n==============================")
            print("|   Masukkan Data Mahasiswa  |")
            print("==============================")
            nama = input("Masukkan Nama         = ").strip()
            nim = input("Masukkan NIM          = ").strip()
            tugas = float(input("Masukkan Nilai Tugas  = ").strip())
            uts = float(input("Masukkan Nilai UTS    = ").strip())
            uas = float(input("Masukkan Nilai UAS    = ").strip())
            proses.tambah_mahasiswa(nama, nim, tugas, uts, uas)
            print("\nData mahasiswa berhasil ditambahkan!")

        elif pilihan == "2":
            View.tampilkan_semua(proses.mahasiswa_list)

        elif pilihan == "3":
            nim = input("Masukkan NIM yang Ingin Dihapus = ").strip()
            mahasiswa = proses.hapus_mahasiswa(nim)
            if mahasiswa:
                print(f"Data mahasiswa dengan NIM '{nim}' berhasil dihapus.")
            else:
                print(f"Data mahasiswa dengan NIM '{nim}' tidak ditemukan.")

        elif pilihan == "4":
            nim = input("Masukkan NIM yang Ingin Diubah = ").strip()
            nama = input("Masukkan Nama Baru (Kosongkan jika tidak diubah) = ").strip()
            tugas = input("Masukkan Nilai Tugas Baru (Kosongkan jika tidak diubah) = ").strip()
            uts = input("Masukkan Nilai UTS Baru (Kosongkan jika tidak diubah) = ").strip()
            uas = input("Masukkan Nilai UAS Baru (Kosongkan jika tidak diubah) = ").strip()

            mahasiswa = proses.ubah_mahasiswa(
                nim,
                nama or None,
                float(tugas) if tugas else None,
                float(uts) if uts else None,
                float(uas) if uas else None
            )

            if mahasiswa:
                print(f"Data mahasiswa dengan NIM '{nim}' berhasil diubah.")
            else:
                print(f"Data mahasiswa dengan NIM '{nim}' tidak ditemukan.")

        elif pilihan == "5":
            nim = input("Masukkan NIM yang Dicari = ").strip()
            mahasiswa = proses.cari_mahasiswa(nim)
            View.tampilkan_mahasiswa(mahasiswa)

        elif pilihan == "6":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()