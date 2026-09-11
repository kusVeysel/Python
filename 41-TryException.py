 #? try-exception

#? Yaygın exception türleri
#* Python'da program çalışırken farklı durumlarda çeşitli exception türleri oluşabilir
#* Aşağıdaki exception türleri günlük kullanımda ve gerçek projelerde en sık karşılaşılanlardandır

#? ValueError
#* Değer doğru türde olsa bile beklenen formata/değere uygun olmadığında oluşur
# Örnek:
# int("abc")
# int("12.5")

#? TypeError
#* Bir işlemde kullanılan veri tipleri birbirleriyle uyumsuz olduğunda oluşur
# Örnek:
# 10 + "20"
# len(10)


#? IndexError
#* Liste, tuple veya benzeri sıralı yapılarda bulunmayan bir index'e erişildiğinde oluşur
# Örnek:
# liste = [10, 20, 30]
# liste[10]


#? KeyError
#* Dictionary içerisinde bulunmayan bir key'e doğrudan erişilmeye çalışıldığında oluşur
# Örnek:
# bilgiler = {"isim": "Ahmet"}
# bilgiler["meslek"]


#? ZeroDivisionError
#* Bir sayı 0'a bölünmeye çalışıldığında oluşur
# Örnek: 10 / 0


#? FileNotFoundError
#* Açılmak istenen dosya bulunamadığında oluşur
# Örnek: open("olmayan_dosya.txt", "r")


#? FileExistsError
#* Oluşturulmak istenen dosya veya klasör zaten mevcut olduğunda oluşabilir
# Örnek:
# os.mkdir("klasor")  # Klasör zaten varsa


#? PermissionError
#* Dosya veya klasör üzerinde gerekli erişim izni olmadığında oluşur
# Örnek:
# open("korumali_dosya.txt", "w")


#? IsADirectoryError
#* Dosya olarak açılmak istenen yol bir klasör olduğunda oluşur
# Örnek:
# open("klasor", "r")


#? NotADirectoryError
#* Klasör olarak kullanılması gereken yol bir dosya olduğunda oluşur
# Örnek: os.listdir("dosya.txt")


#? OSError
#* İşletim sistemiyle ilgili bir işlem başarısız olduğunda oluşabilen genel exception'dır
#* Dosya, klasör, sistem kaynakları gibi işlemlerde karşımıza çıkabilir


#? AttributeError
#* Bir nesnede bulunmayan bir attribute veya method kullanılmaya çalışıldığında oluşur
# Örnek:
# sayi = 10
# sayi.append(20)


#? NameError
#* Tanımlanmamış bir değişken veya isim kullanılmaya çalışıldığında oluşur
# Örnek:
# print(isim)  # isim daha önce tanımlanmadı


#? UnboundLocalError
#* Fonksiyon içerisindeki local bir değişken, değer atanmadan kullanılmaya çalışıldığında oluşur. NameError'ın özel bir türüdür


#? ImportError
#* Bir modülden bulunmayan bir öğe import edilmeye çalışıldığında oluşur
# Örnek: from math import olmayan_fonksiyon


#? ModuleNotFoundError
#* Bulunmayan bir modül import edilmeye çalışıldığında oluşur. ImportError'ın özel bir türüdür
# Örnek: import olmayan_modul


#? RuntimeError
#* İşlem sırasında belirli bir kategoriye girmeyen genel bir çalışma zamanı hatası oluştuğunda kullanılabilir


#? RecursionError
#* Bir fonksiyon kendisini aşırı şekilde çağırıp maksimum recursion sınırını aştığında oluşur


#? StopIteration
#* Iterator içerisinde alınacak başka değer kalmadığında oluşur
#* Genellikle iterator yapıları ve next() kullanılırken karşımıza çıkar


#? AssertionError
#* assert ile yapılan kontrol başarısız olduğunda oluşur
# Örnek: assert 10 > 20


#? OverflowError
#* Bir matematiksel işlem sonucunun Python'ın desteklediği sayı aralığını aşması durumunda oluşabilir


#? FloatingPointError
#* Float işlemleriyle ilgili bir hata oluştuğunda kullanılabilen exception'dır
#* Normal Python kullanımında çok sık karşılaşılmaz


#? UnicodeError
#* Unicode ile ilgili bir kodlama/çözme problemi olduğunda oluşur.
#* Alt türleri:
# UnicodeEncodeError
# UnicodeDecodeError
# UnicodeTranslateError


#? IndentationError
#* Python'da girintileme kurallarına uyulmadığında oluşur
# Örnek:
# if True:
# print("Merhaba")


#? TabError
#* Girintilemede tab ve boşlukların yanlış şekilde karıştırılması durumunda oluşur


#? SyntaxError
#* Python kodunun yazım kurallarına aykırı olması durumunda oluşur
# Örnek: if True print("Merhaba")


#? KeyboardInterrupt
#* Program çalışırken kullanıcı tarafından Ctrl + C ile program durdurulduğunda oluşur


#? Exception
#* Diğer birçok exception'ın üst sınıfıdır
#* Birçok farklı hatayı genel olarak yakalamak için kullanılabilir


#? BaseException
#* Python'daki exception hiyerarşisinin en üst seviyesindeki temel sınıftır
#* Genellikle doğrudan yakalanması önerilmez
#* Exception sınıfı, BaseException'dan türemiştir



#? TEMEL TRY - EXCEPT
#* try içerisinde hata oluşturabilecek kod bulunur
#* Hata oluşursa Python except bölümüne geçer

try:
    sayi = int(input("Bir sayı girin: "))
    print(10 / sayi)

except:
    print("Bir hata oluştu.")


#? BELİRLİ EXCEPTION YAKALAMA
#* Hangi hatayı yakalamak istediğimizi belirtebiliriz.
#* Bu yöntem genel except kullanımından daha kontrollüdür.

try:
    sayi = int(input("Bir sayı girin: "))
    print(10 / sayi)

except ValueError:
    # Kullanıcı sayı yerine uygun olmayan bir değer girerse oluşur.
    print("Lütfen sayı girin.")

except ZeroDivisionError:
    # Kullanıcı 0 girerse oluşur.
    print("Bir sayı 0'a bölünemez.")


#? EXCEPTION'I DEĞİŞKENE ALMA
#* "as hata" ile oluşan Exception nesnesini bir değişkene alabiliriz.
#* Böylece Python'ın oluşturduğu hata mesajına ulaşabiliriz.

try:
    sayi = int(input("Sayı: "))
    sonuc = 10 / sayi

except ValueError as hata:
    print("Değer hatası:", hata)

except ZeroDivisionError as hata:
    print("Sıfıra bölme hatası:", hata)


#? TRY - EXCEPT - ELSE
#* else, try içerisinde hiçbir hata oluşmadığında çalışır
#* Başarılı işlemler için kullanılabilir

try:
    sayi = int(input("Bir sayı girin: "))

except ValueError:
    print("Geçersiz sayı.")

else:
    print("Sayı başarıyla alındı.")
    print("Girilen sayı:", sayi)


#? TRY - EXCEPT - FINALLY
#* finally, hata oluşsa da oluşmasa da çalışır
#* Dosya kapatma, bağlantı kapatma gibi işlemlerde kullanışlıdır

try:
    sayi = int(input("Sayı: "))
    print(100 / sayi)

except ValueError:
    print("Geçersiz değer.")

except ZeroDivisionError:
    print("0'a bölme yapılamaz.")

finally:
    print("İşlem tamamlandı.")


#? TRY - EXCEPT - ELSE - FINALLY
#* try     → Hata çıkabilecek kod
#* except  → Hata oluşursa
#* else    → Hata oluşmazsa
#* finally → Her durumda

try:
    sayi = int(input("Sayı: "))
    sonuc = 100 / sayi

except ValueError:
    print("Sayı formatı hatalı.")

except ZeroDivisionError:
    print("Sıfıra bölme yapılamaz.")

else:
    print("İşlem başarılı.")
    print("Sonuç:", sonuc)

finally:
    print("Program bu bölümü her durumda çalıştırır.")


#? BİRDEN FAZLA EXCEPTION
#* Aynı işlemi birden fazla Exception için kullanabiliriz.

try:
    sayi = int(input("Sayı: "))
    sonuc = 10 / sayi

except (ValueError, ZeroDivisionError):
    print("İşlem sırasında bir hata oluştu.")


#? TYPEERROR
#* Veri tipleri arasında uygun olmayan işlem yapılırsa oluşur

try:
    sayi = 10
    metin = "20"

    sonuc = sayi + metin

except TypeError:
    print("Veri tipleri uyumsuz.")


#? INDEXERROR
#* Listede olmayan bir index'e erişmeye çalışırsak oluşur

try:
    liste = [10, 20, 30]

    print(liste[5])

except IndexError:
    print("Listenin böyle bir index'i yok.")


#? KEYERROR
#* Dictionary içerisinde olmayan bir key'e erişmeye çalışırsak oluşur

try:
    bilgiler = {
        "isim": "Ahmet",
        "yas": 25
    }

    print(bilgiler["meslek"])

except KeyError:
    print("Aranan key bulunamadı.")


#? ATTRIBUTEERROR
#* Bir nesnede bulunmayan bir attribute veya method kullanılmaya çalışılırsa oluşur

try:
    sayi = 10
    sayi.append(20)

except AttributeError:
    print("Bu nesnede böyle bir method veya attribute yok.")


#? NAMEERROR
#* Tanımlanmamış bir değişken kullanılmaya çalışılırsa oluşur

try:
    print(isim)

except NameError:
    print("Bu isim/değişken tanımlanmamış.")


#? FILENOTFOUNDERROR
#* Olmayan bir dosyayı açmaya çalışırsak oluşur

try:
    dosya = open("bilgiler.txt", "r")

except FileNotFoundError:
    print("Dosya bulunamadı.")


#? PERMISSIONERROR
#* Dosyaya veya klasöre erişim izni olmadığında oluşabilir

try:
    dosya = open("korumali_dosya.txt", "w")

except PermissionError:
    print("Dosyaya erişim izniniz yok.")


#? IMPORTERROR
#* Bir modülden bulunmayan bir öğe import edilmeye çalışılırsa oluşur

try:
    from math import olmayan_fonksiyon

except ImportError:
    print("Import edilmek istenen öğe bulunamadı.")


#? MODULENOTFOUNDERROR
#* Bulunmayan bir modül import edilmeye çalışılırsa oluşur

try:
    import olmayan_modul

except ModuleNotFoundError:
    print("Modül bulunamadı.")


#? ASSERTIONERROR
#* assert kontrolü False olduğunda oluşur

try:
    sayi = 10

    assert sayi > 20

except AssertionError:
    print("Assert kontrolü başarısız.")


#? TRY - EXCEPT İLE INPUT KONTROLÜ
#* Kullanıcıdan doğru değer alınana kadar tekrar sorabiliriz

while True:

    try:
        sayi = int(input("1-100 arasında sayı girin: "))

        if 1 <= sayi <= 100:
            print("Geçerli sayı:", sayi)
            break

        print("Sayı 1-100 arasında olmalı.")

    except ValueError:
        print("Lütfen sadece sayı girin.")


#? RAISE
#* raise ile kendi Exception'ımızı oluşturabiliriz
#* Python'ın otomatik olarak hata vermesini beklemek yerine belirlediğimiz durumda kendimiz hata oluşturabiliriz

yas = int(input("Yaşınızı giriniz: "))

if yas < 18:
    raise ValueError("Yaş 18'den küçük olamaz.")


#? RAISE + TRY - EXCEPT
#* raise ile oluşturduğumuz hatayı try-except ile yakalayabiliriz

try:
    yas = int(input("Yaşınızı girin: "))

    if yas < 18:
        # Kendimiz ValueError oluşturuyoruz.
        raise ValueError("Yaş 18'den küçük olamaz.")

    print("İşleme devam edilebilir.")

except ValueError as hata:
    print("Hata:", hata)


#? KENDİ EXCEPTION SINIFIMIZ
#* Exception sınıfından miras alarak kendimize özel Exception oluşturabiliriz

class YasHatasi(Exception):
    pass


try:
    yas = int(input("Yaş: "))

    if yas < 18:
        raise YasHatasi("Yaş 18'den küçük.")

except YasHatasi as hata:
    print("Hata:", hata)


#? ÖNEMLİ
#* Mümkün olduğunda sadece "except:" kullanmak yerine hangi Exception'ı yakalamak istediğimizi belirtmek daha doğrudur

# Örneğin:

try:
    sayi = int(input("Sayı: "))

except ValueError:
    print("Geçersiz sayı.")


#* Genel olarak birçok Exception'ı yakalamak gerekiyorsa Exception kullanılabilir

try:
    sayi = int(input("Sayı: "))

except Exception as hata:
    print("Bir hata oluştu:", hata)