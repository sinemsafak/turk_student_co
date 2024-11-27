# Ürün bilgilerini tutan sınıf
class Urun:
    def __init__(self, ad, fiyat, miktar):
        self.ad = ad  # Ürün adı
        self.fiyat = fiyat  # Ürün fiyatı
        self.miktar = miktar  # Ürün miktarı


# Alışveriş sepeti işlemlerini yöneten sınıf
class Sepet:
    def __init__(self):
        self.urunler = []  # Sepetteki ürünler listesi

    def urun_ekle(self, ad, fiyat, miktar):
        """Yeni bir ürün ekler."""
        self.urunler.append(Urun(ad, fiyat, miktar))

    def urun_cikar(self, ad):
        """Sepetten belirtilen ürünü çıkarır."""
        self.urunler = [urun for urun in self.urunler if urun.ad != ad]

    def toplam_tutar(self):
        """Sepetteki ürünlerin toplam tutarını hesaplar."""
        return sum(urun.fiyat * urun.miktar for urun in self.urunler)

    def sepet_listele(self):
        """Sepetteki ürünleri listeler."""
        return [{"Ad": urun.ad, "Fiyat": urun.fiyat, "Miktar": urun.miktar} for urun in self.urunler]
