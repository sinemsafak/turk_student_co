# Kullanıcı bilgilerini saklamak için kullanılan sınıf
class Kullanici:
    def __init__(self, ad, hesap_no, bakiye):
        self.ad = ad  # Kullanıcı adı
        self.hesap_no = hesap_no  # Hesap numarası
        self.bakiye = bakiye  # Kullanıcının hesabındaki bakiye

    def para_yatir(self, miktar):
        """Hesaba para yatırır."""
        self.bakiye += miktar

    def para_cek(self, miktar):
        """Hesaptan para çeker, yeterli bakiye varsa."""
        if miktar <= self.bakiye:
            self.bakiye -= miktar
        else:
            print("Yetersiz bakiye!")


# Banka işlemlerini yöneten sınıf
class Banka:
    def __init__(self):
        self.kullanicilar = {}  # Kullanıcıları hesap numarasına göre saklar

    def hesap_ac(self, ad, hesap_no, bakiye):
        """Yeni bir kullanıcı hesabı oluşturur."""
        self.kullanicilar[hesap_no] = Kullanici(ad, hesap_no, bakiye)

    def kullanici_bul(self, hesap_no):
        """Hesap numarasına göre kullanıcıyı bulur."""
        return self.kullanicilar.get(hesap_no)

    def islem_yap(self, hesap_no, islem_turu, miktar):
        """Kullanıcının hesabında belirtilen işlemi yapar."""
        kullanici = self.kullanici_bul(hesap_no)
        if kullanici:
            if islem_turu == "yatir":
                kullanici.para_yatir(miktar)
            elif islem_turu == "cek":
                kullanici.para_cek(miktar)
            else:
                print("Geçersiz işlem türü!")
        else:
            print("Kullanıcı bulunamadı.")
