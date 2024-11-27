# Film bilgilerini tutan sınıf
class Film:
    def __init__(self, ad, yonetmen, yil, tur):
        self.ad = ad  # Film adı
        self.yonetmen = yonetmen  # Yönetmen adı
        self.yil = yil  # Çıkış yılı
        self.tur = tur  # Film türü


# Film yönetimi işlemlerini yöneten sınıf
class FilmYoneticisi:
    def __init__(self):
        self.filmler = []  # Film listesi

    def film_ekle(self, ad, yonetmen, yil, tur):
        """Yeni bir film ekler."""
        self.filmler.append(Film(ad, yonetmen, yil, tur))

    def filmleri_listele(self, filtre=None, deger=None):
        """Filmleri belirtilen kritere göre filtreler ve listeler."""
        if filtre == "tur":
            return [film.ad for film in self.filmler if film.tur == deger]
        elif filtre == "yil":
            return [film.ad for film in self.filmler if film.yil == deger]
        return [film.ad for film in self.filmler]

    def film_sil(self, ad):
        """Belirtilen adı taşıyan filmi siler."""
        self.filmler = [film for film in self.filmler if film.ad != ad]
