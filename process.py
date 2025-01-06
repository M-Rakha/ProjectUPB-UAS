from data.data import Data

class Process:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, nama, nim, tugas, uts, uas):
        mahasiswa = Data(nama, nim, tugas, uts, uas)
        self.mahasiswa_list.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nim == nim:
                self.mahasiswa_list.remove(mahasiswa)
                return mahasiswa
        return None

    def ubah_mahasiswa(self, nim, nama=None, tugas=None, uts=None, uas=None):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nim == nim:
                if nama:
                    mahasiswa.nama = nama
                if tugas is not None:
                    mahasiswa.tugas = tugas
                if uts is not None:
                    mahasiswa.uts = uts
                if uas is not None:
                    mahasiswa.uas = uas
                mahasiswa.nilai_akhir = mahasiswa.hitung_nilai_akhir()
                return mahasiswa
        return None

    def cari_mahasiswa(self, nim):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None 