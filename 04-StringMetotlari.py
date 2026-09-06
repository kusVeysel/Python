text=" Hello, World! "

#? in
print("ello" in(text)) #* String text'in içinde varsa True yoksa False döner

#? not in
print("ello" not in(text)) #* String text'in içinde yoksa True yoksa False döner

#? [Başlangıçindeksi,Bitişindeksi]
print(text[2:7])
#? [-Bitişindeksi,-Başlangıçindeksi]
print(text[-4:-1])

#? -------------STRİNG METOTLAR-------------

#? len
print("len(text) => ",len(text)) #* Uzunluk döner

#? upper()
print("text.upper() => ",text.upper()) #* Büyük harfe dönüştürür

#? lower()
print("text.lower() => ",text.lower()) #* Küçük harfe dönüştürür

#? strip()
print("text.strip() => ",text.strip()) #* Sağdan soldan boşlukları kaldırır
# lstrip(): sadece soldaki boşlukları kaldırır
# rstrip(): sadece sağdaki boşlukları kaldırır

#? replace()
print("text.replace(\"l\",\"v\") => ",text.replace("l","v")) #* l stringini v stringi ile değiştirir

#? split()
print("text.split(\",\") => ",text.split(",")) #* ,'den böler(liste(dizi) döner)

#? splitlines(bool)
print("text.splitlines() => ",text.splitlines()) #* \n'den böler

#? capitalize()
print("\"hdslfh\".capitalize() => ","hdslfh".capitalize()) #* stringin ilk harfini büyük harfe dönüştürür

#? casefold()
print("text.casefold() => ",text.casefold()) #* Küçük harfe dönüştürür, lower'den farkı yok sadece daha fazla harfe dönüştürür ve daha yavaş çalışır

#? title()
print("\"sELAM DÜNYA\".title() => ","sELAM DÜNYA".title()) #* Stringin baş harfleri büyük diğer harfleri küçük yazar veya rakamdan sonraki harfi de büyük harfle yazar

#? swapcase()
print("\"Selam Dünya\".swapcase() => ","Selam Dünya".swapcase()) #* Stringin baş harfleri küçük diğer harfleri büyük yazar

#? islower()
print("\"result\".islower() => ","result".islower()) #* tüm string küçükse True yoksa False döner

#? isupper
print("\"RESULT\".isupper() => ","RESULT".isupper()) #* tüm string büyükse True yoksa False döner

#? center(StringinToplamUzunluk,SağaVeSolaNeGelecek)
print("\"Hello World!\".center(20,\"*\") => ","Hello World!".center(20,"*"))

#? count(SayılanDeğer,Başlamaİndeksi,Bitişİndeksi) 
print("text.count(\"Hello\") => ",text.count("Hello")) #* Hello'nun text'in içinde kaç adet olduğunu sayar

#? startswith(değer,Başlamaİndeksi,Bitişİndeksi)
print("text.startswith(\" Hel\") => ",text.startswith(" Hel")) #* text'in içinde parametre içindeki değer ile başlıyor mu diye bakar, True False döner

#? endswith(değer,Başlamaİndeksi,Bitişİndeksi)
print("text.endswith(\"ld! \") => ",text.endswith("ld! ")) #* text'in içinde parametre içindeki değer ile bitiyor mu diye bakar, True False döner

#? expandtabs(BolşulBüyüklüğü)
print("\"P\ty\tt\th\to\tn\".expandtabs(10) => ","P\ty\tt\th\to\tn".expandtabs(10)) 

#? find(ArananDeğer,AramaBaşlangıçİndexi,AramaBitişİndexi)
print("text.find(\"!\") => ",text.find("!")) #* Aranan değerin indexini verir ,değeri bulamazsa -1 döner
# rfind(): Aranan değer birden fazla varsa ilk sağdaki elemanın indexini döndürür

#? index(ArananDeğer)
print("text.index(\"!\") => ",text.index("!")) #* Aranan değerin indexini verir ,değeri bulamazsa hata verir, find ile aynı

#? isalnum()
print("text.isalnum() => ",text.isalnum()) #* String; harf ve rakamlardan oluşuyor mu diye kontrol eder, True False döenr

#? isascii()
print("text.isascii() => ",text.isascii()) #* String içinde ascii'de olmayan varsa False yoksa True döner

#? isdecimal()
print("text.isdecimal() => ",text.isdecimal()) #* Sadece rakamlardan oluşuyorsa True yoksa False döner

#? isdigit()
print("text.isdigit() => ",text.isdigit()) #* Sadece rakamlardan oluşuyorsa True yoksa False döner

#? isidentifier()
print("text.isidentifier() => ",text.isidentifier()) #* sayılar harfler ve underscore(_) harici false döner (sayı ile başlayamaz)

#? isnumeric()
print("text.isnumeric() => ",text.isnumeric()) #* Sadece rakamlardan oluşuyorsa True yoksa False döner

#? isprintable()
print("text.isprintable() => ",text.isprintable()) #* ekrana yazdırılamaz karakterler(\n,\r...) varsa False yoksa True döner

#? isspace()
print("\\t\\n".isspace()) #* yalnızca boşluk karakterlerinden oluşuyorsa True
Meyveler = ("Elma","Armut","Karpuz","Çilek")
print("\"-\".join(Meyveler) => ","-".join(Meyveler)) #* dizinin elemanları arasına "-" ekler

#? ljust()
cilek = "strawberry"
print("{cilek.ljust(19)} onun favori meyvesiymiş => ",f"{cilek.ljust(19)} onun favori meyvesiymiş") #* 19 karakter sola yaslar (kendisi(strawberry) 10 karakter bu yüzden 9 karakter sola yaslar) 

#? rjust()
print("{cilek.rjust(19)} onun favori meyvesiymiş => ",f"{cilek.rjust(19)} onun favori meyvesiymiş") #* 19 karakter sağa yaslar (kendisi(strawberry) 10 karakter bu yüzden 9 karakter sağa yaslar) 

#? maketrans(DeğişecekKarakter,YeniKarakter,SilinecekKarakter) translate(UygulanacakKural)
result = str.maketrans("P","Y","l") #* kural belirler
print(text.translate(result)) #* kuralı uygular

#? partition(NerdenAyrılaacak)
print("\"Tüm gün çilek yiyebilirmiş\".partition(\"çilek\") => ","Tüm gün çilek yiyebilirmiş".partition("çilek")) #* 3'e ayırır(tuple) 
# rpartition(): aynı değer birden fazla varsa ilk sağda gördüğü elemandan böler

#? zfill()
print("\"70\".zfill(9) => ","70".zfill(4)) #* 4 sıfır atar ama , 70 olduğu için yani 2 karakter var , 4 tane sıfır atar

