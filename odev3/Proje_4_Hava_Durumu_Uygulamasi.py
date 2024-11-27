# Şehir ve sıcaklık bilgilerini tutan sınıf
class Sehir:
    def __init__(self, ad, sicaklik):
        self.ad = ad  # Şehir adı
        self.sicaklik = sicaklik  # Şehir sıcaklık bilgisi


# Hava durumu uygulamasını yöneten sınıf
class HavaDurumu:
    def __init__(self):
        self.sehirler = {}  # Şehirleri saklayan sözlük

    def sehir_ekle(self, ad, sicaklik):
        """Yeni bir şehir ekler."""
        self.sehirler[ad] = Sehir(ad, sicaklik)

    def hava_durumu(self, ad):
        """Belirli bir şehrin hava durumu bilgilerini döner."""
        sehir = self.sehirler.get(ad)
        if sehir:
            return self.tavsiye(sehir.sicaklik)
        return "Şehir bulunamadı."

    def tavsiye(self, sicaklik):
        """Sıcaklık değerine göre giyim önerisi yapar."""
        if sicaklik < 0:
            return "Soğuk, sıkı giyinin."
        elif 0 <= sicaklik < 15:
            return "Serin, mont almayı unutmayın."
        else:
            return "Hava güzel, rahat giyin."
