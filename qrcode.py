import urllib.parse
import urllib.request

print("/n")

size = input("Resim boyutu : ")

veri = input("İçerik : ")

veriler = {

    'size': size + "x" + size,
    'data': veri

}

parametreler = urllib.parse.urlencode(veriler)

api_link = "https://api.qrserver.com/v1/create-qr-code/?" + parametreler

urllib.request.urlretrieve(api_link, "kare_kod.png")

print("/n")
print("Kare kod başarıyla oluşturuldu.")
print("kare_kod.png isimli dosyadan ulaşabilirsiniz.")
print("/n")
