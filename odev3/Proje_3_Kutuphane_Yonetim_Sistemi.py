# Kitap bilgilerini tutan sınıf
class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad  # Kitap adı
        self.yazar = yazar  # Yazar adı
        self.odunc_alindi = False  # Ödünç alınıp alınmadığını belirtir

    def odunc_al(self):
        """Kitabı ödünç alır."""
        if not self.odunc_alindi:
            self.odunc_alindi = True
        else:
            print(f"{self.ad} zaten ödünç alınmış.")

    def geri_ver(self):
        """Kitabı geri verir."""
        self.odunc_alindi = False


# Kütüphane işlemlerini yöneten sınıf
class Kutuphane:
    def __init__(self):
        self.kitaplar = []  # Kütüphanedeki kitapları saklar

    def kitap_ekle(self, ad, yazar):
        """Yeni kitap ekler."""
        self.kitaplar.append(Kitap(ad, yazar))

    def kitaplari_listele(self):
        """Kitapları mevcut ve ödünç alınanlar olarak listeler."""
        mevcut = [kitap.ad for kitap in self.kitaplar if not kitap.odunc_alindi]
        odunc = [kitap.ad for kitap in self.kitaplar if kitap.odunc_alindi]
        return {"Mevcut Kitaplar": mevcut, "Ödünç Alınan Kitaplar": odunc}
