 #? FILE HANDLING (Dosya İşlemleri)

#* Python'da dosyalar open() fonksiyonu ile açılır
#* open() kullanılırken temel olarak: open("dosya_yolu", "mod", encoding="...")

#* Örnek: open("dosya.txt", "r", encoding="utf-8")
# encoding="utf-8" türkçe karakterlerin düzgün çalışması için kullanılır


#? DOSYA AÇMA MODLARI

#* r → Read (Okuma)
#* Dosyayı okumak için kullanılır
#* Dosya yoksa FileNotFoundError verir
#* Dosya varsa içeriği okunabilir
#* r modunda dosyaya yazılamaz


#* w  → Write (Yazma)
#* Dosyaya yazmak için kullanılır
#* Dosya yoksa oluşturulur
#* Dosya varsa mevcut içeriğin TAMAMI SİLİNİR ve yeniden yazılır
#* Yani w = var olan içeriği sil + yeni içerik yaz


#* a  → Append (Sona ekleme)
#* Dosyanın sonuna veri eklemek için kullanılır
#* Dosya yoksa oluşturulur
#* Dosya varsa mevcut içerik silinmez
#* Yeni veri dosyanın sonuna eklenir
#* Yani a = mevcut içeriği koru + sona ekle


#* x  → Create (Oluşturma)
#* Yeni bir dosya oluşturur
#* Dosya yoksa oluşturulur
#* Dosya zaten varsa FileExistsError verir
#* Var olan dosyanın üzerine yazmaz


#? + İŞARETİ

#* + işareti dosyanın hem okunabilir hem yazılabilir olarak açılmasını sağlar.

#* r+ → Okuma + Yazma
#* Dosya MUTLAKA mevcut olmalıdır
#* Dosya yoksa FileNotFoundError verir
#* Mevcut içerik açılırken silinmez
#* Hem read hem write yapılabilir
#! Önemli: r+ dosyanın içeriğini otomatik olarak silmez. Üstüne yazar


#* w+ → Yazma + Okuma
#* Dosya yoksa oluşturulur
#* Dosya varsa açılırken mevcut içeriğin TAMAMI SİLİNİR
#* Hem yazma hem okuma yapılabilir
#* w+ = w + read özelliği


#* a+ → Sona ekleme + Okuma
#* Dosya yoksa oluşturulur
#* Dosya varsa mevcut içerik korunur
#* Yazma işlemleri dosyanın SONUNA yapılır
#* Hem okuma hem yazma yapılabilir
#! Önemli: a+ ile dosya açıldığında dosya konumu başlangıçta genellikle dosyanın sonundadır Bu yüzden okumak için çoğu durumda seek(0) kullanılır


#* x+ → Oluşturma + Okuma/Yazma
#* Yeni dosya oluşturur
#* Dosya zaten varsa FileExistsError verir
#* Hem okuma hem yazma yapılabilir


#? MODLARIN KISA TABLOSU

#* r   → oku
#* w   → yaz, eski içeriği sil
#* a   → sona ekle
#* x   → yeni dosya oluştur

#* r+  → oku + yaz
#* w+  → yaz + oku, eski içeriği sil
#* a+  → sona ekle + oku
#* x+  → yeni oluştur + oku/yaz


import os

print("------------------------------------------")
#? OPEN()
#* Dosyayı açma

f = open("39-DosyaIsleme/Dosyalar/dosya.txt", "r", encoding="utf-8")
#* encoding="utf-8": Türkçe karakterler (ç, ğ, ı, İ, ö, ş, ü) gibi karakterlerin doğru şekilde okunup/yazılmasına yardımcı olur


#? read()
#* Dosyanın tamamını okur ve string olarak döndürür

print("f.read() →",f.read())

f.seek(0)
print("f.read(10) →",f.read(10))
#* read(sayi): Belirtilen miktarda karakter okur.
#* Örneğin: f.read(10)
#* Dosyanın bulunduğu mevcut konumdan itibaren 10 karakter okur.


print("------------------------------------------")
#? tell()
#* Dosya imlecinin/konumunun kaçıncı pozisyonda olduğunu döndürür
#* Dönen değer byte cinsinden konumu ifade eder

#* Özellikle encoding kullanıldığında tell() değerini doğrudan "kaç karakter okundu" şeklinde düşünmemek gerekir

print("f.tell() →",f.tell())


print("------------------------------------------")
#? seek()
#* Dosya imlecinin konumunu değiştirir

#* seek(0): Dosyanın başına gider

f.seek(0)

print("f.seek(0) f.read(10) →",f.read(10))


print("------------------------------------------")
#? readline()
#* Dosyadan bir satır okur
#* String olarak döndürür
#* Her çağrıldığında bir sonraki satıra geçer

f.seek(0)
print("f.readline() →",f.readline())
print("f.readline() →",f.readline())


print("------------------------------------------")
#? readlines()
#* Dosyanın satırlarını okur. Liste olarak döndürür
#* Örnek sonuç: ["Birinci satır\n", "İkinci satır\n", "Üçüncü satır\n"]

f.seek(0)
print("f.readlines() →",f.readlines())


print("------------------------------------------")
#? ITERATION
#* Dosya nesnesi üzerinde for döngüsü ile de satır satır dolaşabiliriz.

f.seek(0)

for satir in f:
    print(satir)


print("------------------------------------------")
#? readable()
#* Dosyanın okuma işlemine izin verip vermediğini True / False olarak döndürür.

print("f.readable() →",f.readable())


print("------------------------------------------")
#? writable()
#* Dosyanın yazma işlemine izin verip vermediğini True / False olarak döndürür.

print("f.writable() →",f.writable())


print("------------------------------------------")
#? seekable()
#* Dosya üzerinde seek() ile konum değiştirmenin mümkün olup olmadığını True / False olarak döndürür.

print("f.seekable() →",f.seekable())


print("------------------------------------------")
#? closed
#* Dosyanın kapalı olup olmadığını gösterir.
#* True  → kapalı
#* False → açık

print("f.closed →",f.closed)


print("------------------------------------------")
#? close()
#* Dosyayı manuel olarak kapatır. Dosya ile işimiz bittikten sonra kapatılması gerekir.

f.close()

print("f.close() f.closed →",f.closed)


print("------------------------------------------")
#? WITH

#* with open(...) kullanımı dosya işlemlerinde en güvenli ve önerilen yöntemlerden biridir
#* with bloğu sona erdiğinde dosya otomatik olarak kapatılır. Böylece close() yazmayı unutma problemi ortadan kalkar

with open("39-DosyaIsleme/Dosyalar/dosya.txt", "r", encoding="utf-8") as f:
    print(f.read())

#* with bloğu bittikten sonra dosya otomatik kapanır


print("------------------------------------------")
#? WRITE()
#* write() dosyaya string veri yazar. Yazılan karakter sayısını döndürebilir

with open("39-DosyaIsleme/Dosyalar/dosya2.txt", "w", encoding="utf-8") as f:
    print('f.write("Yavaş yavaş ilerliyoruz\n") →',f.write("Yavaş yavaş ilerliyoruz\n"))


#? WRITELINES()

#* writelines() birden fazla stringi dosyaya yazar. Kendisi otomatik olarak \n eklemez. Bu nedenle satır sonlarını kendimiz vermeliyiz

with open("39-DosyaIsleme/Dosyalar/dosya2.txt", "w", encoding="utf-8") as f:
    f.writelines([
        "Python\n",
        "JavaScript\n",
        "C#\n"
    ])


print("------------------------------------------")
#? TRUNCATE()

#* truncate() dosyanın boyutunu belirtilen BYTE miktarına düşürmek/kesmek için kullanılır
#! ÖNEMLİ: truncate(10), "10 karakter oku" anlamına GELMEZ. Dosyayı 10 BYTE uzunluğunda bırakır
#* Dosya daha uzunsa 10 byte'dan sonrası silinir
#* Dosya daha kısaysa dosya 10 byte'a kadar genişletilebilir ve araya null byte (\x00) gelebilir
#* truncate() yazma yetkisi olan dosyalarda kullanılmalıdır

with open("39-DosyaIsleme/Dosyalar/dosya.txt", "r+", encoding="utf-8") as f:
    print(os.stat("39-DosyaIsleme/Dosyalar/dosya.txt").st_size)

    f.truncate(10)

    f.seek(0)
    print(f.read())


print("------------------------------------------")
#? DOSYA BOYUTU

#* os.stat() dosya hakkında çeşitli bilgiler verir.
#* st_size → dosyanın boyutunu BYTE olarak verir.

print('os.stat("39-DosyaIsleme/Dosyalar/dosya.txt").st_size →',os.stat("39-DosyaIsleme/Dosyalar/dosya.txt").st_size)


print("------------------------------------------")
#? FILENO()
#* fileno() dosyanın işletim sistemi seviyesindeki file descriptor (dosya tanımlayıcısı) numarasını döndürür
#* Bu numara işletim sisteminin açık dosyayı takip etmek için kullandığı sayısal tanımlayıcıdır
#* Günlük Python dosya işlemlerinde çok sık kullanılmaz
#* Daha çok işletim sistemi seviyesindeki işlemlerde kullanılır

with open("39-DosyaIsleme/Dosyalar/dosya.txt", "r", encoding="utf-8") as f:
    print(f.fileno())


#? FLUSH()
#* Python dosyaya yazarken veriyi her zaman anında fiziksel olarak dosyaya göndermeyebilir.
#* Veriler buffer (tampon) içerisinde tutulabilir.
#* flush() buffer'daki bekleyen verilerin dosyaya gönderilmesini ister.
#* Özellikle dosyaya yazma işlemi devam ederken verinin bekletilmeden gönderilmesini istediğimiz durumlarda kullanılabilir.

with open("39-DosyaIsleme/Dosyalar/dosya.txt", "w", encoding="utf-8") as f:
    f.write("Bu veri buffer'a alınabilir.")

    f.flush()

    #* Burada bekleyen yazma işleminin dosyaya gönderilmesi istenir.


print("------------------------------------------")
#? r+ ÖRNEĞİ

#* r+:
#* - Dosya mevcut olmalı
#* - Okuma yapılabilir
#* - Yazma yapılabilir
#* - Eski içerik otomatik silinmez

with open("39-DosyaIsleme/Dosyalar/dosya.txt", "r+", encoding="utf-8") as f:
    print(f.read())

    f.seek(0)
    f.write("YENİ")

    f.seek(0)
    print(f.read())


print("------------------------------------------")
#? w+ ÖRNEĞİ

#* w+:
#* - Dosya yoksa oluşturulur
#* - Dosya varsa eski içerik açılışta silinir
#* - Okuma yapılabilir
#* - Yazma yapılabilir

with open("39-DosyaIsleme/Dosyalar/dosya3.txt", "w+", encoding="utf-8") as f:
    f.write("Python")

    f.seek(0)

    print(f.read())


print("------------------------------------------")
#? a+ ÖRNEĞİ

#* a+:
#* - Dosya yoksa oluşturulur
#* - Eski içerik silinmez
#* - Yeni veri sona eklenir
#* - Okuma yapılabilir

#* ÖNEMLİ:
#* Okumaya başlamadan önce seek(0) kullanmak gerekir.

with open("39-DosyaIsleme/Dosyalar/dosya4.txt", "a+", encoding="utf-8") as f:
    f.write("Python\n")

    f.seek(0)

    print(f.read())


#? x ÖRNEĞİ

#* x: Sadece yeni dosya oluşturmak istediğimizde kullanılır. Dosya zaten varsa hata verir.

try:
    with open("39-DosyaIsleme/Dosyalar/yeni_dosya.txt", "x", encoding="utf-8") as f:
        f.write("Yeni dosya oluşturuldu.")
except FileExistsError:
    print("Dosya zaten mevcut.")


print("------------------------------------------")
#? BINARY MODLAR

#* Dosyaları metin olarak değil byte olarak açmak için b kullanılır.

#* rb → binary okuma
#* wb → binary yazma
#* ab → binary sona ekleme
#* rb+ / r+b → binary okuma + yazma

#* Resim, PDF, video gibi metin olmayan dosyalarda kullanılır.

with open("39-DosyaIsleme/Dosyalar/png.png", "rb") as f:
    veri = f.read()

    print(veri)

#* Binary modda sonuç string değil bytes olur.


print("------------------------------------------")
#? DOSYA KONTROLÜ

import os

#* exists(): Dosya veya klasörün mevcut olup olmadığını kontrol eder.

if os.path.exists("39-DosyaIsleme/Dosyalar/png.png"):
    print("Dosya mevcut")
else:
    print("Dosya mevcut değil")


print("------------------------------------------")
#? DOSYA SİLME

if os.path.exists("39-DosyaIsleme/Dosyalar/png.png"):
    os.remove("39-DosyaIsleme/Dosyalar/png.png")
else:
    print("Dosya bulunamadı")


print("------------------------------------------")
#? KLASÖR LİSTELEME

#* os.listdir(): Belirtilen klasördeki dosya ve klasörleri liste olarak döndürür.
print(os.listdir("C:\\Users\\veysel\\Desktop\\Python"))


print("------------------------------------------")
#? KLASÖR OLUŞTURMA
#* os.mkdir(): Yeni klasör oluşturur.

klasor_yolu = "C:\\Users\\veysel\\Desktop\\Python\\39-DosyaIsleme/Dosyalar\\newFolder"

if not os.path.exists(klasor_yolu):
    os.mkdir(klasor_yolu)
    print("Klasör eklendi, os.mkdir(klasor_yolu)")


print("------------------------------------------")
#? KLASÖR SİLME
#* os.rmdir(): Boş bir klasörü siler. Klasörün içinde dosya varsa normal şekilde silemez

if os.path.exists(klasor_yolu):
    os.rmdir(klasor_yolu)
    print("Klasör silindi, os.rmdir(klasor_yolu)")


#? DOSYANIN SONUNA EKLEME
#* a modu mevcut içeriği silmeden dosyanın sonuna ekler

with open("39-DosyaIsleme/Dosyalar/dil.txt", "a", encoding="utf-8") as f:
    f.write("Python\n")


#? DOSYANIN BAŞINA VERİ EKLEME

#* Dosyaya doğrudan "başına ekle" şeklinde bir işlem yoktur
#* Bunun yerine:
#* 1- Dosyanın tamamını oku
#* 2- Yeni veriyi başa ekle
#* 3- Dosyanın başına git
#* 4- Yeni içeriği tekrar yaz

#* Ancak dosyanın tamamını yeniden yazmak gerektiği için büyük dosyalarda verimli olmayabilir

with open("39-DosyaIsleme/Dosyalar/dil.txt", "r", encoding="utf-8") as f:
    my_text = f.read()

my_text = "1-Python\n" + my_text

with open("39-DosyaIsleme/Dosyalar/dil.txt", "w", encoding="utf-8") as f:
    f.write(my_text)


#? DOSYANIN ORTASINA / BELİRLİ SATIRA VERİ EKLEME

#* Dosyanın ortasına doğrudan insert() gibi bir dosya metodu yoktur
#* Genellikle:
#* 1- İçeriği oku
#* 2- Listeye dönüştür
#* 3- Liste üzerinde insert() yap
#* 4- Dosyanın tamamını yeniden yaz

with open("39-DosyaIsleme/Dosyalar/dil.txt", "r", encoding="utf-8") as f:
    my_list = f.readlines()

my_list.insert(3, "4-Java\n")

with open("39-DosyaIsleme/Dosyalar/dil.txt", "w", encoding="utf-8") as f:
    f.writelines(my_list)

with open("39-DosyaIsleme/Dosyalar/dil.txt", "r", encoding="utf-8") as f:
    print(f.read())
