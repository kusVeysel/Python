
#? print()
#* çıktı vermek için kullanılır
print ("Python Giris")

#? input()
#* kullanıcıdan metin alır ve her zaman str döndürür; prompt metni ekrana yazılır
input("Sayı gir: ")

#? değişkene atanan değer, değişkenin tipi olur
a = 1
a = "veysel"
print(f"a değişkeninin tipi → {type(a)}, a → {a}")

#? casting (tip belirleme)
x = str(7)
y = int(7)
z = float(7)

print(x, y ,z)

#? type() değişkenin tipini gösterir
print(type(x), type(y), type(z))

#? Değişken Oluşturma
#* İsimler Unicode harfleri, rakamları ve "_" içerebilir; rakamla başlayamaz ve
#* Python anahtar kelimeleri isim olarak kullanılamaz.
# // 1degisken , yanlış
# degisken1 , doğru

#? Variable Unpacking
colors = ["white","red","grey","red","yellow"]
a,b,c,d,e = colors #! Destruct işlemidir ,React'ta vs. yaygın olarak kullanılır 
print(a,b,c,d,e)

#? Output Variables
#* + ile birleştirilirse aralarında boşluk olmaz, + matematiksel işlemlerde de kullanılır 
#* , ile birleştirilirse aralarında otomatik boşluk olur
 
degisken1 = "Şebnem"
degisken2 = "Ferah"
degisken3 = "Hoşçakal"
print(degisken1 + degisken2 + degisken3)
print(degisken1 , degisken2 , degisken3)
