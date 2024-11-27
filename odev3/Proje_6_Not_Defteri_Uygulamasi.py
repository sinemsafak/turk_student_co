import datetime

# Not bilgilerini tutan sınıf
class Not:
    def __init__(self, icerik):
        self.icerik = icerik  # Not içeriği
        self.tarih = datetime.datetime.now()  # Notun oluşturulma tarihi


# Not defteri işlemlerini yöneten sınıf
class NotDefteri:
    def __init__(self):
        self.notlar = []  # Notlar listesi

    def not_ekle(self, icerik):
        """Yeni bir not ekler."""
        self.notlar.append(Not(icerik))

    def notlari_listele(self):
        """Notları tarih sırasına göre listeler."""
        return [{"İçerik": not_.icerik, "Tarih": not_.tarih.strftime('%Y-%m-%d %H:%M:%S')} for not_ in self.notlar]

    def not_sil(self, index):
        """Belirli bir notu siler."""
        if 0 <= index < len(self.notlar):
            self.notlar.pop(index)
