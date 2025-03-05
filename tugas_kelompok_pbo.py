class Televisi:
    def __init__(self, ukuran_layar, warna_layar, type_tv):
        self.ukuran_layar = ukuran_layar
        self.warna_layar = warna_layar
        self.type_tv = type_tv

    def dimatikan_dihidupkan(self):
        print(f'{self.type_tv} telah dihidupkan')
        print(f'TV ini memiliki warna layar {self.warna_layar} dan memiliki ukuran layar {self.ukuran_layar} inci')

    def naik_turun_volume(self):
        print(f'Tekan tombol volume pada remote untuk menaikkan atau menurunkan volume pada TV {self.type_tv}')

    def mencari_chanel(self):
        print(f'Tekan tombol angka pada remote untuk mengganti channel pada TV {self.type_tv}')

Televisi_A = Televisi(32, 'SRGB 86%', 'Samsung')
Televisi_B = Televisi(42, 'SRGB 68%', 'LG')

Televisi_A.dimatikan_dihidupkan()
Televisi_A.naik_turun_volume()
Televisi_A.mencari_chanel()

Televisi_B.dimatikan_dihidupkan()
Televisi_B.naik_turun_volume()
Televisi_B.mencari_chanel()
