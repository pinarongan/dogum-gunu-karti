from PIL import Image, ImageDraw, ImageFont

def kart_olustur(dogun_gunu_cocugu,kart_olusturan,bugunun_tarihi):
    # 2. ADIM: Kartın arka planını oluşturalım.
    arka_plan = Image.open("arka-plan.png").convert("RGBA")  # "arka plan" dosyasını açar
    kart_sablonu = arka_plan.resize((int(arka_plan.width/2), int(arka_plan.height/2)))   # arka planı yeniden boyutlandırarak kart şablonunu oluşturur
    hazir_sablon = ImageDraw.Draw(kart_sablonu)        # kart şablonumuz, üzerine bilgi girilecek şekle getirilir

    # 3. ADIM: Kartın üzerine notumuzu yazalım.
    font = ImageFont.truetype('segoescb.ttf', size=15)     # bilgileri girerken kullanacağımız font ve yazı boyutunu seçer
    alinti_siir = "\"\'Öyle güzelsin ki, kuş koysunlar yoluna\'\nbir çocuk demiş.\""
    sair = "Nilgün Marmara"
    hazir_sablon.text((20, 17), alinti_siir, font=font, fill='black')
    hazir_sablon.text((250, 52), sair, font=font, fill='black')

    font = ImageFont.truetype('calibril.ttf', size=17)     # bilgileri girerken kullanacağımız font ve yazı boyutunu seçer
    tarih = bugunun_tarihi
    mesaj_kime = dogun_gunu_cocugu
    mesaj_kimden = kart_olusturan
    mesaj = "Sevgili "+mesaj_kime+", \n\nİyi ki varsın ve iyi ki kesişti yollarımız. \nSana güzelliğini her daim hatırlatacak olan\nkuşlarla çevrili bir ömür diliyorum. \nDoğum günün kutlu olsun."
    hazir_sablon.text((280, 100), tarih, font=font, fill='black')
    hazir_sablon.text((50, 120), mesaj, font=font, fill='black')
    hazir_sablon.text((322, 225), mesaj_kimden, font=font, fill='black')
    kart_sablonu.save("dogumgunukarti.png")

# 1. ADIM: Gerekli bilgileri kullanıcıdan alalım.
kime = input("Bu kartı kim için hazırlıyorsunuz?\n")
tarih = input("Karta atmak istediğiniz tarih:\n")
kimden = input("İsminiz:\n")
kart_olustur(kime,kimden,tarih)