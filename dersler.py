#6.SORU A SIKKI:
#sözlük olusturarak derslerin kacıncı sınıfa ait oldugunu bulma
# oncelikle dersleri yazip (key) karsisina  sınıf degerini atıyoruz(value)
dersler={"Hukukun Temel Kavramları":"1.sınıf",
"Muhasebenin temel ilkeleri":"1.sınıf",
"İstatistik":"2.sınıf",
"e-ticaret":"2.sınıf",
"sistem analizi":"3.sınıf",
"gorsel programlama":"3.sınıf"}

ders_adi = input("Bir ders adi girip kaçıncı sınıfa ait oldugunu ogrenin: ")
#ders adini isteyip kacıncı sınıfa ait oldugunu ogrenecegiz
sinif = "{} dersi {} 'a aittir"

print(sinif.format(ders_adi, dersler[ders_adi]))
print()

#B SIKKI:
#iki liste olusturup bu listeleri birbirlerine ekleme
liste1=["Berna","Sevval","Uysal"]
liste2=[1,2,3]
liste1.append(liste2) #append listeyi ekleme komutudur
print(liste1)