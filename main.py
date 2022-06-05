import string
import urllib.parse
import urllib.request
import secrets

print("/n")

size = input("Resim boyutu : ")

veri = input("İçerik : ")

veriler = {

    'size': size + "x" + size,
    'data': veri

}

parametreler = urllib.parse.urlencode(veriler)

#karekod=f'{veri}{secrets.token_hex(5)}'
#karekod="%silbey" % parametreler
karekod=f"ilbey{veri}aktorun{size}"

api_link = "https://api.qrserver.com/v1/create-qr-code/?" + parametreler

urllib.request.urlretrieve(api_link, karekod+".png")


print("/n")
print("Kare kod başarıyla oluşturuldu.")
print("kare_kod.png isimli dosyadan ulaşabilirsiniz.")
print("/n")

