blok_sayisi = int(input("Blok sayısını giriniz: "))

yukseklik = 0
kullanilan_blok = 0
kat = 1

while kullanilan_blok + kat <= blok_sayisi:
    kullanilan_blok += kat
    yukseklik += 1
    kat += 1

print("Piramidin yüksekliği:", yukseklik)
