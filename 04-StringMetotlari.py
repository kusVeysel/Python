 #? STRİNG METOTLAR

#* len(): Uzunluğu döner

#* upper(): Büyük harflere dönüştürür

#* lower(): Küçük harflere dönüştürür

#* strip(): Sağdaki ve soldaki boşlukları kaldırır
# lstrip(): Sadece soldaki boşlukları kaldırır
# rstrip(): Sadece sağdaki boşlukları kaldırır
#! → parametre içine karakter kümesi verilirse, baştaki ve sondaki bu karakterleri kaldırır

#* replace('x','y'): x stringini y stringi ile değiştirir

#* split('x'): x stringinden böler ve liste olarak döner  

#* splitlines(): \n'den böler

#* capitalize(): İlk harfi büyük harfe dönüştürür, diğerlerini küçük harfe dönüştürür

#* casefold(): Küçük harfe dönüştürür, lower'den farkı yok sadece daha fazla harfe dönüştürür ve daha yavaş çalışır

#* title(): Stringin baş harfleri büyük diğer harfleri küçük yazar, rakamdan sonraki harfi de büyük harfle yazar

#* swapcase(): Büyük harfleri küçük, küçük harfleri büyük yapar

#* islower(): Tüm string küçükse True yoksa False döner

#* isupper(): Tüm string büyükse True yoksa False döner

#* center(x, y): 
# → x: Stringin toplam uzunluğu
# → y: Sağa ve sola eklenecek eleman

#* count(x,y,z): x'in stringin içinde y-z index aralığında kaç adet olduğunu sayar
# → x: Sayılan değer
# → y: Başlama İndeksi(Dahil)
# → z: Bitiş İndeksi(Dahil değil)

#* startswith(x,y,z): stringin içinde y,z aralığında  x değeri ile başlıyor mu diye bakar
# → x: Değer
# → y: Başlama İndeksi(Dahil)
# → z: Bitiş İndeksi(Dahil değil)

#* endswith(x,y,z): stringin içinde y,z aralığında  x değeri ile bitiyor mu diye bakar
# → x: Değer
# → y: Başlama İndeksi(Dahil)
# → z: Bitiş İndeksi(Dahil değil)

#* expandtabs(): \t karakterlerini belirlenen tab genişliğine göre boşluklara dönüştürür.

#* find(x,y,z): Aranan değerin indexini verir ,değeri bulamazsa -1 döner
# → x: Aranan Değer
# → y: Arama Başlangıç İndeksi
# → z: Arama Bitiş İndeksi
# rfind(): Aranan değer birden fazla varsa ilk sağdaki(indexi büyük olan) elemanın indexini döndürür

#* index(): Aranan değerin indexini verir, değeri bulamazsa hata verir

#* isalnum(): String; harf ve rakamlardan oluşuyor mu diye kontrol eder. Boşluk ve özel karakter kabul etmez.

#* isascii(): String içinde ascii'de olmayan varsa False yoksa True döner

#* isdecimal(): Sadece rakamlardan oluşuyorsa True yoksa False döner

#* isdigit(): Sadece rakamlardan oluşuyorsa True yoksa False döner

#* isnumeric(): Sadece rakamlardan oluşuyorsa True yoksa False döner

# → isdecimal() ⊂ isdigit() ⊂ isnumeric()

#* isidentifier(): Geçerli bir identifier/değişkenadı olup olmadığını kontrol eder

#* isprintable(): Ekrana yazdırılamaz karakterler(\n,\r...) varsa False yoksa True döner

#* isspace(): Yalnızca boşluk karakterlerinden oluşuyorsa True, yoksa False

#* 'x'.join(dizi): Dizinin elemanları arasına 'x' ekler

#* ljust(x):  x karakter sola yaslar (kendisini de dahil eder) 

#* rjust(x):  x karakter sağa yaslar (kendisini de dahil eder) 

#* maketrans(x,y,z): Kural belirler
#* translate(a): kuralı uygular
# → x: Değişecek karakter
# → y: Yeni karakter
# → z: Silinecek karakter
# → a: Uygulanacak kural

#* partition(x): x'ten ayırır, x'ten önce, x'ten sonra ve x olarak 3'e ayrılır, tuple olarak döner
# → x: Ayrılacak string 
# rpartition(): Aynı değer birden fazla varsa en sağdaki(indexi büyük olan) ayırıcıdan böler

#* zfill(x): sola x sıfır atar (kendisini de dahil eder)

#? operatör
#* in(x): İçeriyor mu diye bakar
# → x: Aranan eleman

#* not in(x): İçermiyor mu diye bakar
# → x: Aranan eleman


#? len
print("------------------------------------------")
print("len('text') →", len('text'))
print("------------------------------------------")

#? upper()
print("'text'.upper() →",'text'.upper())
print("------------------------------------------")

#? lower()
print("'TEXT'.lower() →",'TEXT'.lower())
print("------------------------------------------")

#? strip()
print("' text '.strip() →",' text '.strip())
print("------------------------------------------")

#? replace()
print("'text'.replace('t','a') →",'text'.replace('t','a'))
print("------------------------------------------")

#? split()
print("'te,x,t'.split(',') →",'te,x,t'.split(','))
print("------------------------------------------")

#? splitlines()
print("'text\\ntext'.splitlines() →",'text\ntext'.splitlines())
print("------------------------------------------")

#? capitalize()
print("'tEXT'.capitalize() →",'tEXT'.capitalize()) 
print("------------------------------------------")

#? casefold()
print("'TEXT'.casefold() →",'TEXT'.casefold())
print("------------------------------------------")

#? title()
print("'sELAM DÜNYA'.title() →",'sELAM dÜNYA'.title())
print("------------------------------------------")

#? swapcase()
print("'TeXt'.swapcase() →",'TeXt'.swapcase())
print("------------------------------------------")

#? islower()
print("'result'.islower() →",'result'.islower())
print("------------------------------------------")

#? isupper
print("'RESULT'.isupper() →",'RESULT'.isupper())
print("------------------------------------------")

#? center()
print("'text'.center(10,'*') →",'text'.center(10,'*'))
print("------------------------------------------")

#? count() 
print("'text'.count('t') →","text".count('t'))
print("------------------------------------------")

#? startswith()
print("'text'.startswith('x',2,3) →",'text'.startswith('x',2,3))
print("------------------------------------------")

#? endswith()
print("'text'.endswith('e',1,2) →",'text'.endswith('e',1,2))
print("------------------------------------------")

#? expandtabs()
print("'P\\ty\\tt\\th\\to\\tn'.expandtabs(10) →",'P\ty\tt\th\to\tn'.expandtabs(10)) 
print("------------------------------------------")

#? find()
print("'text'.find('x') →",'text'.find('x'))
print("------------------------------------------")

#? index()
print("'text'.index('x') →",'text'.index('x'))
print("------------------------------------------")

#? isalnum()
print("'text'.isalnum() →",'text'.isalnum())
print("------------------------------------------")

#? isascii()
print("'text'.isascii() →",'text'.isascii())
print("------------------------------------------")

#? isdecimal()
print("'1234'.isdecimal() →",'1234'.isdecimal())
print("------------------------------------------")

#? isdigit()
print("'1234'.isdigit() →",'1234'.isdigit())
print("------------------------------------------")

#? isidentifier()
print("'text'.isidentifier() →",'text'.isidentifier())
print("------------------------------------------")

#? isnumeric()
print("'1234'.isnumeric() →",'1234'.isnumeric())
print("------------------------------------------")

#? isprintable()
print("'\\n\\t'.isprintable() →",'\n\t'.isprintable())
print("------------------------------------------")

#? isspace()
print("'\\t\\n'.isspace()",'\t\n'.isspace())
print("------------------------------------------")

#? join()
print("'-'.join(('Elma','Armut','Karpuz','Çilek')) →",'-'.join(('Elma','Armut','Karpuz','Çilek')))
print("------------------------------------------")

#? ljust()
print("{'cilek'.ljust(19)} onun favori meyvesiymiş →",f"{'cilek'.ljust(19)} onun favori meyvesiymiş")
print("------------------------------------------")

#? rjust()
print("{'cilek'.rjust(19)} onun favori meyvesiymiş →",f"{'cilek'.rjust(19)} onun favori meyvesiymiş") 
print("------------------------------------------")

#? maketrans()
print("'text'.translate(str.maketrans('t','a','x')) →",'text'.translate(str.maketrans('t','a','x')))
print("------------------------------------------")

#? partition()
print("'Tüm gün çilek yiyebilirmiş'.partition('çilek') →",'Tüm gün çilek yiyebilirmiş'.partition('çilek'))
print("------------------------------------------")

#? zfill()
print("'70'.zfill(4) →",'70'.zfill(4))
print("------------------------------------------")

#? operatör

#? in()
print("'xt' in('text') →",'xt' in('text'))
print("------------------------------------------")

#? not in()
print("'xt' not in('text') →",'xt' not in('text')) 
print("------------------------------------------")

#? 
#? [Başlangıç_indeksi(dahil), Bitiş_indeksi(dahil değil)]
print("'texttexttext'[2:7] →",'texttexttext'[2:7])
#? [-Bitişindeksi, -Başlangıçindeksi]
print("'texttexttext'[-4:-1] →",'texttexttext'[-4:-1])