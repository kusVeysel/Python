 #? REGEX (Regular Expression)
#* Regex, metinler içerisinde belirli bir karakter, kelime veya desenin aranması, kontrol edilmesi, bulunması, değiştirilmesi ve ayrıştırılması için kullanılır
#* Python'da Regex işlemleri için "re" modülü kullanılır

import re

#? REGEX KARAKTERLERİ
#* [] : Karakter kümesi
#* Belirtilen karakterlerden herhangi birini eşleştirir
# Örnek: [abc] → a, b veya c karakterlerinden biri

#* [^] : Belirtilen karakterler dışındaki karakter [] içerisinde ^ kullanılırsa belirtilen karakterlerin dışındakileri eşleştirir
# Örnek: [^abc] → a, b ve c dışındaki bir karakter

#* - : Karakter aralığı belirli bir karakter aralığını belirtir
# Örnek:
# [a-z] → küçük harfler
# [A-Z] → büyük harfler
# [0-9] → rakamlar

#* \ : Özel karakter / escape karakteri
#* Regex içerisinde özel anlamı olan karakterleri normal karakter olarak kullanmak veya özel karakter sınıflarını kullanmak için kullanılır.
# Örnek:
# \. → nokta
# \+ → artı
# \( → parantez


#* . : Herhangi bir karakter yeni satır (\n) dışındaki herhangi bir karakteri eşleştirir
# Örnek: a.c → abc, a1c, a-c ...

#* ^ : Başlangıç metnin veya satırın başlangıcını belirtir
# Örnek: ^Merhaba → Merhaba ile başlayan metin

#* $ : Son Metnin veya satırın sonunu belirtir
# Örnek: dünya$ → dünya ile biten metin

#* * : Sıfır veya daha fazla tekrar önceki karakterin/desenin 0 veya daha fazla tekrarını eşleştirir
# Örnek: ab* → a, ab, abb, abbb ...

#* + : Bir veya daha fazla tekrar önceki karakterin/desenin en az 1 kez bulunmasını ister
# Örnek: ab+ → ab, abb, abbb ...

#* ? : Sıfır veya bir tekrar önceki karakterin/desenin 0 veya 1 kez bulunmasını ister
# Örnek: ab? → a veya ab

#* {n} : Tam olarak n tekrar önceki karakterin/desenin tam olarak belirtilen sayıda tekrarını ister
# Örnek: a{3} → aaa

#* {n,} : En az n tekrar önceki karakterin/desenin en az n kez bulunmasını ister
# Örnek: a{2,} → aa, aaa, aaaa ...

#* {n,m} : n ile m arasında tekrar önceki karakterin/desenin en az n, en fazla m kez bulunmasını ister
# Örnek: a{2,4} → aa, aaa, aaaa

#* | : OR alternatiflerden birinin eşleşmesini sağlar
# Örnek: kedi|köpek → kedi veya köpek

#* () : Grup birden fazla karakteri/deseni tek bir grup haline getirir. Aynı zamanda eşleşen bölümü yakalamak için kullanılır
# Örnek: (abc)+ → abc, abcabc ...

#* (?:) : Non-capturing group grup oluşturur fakat eşleşen kısmı ayrı bir grup olarak kaydetmez
# Örnek: (?:http|https)

#* (?P<isim>) : İsimlendirilmiş grup yakalanan gruba isim vermemizi sağlar
# Örnek: (?P<isim>[A-Za-z]+)

#* (?=...) : Pozitif lookahead belirtilen desenin devamında bulunmasını kontrol eder fakat kontrol edilen kısmı eşleşmeye dahil etmez.
# Örnek: \d+(?=TL) → Sonunda TL bulunan sayıyı yakalar

#* (?!...) : Negatif lookahead belirtilen desenin devamında bulunmamasını kontrol eder. Kontrol edilen kısım eşleşmeye dahil edilmez
# Örnek: \d+(?!TL)

#* (?<=...) : Pozitif lookbehind belirtilen desenin hemen öncesinde bulunmasını kontrol eder
# Örnek: (?<=₺)\d+ → Önünde ₺ bulunan sayıyı yakalar

#* (?<!...) : Negatif lookbehind belirtilen desenin hemen öncesinde bulunmamasını kontrol eder
# Örnek: (?<!₺)\d+ → Önünde ₺ bulunmayan sayıyı yakalar


#? ÖZEL KARAKTER SINIFLARI

#* \d : Rakam 0-9 arasındaki rakamları eşleştirir
# Örnek: \d+ → 123, 456, 789 ...

#* \D : Rakam olmayan karakter \d'nin tersidir
# Örnek: \D+ → abc, XYZ, !@# ...

#* \w : Kelime karakteri harf, rakam ve "_" karakterlerini eşleştirir
# Örnek: \w+ → Python, test123, user_name ...

#* \W : Kelime karakteri olmayan karakter \w'nin tersidir
# Örnek: \W+ → !@#, boşluk, noktalama işaretleri ...

#* \s : Boşluk karakterleri space, tab, newline gibi whitespace karakterlerini eşleştirir
# Örnek: \s+

#* \S : Boşluk olmayan karakter \s'nin tersidir.
# Örnek: \S+

#* \b : Kelime sınırı kelimenin başlangıç veya bitiş sınırını belirtir
# Örnek: \bcat\b → Sadece "cat" kelimesini yakalar."cat" eşleşir. "category" eşleşmez.

#* \B : Kelime sınırı olmayan yer \b'nin tersidir.


#? RAW STRING
#* Regex yazarken r"" kullanmak yaygın ve önerilen bir kullanımdır.
#* Böylece Python'ın \ karakterini normal string escape'i olarak yorumlaması ile Regex escape'lerinin karışması önlenir.

pattern = r"\d+"

# Örneğin: r"\d+"


#? FINDALL
#* Metindeki Regex desenine uyan TÜM eşleşmeleri liste olarak döndürür.

metin = "Ali 20 yaşında, Ahmet 25 yaşında."

sonuc = re.findall(r"\d+", metin)

print(sonuc)
# ['20', '25']

#? SEARCH
#* Metin içerisinde deseni arar
#* İlk bulduğu eşleşmeyi Match nesnesi olarak döndürür
#* Hiçbir eşleşme yoksa None döndürür

metin = "Python öğreniyorum."

sonuc = re.search(r"Python", metin)

if sonuc:
    print("Bulundu:", sonuc.group())
else:
    print("Bulunamadı.")


#? MATCH
#* Deseni sadece metnin BAŞLANGICINDA arar
#* Baştan eşleşme yoksa None döndürür

metin = "Python öğreniyorum."

sonuc = re.match(r"Python", metin)

if sonuc:
    print("Eşleşti:", sonuc.group())


#? FULLMATCH
#* Desenin TÜM metni kapsayıp kapsamadığını kontrol eder
#* Metnin tamamı desene uymalıdır

metin = "12345"

sonuc = re.fullmatch(r"\d+", metin)

if sonuc:
    print("Metnin tamamı sayılardan oluşuyor.")
else:
    print("Tam eşleşme yok.")


#? SPLIT
#* Regex desenine göre metni parçalara ayırır
#* Sonuç olarak liste döndürür

metin = "Elma,Armut;Muz Portakal"

sonuc = re.split(r"[,; ]", metin)

print(sonuc)
# ['Elma', 'Armut', 'Muz', 'Portakal']


#? SUB
#* Regex desenine uyan bölümleri başka bir metinle değiştirir

metin = "Telefon: 555-123-4567"

sonuc = re.sub(r"\d", "*", metin)

print(sonuc)
# Telefon: ***-***-****


#? SUBN
#* sub ile aynı işlemi yapar
#* Ancak değiştirilmiş metinle birlikte kaç değişiklik yapıldığını da döndürür

metin = "Ali 20 yaşında, Ahmet 25 yaşında."

sonuc = re.subn(r"\d+", "XX", metin)

print(sonuc)
# ('Ali XX yaşında, Ahmet XX yaşında.', 2)


#? FINDITER
#* findall gibi tüm eşleşmeleri bulur
#* Ancak sonuçları Match nesneleri olarak iterator şeklinde döndürür
#* group(), start(), end() gibi bilgileri almamızı sağlar

metin = "Ali 20 yaşında, Ahmet 25 yaşında."

sonuclar = re.finditer(r"\d+", metin)

for sonuc in sonuclar:
    print(sonuc.group())
    print(sonuc.start())
    print(sonuc.end())


#? GROUP
#* search, match veya finditer sonucundaki eşleşen metni alır

metin = "Telefon: 5551234567"

sonuc = re.search(r"\d+", metin)

if sonuc:
    print(sonuc.group())


#? START
#* Eşleşmenin başladığı index'i döndürür

metin = "Merhaba Python"

sonuc = re.search(r"Python", metin)

if sonuc:
    print(sonuc.start())


#? END
#* Eşleşmenin bittiği index'i döndürür
#* End index'i eşleşmenin son karakterinden bir sonraki konumu gösterir

metin = "Merhaba Python"

sonuc = re.search(r"Python", metin)

if sonuc:
    print(sonuc.end())


#? SPAN
#* Eşleşmenin başlangıç ve bitiş index'lerini tuple olarak döndürür

metin = "Merhaba Python"

sonuc = re.search(r"Python", metin)

if sonuc:
    print(sonuc.span())


#? GROUPS
#* Regex içerisinde bulunan yakalama gruplarının tamamını tuple olarak döndürür

metin = "Ad: Ali, Yaş: 25"

sonuc = re.search(r"Ad: (\w+), Yaş: (\d+)", metin)

if sonuc:
    print(sonuc.groups())
    # ('Ali', '25')


#? GROUP(N)
#* Belirli bir yakalama grubuna erişmemizi sağlar

metin = "Ad: Ali, Yaş: 25"

sonuc = re.search(r"Ad: (\w+), Yaş: (\d+)", metin)

if sonuc:
    print(sonuc.group(1))
    print(sonuc.group(2))


#? NAMED GROUP
#* Yakalama gruplarına isim verebiliriz

metin = "Ad: Ali, Yaş: 25"

sonuc = re.search(
    r"Ad: (?P<isim>\w+), Yaş: (?P<yas>\d+)",
    metin
)

if sonuc:
    print(sonuc.group("isim"))
    print(sonuc.group("yas"))


#? GROUPDICT
#* İsimlendirilmiş grupları dictionary olarak döndürür

metin = "Ad: Ali, Yaş: 25"

sonuc = re.search(
    r"Ad: (?P<isim>\w+), Yaş: (?P<yas>\d+)",
    metin
)

if sonuc:
    print(sonuc.groupdict())
    # {'isim': 'Ali', 'yas': '25'}



#? COMPILE
#* Regex desenini önceden bir Regex Pattern nesnesine dönüştürür
#* Aynı deseni birden fazla kez kullanacağımız zaman kullanışlıdır

pattern = re.compile(r"\d+")

print(pattern.findall("Ali 20, Ahmet 25"))
print(pattern.findall("Veli 30, Ayşe 35"))


#? REGEX QUANTIFIER'LARI


#* * → 0 veya daha fazla
print(re.findall(r"ab*", "a ab abb abbb"))

#* + → 1 veya daha fazla
print(re.findall(r"ab+", "a ab abb abbb"))

#* ? → 0 veya 1
print(re.findall(r"ab?", "a ab abb"))

#* {n} → Tam olarak n
print(re.findall(r"a{3}", "aa aaa aaaa"))

#* {n,} → En az n
print(re.findall(r"a{2,}", "a aa aaa aaaa"))

#* {n,m} → n ile m arasında
print(re.findall(r"a{2,4}", "a aa aaa aaaa aaaaa"))


#? GREEDY / LAZY
#* Regex quantifier'ları varsayılan olarak mümkün olan en uzun eşleşmeyi bulmaya çalışır
#* Buna greedy denir.

metin = "<div>Merhaba</div><div>Dünya</div>"

print(re.findall(r"<div>.*</div>", metin))

#* ? kullanarak lazy davranış elde edebiliriz
#* Mümkün olan en kısa eşleşmeyi bulmaya çalışır

print(re.findall(r"<div>.*?</div>", metin))


#? KARAKTER KÜMELERİ

#* Sadece küçük harfler:
print(re.findall(r"[a-z]+", "Python abc XYZ 123"))

#* Sadece büyük harfler:
print(re.findall(r"[A-Z]+", "Python ABC xyz"))

#* Sadece rakamlar:
print(re.findall(r"[0-9]+", "abc 123 xyz 456"))

#* Küçük veya büyük harf:
print(re.findall(r"[A-Za-z]+", "Python ABC test"))


#? OR (|)

metin = "Python Java JavaScript C#"

sonuc = re.findall(r"Python|JavaScript|C#", metin)

print(sonuc)


#? GRUPLAMA

#* () ile birden fazla karakteri tek bir grup haline getirebiliriz

metin = "ha haha hahaha"

sonuc = re.findall(r"(ha)+", metin)

print(sonuc)


#? BAŞLANGIÇ ^

metin = "Python öğreniyorum."

sonuc = re.search(r"^Python", metin)

if sonuc:
    print("Metin Python ile başlıyor.")


#? SON $

metin = "Python öğreniyorum"

sonuc = re.search(r"öğreniyorum$", metin)

if sonuc:
    print("Metin öğreniyorum ile bitiyor.")


#? KELİME SINIRI \b

metin = "cat category scatter"

sonuc = re.findall(r"\bcat\b", metin)

print(sonuc)
# Sadece ayrı bir kelime olan cat bulunur.


#? NEGATİF KARAKTER KÜMESİ [^]

metin = "abc123XYZ"

sonuc = re.findall(r"[^0-9]+", metin)

print(sonuc)


#? EMAIL KONTROLÜ

email = "test@example.com"

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.fullmatch(pattern, email):
    print("Geçerli email formatı.")
else:
    print("Geçersiz email formatı.")


#? TELEFON NUMARASI KONTROLÜ

telefon = "05551234567"

pattern = r"^05\d{9}$"

if re.fullmatch(pattern, telefon):
    print("Geçerli telefon numarası.")
else:
    print("Geçersiz telefon numarası.")


#? POSTA KODU KONTROLÜ

posta_kodu = "06100"

pattern = r"^\d{5}$"

if re.fullmatch(pattern, posta_kodu):
    print("Geçerli posta kodu.")


#? TARİH KONTROLÜ

tarih = "11/09/2026"

pattern = r"^\d{2}/\d{2}/\d{4}$"

if re.fullmatch(pattern, tarih):
    print("Tarih formatı doğru.")


#? SADECE SAYI KONTROLÜ

metin = "12345"

if re.fullmatch(r"\d+", metin):
    print("Sadece sayı içeriyor.")


#? SADECE HARF KONTROLÜ

metin = "Python"

if re.fullmatch(r"[A-Za-z]+", metin):
    print("Sadece harf içeriyor.")


#? KULLANICI ADI KONTROLÜ

kullanici_adi = "veysel_123"

pattern = r"^[A-Za-z0-9_]{3,20}$"

if re.fullmatch(pattern, kullanici_adi):
    print("Kullanıcı adı geçerli.")
else:
    print("Kullanıcı adı geçersiz.")


#? ŞİFRE KONTROLÜ
#* En az 8 karakter
#* En az bir büyük harf
#* En az bir küçük harf
#* En az bir rakam

sifre = "Python123"

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

if re.fullmatch(pattern, sifre):
    print("Şifre uygun.")
else:
    print("Şifre uygun değil.")


#? LOOKAHEAD

#* (?=...) belirtilen desenin sonrasında bulunmasını kontrol eder
#* Ancak kontrol edilen bölüm eşleşmeye dahil edilmez

metin = "100TL 200USD 300TL"

sonuc = re.findall(r"\d+(?=TL)", metin)

print(sonuc)
# ['100', '300']


#? NEGATİF LOOKAHEAD

#* (?!...) belirtilen desenin sonrasında bulunmamasını kontrol eder

metin = "100TL 200USD 300TL"

sonuc = re.findall(r"\d+(?!TL)", metin)

print(sonuc)


#? LOOKBEHIND

#* (?<=...) belirtilen desenin eşleşmenin hemen öncesinde bulunmasını kontrol eder

metin = "₺100 $200 ₺300"

sonuc = re.findall(r"(?<=₺)\d+", metin)

print(sonuc)
# ['100', '300']


#? NEGATİF LOOKBEHIND

#* (?<!...) belirtilen desenin eşleşmenin hemen öncesinde bulunmamasını kontrol eder

metin = "₺100 $200 ₺300"

sonuc = re.findall(r"(?<!₺)\d+", metin)

print(sonuc)


#? REGEX FLAGS

#* Regex'in nasıl çalışacağını değiştirmek için flag kullanılabilir


#* re.IGNORECASE / re.I
#* Büyük-küçük harf ayrımını kaldırır.

metin = "Python PYTHON python"

print(re.findall(r"python", metin, re.IGNORECASE))


#* re.MULTILINE / re.M
#* ^ ve $ karakterlerinin her satırın başlangıç ve sonunu kontrol etmesini sağlar

metin = """Python
Java
Python"""

print(re.findall(r"^Python", metin, re.MULTILINE))


#* re.DOTALL / re.S . karakterinin newline (\n) karakterini de eşleştirmesini sağlar

metin = "Merhaba\nDünya"

print(re.findall(r"Merhaba.Dünya", metin, re.DOTALL))


#* Birden fazla flag birlikte kullanılabilir

metin = """Python
PYTHON
python"""

print(
    re.findall(
        r"^python$",
        metin,
        re.IGNORECASE | re.MULTILINE
    )
)


#? ESCAPE
#* Regex'te özel anlam taşıyan karakterleri normal karakter olarak aramak için re.escape() kullanılabilir.

metin = "fiyat: 10.50 TL"

aranacak = "10.50"

pattern = re.escape(aranacak)

print(re.search(pattern, metin))


#? REGEX İLE METİNDEN BİLGİ ÇIKARMA

metin = """
Ad: Veysel
Email: test@example.com
Telefon: 05551234567
"""

email = re.search(
    r"Email:\s*([\w.-]+@[\w.-]+\.\w+)",
    metin
)

telefon = re.search(
    r"Telefon:\s*(05\d{9})",
    metin
)

if email:
    print("Email:", email.group(1))

if telefon:
    print("Telefon:", telefon.group(1))


#? REGEX İLE BİRDEN FAZLA VERİ ÇIKARMA

metin = """
Ali - 25
Ahmet - 30
Veli - 22
"""

sonuclar = re.findall(
    r"(\w+)\s*-\s*(\d+)",
    metin
)

print(sonuclar)

# [('Ali', '25'), ('Ahmet', '30'), ('Veli', '22')]


#? REGEX İLE METİN DEĞİŞTİRME

metin = "Merhaba    dünya.     Python öğreniyorum."

# Birden fazla boşluğu tek boşluğa indirir.

metin = re.sub(r"\s+", " ", metin)

print(metin)


#? REGEX İLE HTML TAG TEMİZLEME

metin = "<p>Merhaba <b>dünya</b></p>"

sonuc = re.sub(r"<.*?>", "", metin)

print(sonuc)
# Merhaba dünya


#? REGEX İLE SAYILARI BULMA

metin = "Ürünler: 100 TL, 250 TL ve 500 TL"

sayilar = re.findall(r"\d+", metin)

print(sayilar)


#? REGEX İLE URL BULMA

metin = """
Web sitemiz: https://example.com
Github: https://github.com/test
"""

pattern = r"https?://[^\s]+"

sonuclar = re.findall(pattern, metin)

print(sonuclar)


#? REGEX İLE IP ADRESİ FORMATINI KONTROL ETME

ip = "192.168.1.10"

pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

if re.fullmatch(pattern, ip):
    print("IP formatı uygun.")
else:
    print("IP formatı uygun değil.")


#? TRY - EXCEPT İLE REGEX KULLANIMI

#* Regex işlemlerinde hata oluşma ihtimaline karşı try-except kullanılabilir

try:
    pattern = re.compile(r"[")

except re.error as hata:
    print("Regex hatası:", hata)


#? RE.ERROR
#* Geçersiz bir Regex deseni oluşturulduğunda oluşabilecek exception'dır

try:
    regex = re.compile(r"[abc")

except re.error as hata:
    print("Geçersiz Regex:", hata)