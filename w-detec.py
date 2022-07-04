import requests
import time

# Renkler
sifirla = "\033[0m"
kirmizi = "\033[1;31m"
yesil = "\033[1;32m"
cyan = "\033[1;36m"

# Semboller
arti = yesil + "[" + kirmizi + "+" + yesil + "]"
eksi = yesil + "[" + kirmizi + "-" + yesil + "]"
bulundu = yesil + "[" + kirmizi + "BULUNDU" + yesil + "]" + sifirla
soru_isareti = yesil + "[" + kirmizi + "?" + yesil + "]"
unlem = yesil + "[" + kirmizi + "!" + yesil + "]"



def kontrol():
    istek = requests.get("https://ipinfo.io/")
    if (istek.status_code == 200):
        print(arti + " Sunucu Çevrimiçi")
        time.sleep(1)
   
    else:
        print(eksi + " Sunucu Çevrimdışı")
        time.sleep(1)
        print(eksi + " Programdan Çıkılıyor")
        time.sleep(1)
        exit()



print(kirmizi + "\n.:: Coded By wolkan ::.")
kontrol()
time.sleep(1)


try:
    while True:
        ip = input(soru_isareti + " Hedef IP: " + sifirla)
        time.sleep(1)

        hostname = requests.get("https://ipinfo.io/{}/hostname".format(ip)).text
        city = requests.get("https://ipinfo.io/{}/city".format(ip)).text
        region = requests.get("https://ipinfo.io/{}/region".format(ip)).text
        country = requests.get("https://ipinfo.io/{}/country".format(ip)).text
        location = requests.get("https://ipinfo.io/{}/loc".format(ip)).text
        organization = requests.get("https://ipinfo.io/{}/org".format(ip)).text
        postal = requests.get("https://ipinfo.io/{}/postal".format(ip)).text
        time_zone = requests.get("https://ipinfo.io/{}/timezone".format(ip)).text

        print("""{} Alan Adı: {}{} Şehir: {}{} Bölge: {}{} Ülke: {}{} Lokasyon: {}{} Organizasyon: {}{} Posta: {}{} Zaman Dilimi: {}""".format(bulundu,hostname,bulundu,city,bulundu,region,bulundu,country,bulundu,location,bulundu,organization,bulundu,postal,bulundu,time_zone))
        soru = input(soru_isareti + " Yeni bir sorgu yapmak ister misiniz? (e/h) " + sifirla)
        time.sleep(1)
        
        if (soru == "e"):
            continue

        else:
            print(eksi + " Programdan Çıkılıyor")
            time.sleep(1)
            exit()

except KeyboardInterrupt:
    print("\n" + eksi + " Programdan Çıkılıyor")
    time.sleep(1)
    exit()