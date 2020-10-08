liste3=[]
liste2= []
liste4 = []
def hesaplama(parametre):

    parametre=parametre[:-1] # alt alta boşluk olmadan gözükmesi için tersten siliyoruz

    liste = parametre.split(",") # split ile ayırmak istedigimiz şeyi söylüyoruz liste degişkenine atıyoruz

    isim = liste[0]  # isim degişkeninin listenin 0. parametresindeki degişkeni alacagını söylüyoruz
    notbir = int(liste[1])
    notiki = int(liste[2])
    notüç = int(liste[3])

    sondurum = notbir * (3/10) + notiki * (3/10) + notüç * (4/10) #hesaplama işlemini söylüyoruz

    if(sondurum>=90):
        harf = "AA"
        durum = "geçtiniz"
        liste3.append(isim + "---------------------------------" + harf +"\n"+ durum +"\n")

    elif(sondurum>=80):
        harf = "BA"
        durum = "geçtiniz"
        liste3.append(isim + "---------------------------------" + harf +"\n"+ durum +"\n")
    elif(sondurum>=70):
        harf = "BB"
        durum = "geçtiniz"
        liste3.append(isim + "---------------------------------" + harf +"\n"+ durum +"\n")
    elif(sondurum>=60):
        harf = "CB"
        durum = "geçtiniz"
        liste3.append(isim + "---------------------------------" + harf +"\n"+ durum +"\n")
    elif(sondurum>=50):
        harf="CC"
        durum = "geçtiniz"
        liste3.append(isim + "---------------------------------" + harf +"\n"+ durum +"\n")
    elif(sondurum>=40):
        harf = "DC"
        durum = "geçtiniz"
        liste3.append(isim + "---------------------------------" + harf +"\n"+ durum +"\n")
    else:
        harf = "FF"
        durum = "kaldınız"
        liste4.append(isim + "---------------------------------" + harf +"\n"+ durum +"\n")


    return isim + "---------------------------------" + harf +"\n"+ durum +"\n" # harf notlarını söyledikten sonra
                                                                  #return yaparak tabloyu güncelliyoruz

with open ("sınıf.txt","r",encoding="utf-8")as file:
    for i in file:
       liste2.append(hesaplama(i)) #yeni listeye eklemeyi gerçekleştirdik




    with open("sonuçlar.txt","w",encoding="utf-8")as  file2:
     for i in liste2:
          file2.write(i)  #yeni bi txt dosyası oluşturup gösterdik.
    with open("geçenler.txt", "w" , encoding="utf-8")as file3:
        for i in liste3:
            file3.write(i)

    with open("kalanlar.txt", "w", encoding="utf-8")as file4:
        for i in liste4:
            file4.write(i)