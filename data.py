class Data:
    def __init__(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts 
        self.uas = uas
        self.nilai_akhir = self.hitung_nilai_akhir()
                
    def hitung_nilai_akhir(self):
        return(self.tugas * 0.3) + (self.uts * 0.35) + (self.uas * 0.35)