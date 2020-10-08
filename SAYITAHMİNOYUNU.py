
import random
import time
print("""
       Merhaba sayı tahmin oyununa hoş geldiniz
       1 ile 50 arasında ki sayıyı tahmin etmeye çalışıcaksınız 
       hazırsan sayını gir...

""")
rastgeleSayı = random.randint(1,50)
tahmin_hakkı = 10
while True:
   tahminSayısı = int (input("sayıyı giriniz"))
   if(tahminSayısı == 0):
       print("Çıkış yapılıyor...")
       break
   if(tahminSayısı < rastgeleSayı):
             print("Sayı kontrol ediliyor...")
             time.sleep(1)
             tahmin_hakkı-=1
             print("Sayıyı arttırın...")
   elif(tahminSayısı > rastgeleSayı):
             print("Sayı kontrol ediliyor...")
             time.sleep(1)
             tahmin_hakkı-=1
             print("Sayıyı küçültün")
   elif (tahminSayısı == rastgeleSayı):
             print("Sayı kontrol ediliyor...")
             time.sleep(1)
             print("Tebrikler bildiniz...")
             break
   elif(tahmin_hakkı ==0):
             print("Hak durumu kontrol ediliyor...")
             time.sleep(2)
             print("Hakkınız dolmuştur katıldıgınız için teşekkür ederiz...")


