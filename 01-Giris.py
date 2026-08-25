
#? çıktı vermek için kullanılır
print ("Python Giris")

#? çıktı almak için kullanılır
input("Sayı gir: ")

#? değişkene atanan değer, değişkenin tipi olur
a = 1
a = "veysel"
print (a)

#? casting (tip belirleme)
x = str(7)
y = int(7)
z = float(7)

print(x, y ,z)

#? type() değişkenin tipini gösterir
print(type(x),type(y),type(z))

#? değişken oluşturma
#* değişkenler sadece büyük/küçük harfler ,sayılar ve _ işareti ile oluşturulabilir ve bir değişken sayı ile başlayamaz

#? variable unpacking
colors = ["white","red","grey","red","yellow"]
a,b,c,d,e = colors #! Destruct işlemidir ,React'ta vs. yaygın olarak kullanılır 
print(a,b,c,d,e)

#? output variables
#* + ile birleştirilirse otomatik aralarında boşluk olur, matematiksel işlemlerde de kullanılır 
#* , ile birleştirilirse aralarında boşluk olmaz 
degisken1 = "Şebnem"
degisken2 = "Ferah"
degisken3 = "Hoşçakal"
print(degisken1+degisken2+degisken3)
print(degisken1,degisken2,degisken3)


