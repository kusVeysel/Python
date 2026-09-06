# SummerPy 01-38 Konu Özeti

Bu dosya, `01-Giris.py` ile `38-Metaprogramming.py` arasındaki derslerde kullanılan
fonksiyon, değişken, property/attribute, class ve önemli Python yapılarını özetler.

## 01 - Python'a Giriş

- `print()`: Ekrana çıktı yazar.
- `input()`: Kullanıcıdan veri alır. Prompt gösterse de dönüş değeri her zaman `str` olur.
- `type()`: Bir değerin veya değişkenin türünü verir.
- `str()`, `int()`, `float()`: Tür dönüştürme fonksiyonlarıdır.
- Değişken yeniden atanabilir; değişkenin türü son atanan değerin türü değildir, Python'da
	isimler değerlere bağlanır.
- Değişken isimleri rakamla başlayamaz; harf, Unicode karakterleri, rakam ve `_` içerebilir.
- `a, b, c = colors`: Iterable elemanlarını ayrı isimlere açar (unpacking).
- `+` stringleri bitişik birleştirir; `print()` içindeki virgül araya boşluk koyar.
- Örnek değişkenler: `a`, `x`, `y`, `z`, `colors`, `degisken1`, `degisken2`, `degisken3`.

## 02 - Veri Türleri ve Kapsam

- Global değişken: Fonksiyon dışında tanımlanır ve global kapsamda bulunur.
- Local değişken: Fonksiyon içinde tanımlanır; fonksiyon dışında doğrudan kullanılamaz.
- `global`: Fonksiyon içinden global isim oluşturmayı veya değiştirmeyi sağlar.
- Temel türler: `str` metin, `int` tam sayı, `float` ondalık sayı, `complex` karmaşık sayı,
	`bool` doğru/yanlış ve `NoneType` için `None`.
- Koleksiyonlar: `list` değiştirilebilir, `tuple` değiştirilemez, `range` sayı aralığı,
	`dict` anahtar-değer, `set` tekrarsız küme, `frozenset` değiştirilemez kümedir.
- `2e4`: Bilimsel gösterimdir ve `20000.0` değerini ifade eder.

## 03 - `random` Modülü

- `random()`: `0 <= x < 1` aralığında ondalık sayı üretir.
- `seed(value)`: Üretecin durumunu belirler; aynı tohum aynı sayı dizisini üretir.
- `getstate()` / `setstate(state)`: Rastgelelik durumunu kaydetme ve geri yükleme.
- `getrandbits(k)`: `k` bitlik rastgele tam sayı üretir.
- `randrange(start, stop, step)`: `stop` hariç aralıktan seçim yapar.
- `randint(a, b)`: `a` ve `b` dahil rastgele tam sayı üretir.
- `choice(sequence)`: Tek bir rastgele eleman seçer.
- `choices(sequence, weights, k)`: Ağırlıklı seçim yapar; aynı eleman tekrar seçilebilir.
- `shuffle(list)`: Listeyi yerinde karıştırır ve yeni liste döndürmez.
- `sample(sequence, k)`: Tekrarsız `k` elemanlı örneklem döndürür.
- `uniform(a, b)`: İki sınır arasında ondalık sayı üretir.
- Dağılım fonksiyonları: `triangular`, `betavariate`, `expovariate`, `gammavariate`,
	`gauss`, `lognormvariate`, `normalvariate`, `vonmisesvariate`, `paretovariate`,
	`weibullvariate`.

## 04 - String Metotları

- `in` / `not in`: Bir metnin içinde alt metin veya karakter arar.
- `text[start:end]`: Bitiş indeksi dahil olmadan dilim alır; negatif indeks sondan başlar.
- `len()`: String uzunluğunu verir.
- `upper()`, `lower()`, `casefold()`, `capitalize()`, `title()`, `swapcase()`: Harf
	büyüklüğünü dönüştürür.
- `strip()`, `lstrip()`, `rstrip()`: Baştaki ve/veya sondaki karakterleri kaldırır.
- `replace()`: Bir metin parçasını başka bir metinle değiştirir.
- `split()`, `splitlines()`: Stringi listeye ayırır.
- `center()`, `ljust()`, `rjust()`, `zfill()`: Hizalama veya toplam genişlik sağlar.
- `find()` / `rfind()`: İndeks döndürür; bulamazsa `-1` verir.
- `index()`: İndeks döndürür; bulamazsa hata yükseltir.
- `count()`: Alt metnin kaç kez bulunduğunu sayar.
- `startswith()` / `endswith()`: Başlangıç veya bitiş kontrolü yapar.
- `join(iterable)`: Iterable elemanlarını ayraç stringiyle birleştirir.
- `expandtabs()`: `\t` karakterinin tab genişliğini ayarlar.
- `maketrans()` ve `translate()`: Karakter değiştirme/silme tablosu oluşturur ve uygular.
- `partition()` / `rpartition()`: Ayraç etrafında üç parçalı tuple döndürür.
- Kontrol metotları: `islower`, `isupper`, `isalnum`, `isascii`, `isdecimal`, `isdigit`,
	`isidentifier`, `isnumeric`, `isprintable`, `isspace`.

## 05 - Özel Karakterler

- `\"`, `\'`: Tırnak karakterlerini string içinde kullanır.
- `\\`: Ters bölü karakteridir.
- `\n`: Yeni satır, `\r`: satır başına dönüş, `\t`: tab, `\b`: backspace karakteridir.
- `\120`: Oktal karakter gösterimi; `\x50`: hexadecimal karakter gösterimidir.
- `\r` ve `\b` çıktısının terminalde nasıl göründüğü ortama göre değişebilir.

## 06 - String Formatlama

- f-string: `f"Merhaba {name}"` biçiminde ifadeyi string içine yerleştirir.
- `f"{price:.2f}"`: Ondalık kısmı iki basamakla biçimlendirir.
- `str.format()`: `{}` yer tutucularını değerlerle doldurur.
- Hizalama: `:<4` sol, `:>4` sağ, `:^4` orta hizalamadır.
- İşaret biçimleri: `:+` pozitif işareti gösterir, `: ` pozitif sayının önüne boşluk koyar.
- `:,` ve `:_`: Binlik ayırıcı kullanır.
- `:b`, `:c`, `:d`, `:e`, `:o`, `:x`: İkilik, Unicode karakter, ondalık, bilimsel,
	sekizlik ve hexadecimal biçimlerdir.
- `notVize` ve `notFinal` `input()` ile string gelir; hesaplama için `float()` gerekir.

## 07 - ASCII ve Kodlama

- `ord(character)`: Karakterin Unicode code point değerini verir; ASCII karakterlerde bu
	değer ASCII koduyla aynıdır.
- `bin(number)`: Sayıyı ikilik gösterime çevirir.
- `int(value, base)`: Belirtilen tabandaki stringi tam sayıya çevirir.
- `bit_length()`: Bir tam sayının işaret biti hariç bit uzunluğunu verir.
- `encode()`: Stringi `bytes` değerine çevirir; `decode()`: bytes değerini stringe çevirir.
- `backslashreplace`, `ignore`, `namereplace`, `replace`, `xmlcharrefreplace`: Kodlama
	sırasında desteklenmeyen karakterlerin ele alınma biçimleridir.
- UTF-8, Türkçe karakterleri ASCII'den daha geniş biçimde destekler.

## 08 - Koşullar

- `if`, `elif`, `else`: Koşula göre farklı kod bloklarını çalıştırır.
- Girintileme Python'da blok yapısının parçasıdır.
- `bool(value)`: Değerin doğruluk karşılığını verir.
- `None`, `False`, `0`, `""` ve boş list/tuple/set/dict değerleri false kabul edilir.
- Örnek değişkenler: `sayi1`, `sayi2`, `x`, `y`.

## 09 - Operatörler

- Aritmetik: `+`, `-`, `*`, `/`, `%`, `**`, `//`.
- Atama: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.
- Karşılaştırma: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- Mantıksal: `and`, `or`, `not`.
- `/` normal bölme, `//` floor uygulanmış bölmedir; negatif sayılarda sıfıra değil aşağıya yuvarlar.
- `sayi`: Bileşik atama operatörlerinin sonuçlarını göstermek için kullanılan değişkendir.

## 10 - Liste Metotları

- `copy()`: Sığ kopya üretir; iç içe mutable nesneler paylaşılabilir.
- `append(value)`: Sona tek eleman ekler.
- `insert(index, value)`: Belirtilen indekse ekler.
- `extend(iterable)`: Iterable içindeki elemanları tek tek ekler.
- `pop(index=-1)`: Elemanı siler ve silinen değeri döndürür.
- `remove(value)`: İlk eşleşen değeri siler.
- `clear()`: Listeyi boşaltır; `del list_name` isim bağını kaldırır.
- `sort()`: Listeyi yerinde sıralar; `reverse()`: Listeyi yerinde ters çevirir.
- Örnek listeler: `fruit`, `fruit2`, `newfruit`, `esyalar`.

## 11 - `while` Döngüsü

- `while condition`: Koşul doğru olduğu sürece bloğu tekrarlar.
- Sayaçlı döngüde başlangıç, koşul ve sayaç değişimi bulunmalıdır.
- `break`: Döngüyü tamamen bitirir.
- `continue`: Mevcut turu atlayıp sonraki tura geçer.
- `i`: Sayaç olarak kullanılan değişkendir. Sayaç değişmezse sonsuz döngü oluşabilir.

## 12 - `for` Döngüsü

- `for item in sequence`: Iterable elemanlarını sırayla gezer.
- `range(8)`: `0` dahil, `8` hariç sayıları üretir.
- `end=" "`: `print()` fonksiyonunun varsayılan satır sonunu değiştirir.
- `break` döngüyü bitirir, `continue` mevcut turu atlar.
- `pass` ve `...`, henüz kod yazılmamış bloklar için yer tutucudur.

## 13 - Tuple

- Tuple sıralı, tekrara izin veren ve eleman atamasıyla değiştirilemeyen bir koleksiyondur.
- Tek elemanlı tuple için virgül gerekir: `("karpuz",)`.
- `("kavun")` tuple değil stringdir.
- `fruits * 2`, tuple elemanlarını tekrarlar.
- `x, y, *z = fruits`: Unpacking yapar; `z` kalan elemanları liste olarak toplar.
- Tuple değiştirilemez olsa da içinde bulunan mutable bir listenin içeriği değişebilir.

## 14 - Set

- Set tekrarsız, sırasız ve değiştirilebilir bir koleksiyondur.
- `add()`: Eleman ekler; `update()`: Iterable elemanlarını ekler.
- `remove()`: Eleman yoksa `KeyError`; `discard()`: Eleman yoksa hata vermez.
- `pop()`: Belirli sıra garantisi olmadan bir eleman kaldırır.
- `clear()`: Seti boşaltır; `del`: Set isim bağını siler.
- Küme işlemleri: `intersection`, `intersection_update`, `union`, `difference`,
	`difference_update`, `symmetric_difference`, `symmetric_difference_update`.
- Küme ilişkileri: `isdisjoint`, `issubset`, `issuperset`.

## 15 - Dictionary

- Dictionary anahtar-değer çiftlerinden oluşur; anahtarlar benzersiz, değerler tekrarlı olabilir.
- Python 3.7 ve sonrasında ekleme sırasını korur.
- `keys()`, `values()`, `items()`: Sırasıyla anahtar, değer ve çift view nesneleri döndürür.
- `update()`: Var olan anahtarı günceller veya yeni anahtar ekler.
- `pop(key)`, `popitem()`, `clear()`: Eleman silme ve temizleme işlemleridir.
- `copy()` ve `dict(existing)`: Sığ dictionary kopyası oluşturur.
- `setdefault(key, default)`: Anahtar yoksa varsayılan değerle oluşturur.
- `dict.fromkeys(keys, value)`: Verilen anahtarlarla dictionary oluşturur.
- İç içe dictionary örneği: `ardakaslarim["arkadas1"]["year"]`.
- `car`, `person`, `ardakaslarim`, `anahtar`, `deger`, `result` dosyada kullanılan değişkenlerdir.

## 16 - Fonksiyonlar

- `def`: Fonksiyon tanımlar; `return`: Sonuç döndürür.
- Parametre fonksiyona veri sağlar; varsayılan parametre çağrıda değer verilmezse kullanılır.
- `*args`: Değişken sayıda konumsal argümanı tuple olarak toplar.
- `**kwargs`: Değişken sayıda isimli argümanı dictionary olarak toplar.
- İsimli argümanlarda çağrı sırası önemini kaybeder.
- Fonksiyon başka bir fonksiyonu parametre olarak alabilir veya fonksiyon içinde tanımlanabilir.
- `fac(n)`: Faktöriyel, `fib(n)`: Fibonacci, `topla(n)`: 1'den `n`'e toplam için recursive örneklerdir.
- Recursive fonksiyonlarda temel durum bulunmazsa sonsuz çağrı oluşur.
- Dosyadaki değişken ve fonksiyonlar: `name`, `dinamik_fonksion`, `isim`, `my_name`,
	`my_counrty`, `mat`, `carp`, `x`, `outer_function`, `square`, `sum_and_square`, `fac`, `fib`, `topla`.

## 17 - Sayıyı Türkçe Yazıya Çevirme

- `number_to_words(number)`: 1000-9999 aralığındaki sayıyı Türkçe metne dönüştürür.
- `ones` ve `tens`: Birler ve onlar basamağı karşılıklarını tutan listelerdir.
- `%` ve `//` ile `one_digit`, `ten_digit`, `hundred_digit`, `thousand_digit` ayrıştırılır.
- `result`: Parçaların birleştirilmesiyle oluşan sonuç stringidir.
- Geçersiz aralık veya sayı girişi için mesaj döndürülür.

## 18 - `math` Modülü

- Sabitler: `e`, `inf`, `nan`, `pi`, `tau`.
- Trigonometri: `acos`, `acosh`, `asin`, `asinh`, `atan`, `atan2`, `atanh`.
- Dönüşüm: `degrees()` radyanı dereceye, `radians()` dereceyi radyana çevirir.
- Yuvarlama/kök: `ceil`, `floor`, `sqrt`, `isqrt`, `trunc`.
- `comb`, `perm`, `factorial`, `gcd`, `prod`: Kombinasyon, permütasyon, faktöriyel,
	ortak bölen ve çarpım işlemleri.
- `dist`, `hypot`: Öklid mesafesi/normu hesaplar; `hypot(3, 4)` 5 verir.
- `remainder`: Normal `%` kalanı değil, IEEE 754 kalanını hesaplar.
- `isfinite`, `isinf`, `isnan`, `isclose`: Sayısal durum ve yakınlık kontrolleridir.
- `log`, `log10`, `log1p`, `log2`, `exp`, `expm1`, `exp2`: Logaritma ve üstel işlemler.
- `fmod`, `frexp`, `fsum`, `gamma`, `lgamma`, `copysign`, `modf`, `ldexp`, `pow`: Diğer sayısal yardımcılar.

## 19 - `cmath` Modülü

- Karmaşık sayılarla matematiksel işlem yapar.
- Sabitler: `e`, `inf`, `infj`, `nan`, `nanj`, `tau`.
- `sqrt`, `acos`, `acosh`, `asin`, `asinh`, `atan`, `atanh`, `exp`, `log`, `log10` karmaşık değerlerle çalışır.
- `isfinite`, `isinf`, `isnan`, `isclose`: Karmaşık değer kontrolleridir.
- `phase()`: Karmaşık sayının açısını verir.
- `polar()`: Karmaşık sayıyı `(yarıçap, açı)` biçimine çevirir.
- `rect(radius, angle)`: Kutupsal gösterimi karmaşık sayıya çevirir.

## 20 - `statistics` Modülü

- `harmonic_mean()`: Harmonik ortalama; `mean()`: Aritmetik ortalama.
- `median()`: Ortanca; `median_grouped()`: Gruplanmış veri için ortanca.
- `median_high()` ve `median_low()`: Çift sayıda veride ortadaki büyük/küçük değeri verir.
- `mode()`: Mod; `multimode()`: Birden fazla modu liste olarak verir.
- `pstdev()` / `pvariance()`: Anakütle standart sapması/varyansı.
- `stdev()` / `variance()`: Örneklem standart sapması/varyansı.
- `data`: Dosyadaki örnek veri listesidir.

## 21 - `datetime`, `time` ve `locale`

- `datetime as dt`, `timezone as tz`, `timedelta as td`, `time as tm`: Kısaltılmış importlardır.
- `dt.now()`: Güncel tarih-saat; `.hour`, `.minute`, `.second`, `.microsecond`: Alan özellikleri.
- `weekday()`: Pazartesi `0`, pazar `6` olacak şekilde gün indeksini verir.
- `ctime()`: Okunabilir tarih metni; `strftime()`: Tarihi biçimlendirilmiş stringe çevirir.
- `strptime(text, format)`: Stringi `datetime` nesnesine çevirir.
- `timestamp()`: Unix zaman damgası verir.
- `td(days=...)`: Tarih-saat ekleme/çıkarma için süre nesnesidir.
- `date`, `time`, `datetime.combine()`, `replace()`: Tarih-saat oluşturma/birleştirme/güncelleme.
- `tm.sleep(seconds)`: Programı bekletir; `process_time()`: CPU süresini ölçer.
- `locale.setlocale()`: Tarih biçimlerinin dilini işletim sistemine göre değiştirir; locale isimleri
	her işletim sisteminde aynı olmayabilir.

## 22 - Kendi Modülünü Oluşturma

### `22-ModuleOlusturma/BenimModulum.py`

- `number`: Modül seviyesinde `7` değerini taşıyan değişken.
- `person`: `name`, `age`, `country` anahtarlarına sahip dictionary.
- `gretting(name="Python")`: Varsayılan isimle veya verilen isimle selamlama stringi döndürür.

### `22-ModuleOlusturma/Kod.py`

- `import BenimModulum as bm`: Modülü `bm` takma adıyla içe aktarır.
- `bm.number`, `bm.person`, `bm.gretting()`: Modül üyelerine erişim örnekleridir.
- `from BenimModulum import *`: Üyeleri doğrudan içe aktarır; isim çakışmalarına dikkat edilmelidir.

## 23 - Lambda

- `lambda`: Genellikle tek ifadeli, isimsiz kısa fonksiyon oluşturur.
- `lambda x: x + 10`, eşdeğer bir `def` fonksiyonunun kısa biçimidir.
- Ternary ifade: `değer1 if koşul else değer2`.
- `("pozitif değil", "pozitif")[sayi > 0]`: Boolean indeksleme ile seçim yapar; iki seçenek
	ifadesi de önceden değerlendirilebilir.
- `kontrol`: Sayının pozitif olup olmadığını string olarak döndüren lambda değişkenidir.

## 24 - `map`, `filter`, `sorted` ve Closure

- `map(function, iterable)`: Her elemana fonksiyon uygular ve iterator döndürür.
- `filter(function, iterable)`: Fonksiyonun doğru döndürdüğü elemanları seçer.
- `sorted(iterable, reverse=True)`: Yeni sıralı liste döndürür; orijinal listeyi değiştirmez.
- `key=lambda x: abs(x)`: Sıralama anahtarını belirler.
- `carp(x)`: Sayıyı ikiyle çarpar.
- `my_function(n)`: `lambda x: x*n` döndürür; dış `n` değerini kapatan bir closure oluşturur.
- `numbers`, `list1`, `list2`, `liste`, `degerler`: Örnek iterable değişkenleridir.

## 25 - Decorator

- Decorator, bir fonksiyonu sarmalayıp davranışını genişleten fonksiyondur.
- `@decorator_function`: Fonksiyon çağrısına başlangıç/bitiş mesajı ekler.
- `authentication`: `user["auth"]` değerini kontrol eder ve yetkisiz kullanıcıyı engeller.
- `timer_decoration`: Fonksiyonun çalışma süresini ölçer.
- `flexible_decorator`: `*args`, `**kwargs` ve dönüş değerini raporlar.
- `wrapper(*args, **kwargs)`: Sarılan fonksiyonun farklı argümanlarını iletir.
- `func.__name__`: Fonksiyonun adıdır; `functools.wraps()` kullanılmazsa decorator sonrası metadata kaybolabilir.
- Örnek fonksiyonlar: `myMessage`, `view_account`, `slow_function`, `fast_function`,
	`faster_function`, `add`, `greet`, `multiply_and_sum`.

## 26 - OOP Temelleri

- `class`: Nesnelerin şablonunu oluşturur.
- `__init__`: Constructor/kurucu metottur; nesne oluşturulurken çalışır.
- `self`: O anki nesneyi temsil eden ilk instance parametresidir.
- Attribute/property: Nesneye ait `brand`, `model`, `color`, `name`, `age` gibi verilerdir.
- `Vehicle`: `brand`, `model`, `color` özelliklerine sahip araç sınıfıdır.
- `Person`: `__str__` ile kullanıcıya yönelik, `__repr__` ile geliştiriciye yönelik gösterim sağlar.
- `Person2.myInfo()`: Normal instance metodu örneğidir.
- `__str__` ve `__repr__` dunder metotlardır; normal metotlar `.method_name()` ile çağrılır.

## 27 - Kalıtım ve Metot Ezme

- `Kisi`: `firstname`, `lastname`, `myPrint()` içeren üst sınıftır.
- `Ogrenci(Kisi)`: `Kisi` sınıfından miras alır; `graduationyear` ve `welcome()` ekler.
- `super().__init__()`: Üst sınıfın constructor'ını çağırır.
- `Dog` ve `Cat`, `Animal.speak()` metodunu override eder.
- `Mouse`, override yapmadan üst sınıf metodunu kullanır.
- `isinstance(object, class)`: Nesnenin sınıf veya üst sınıf ilişkisini kontrol eder.
- `issubclass(class1, class2)`: Bir sınıfın diğerinden türeyip türemediğini kontrol eder.

## 28 - OOP Uygulaması

- `Animal`: `name`, `is_alive`, `eat()`, `sleep()` üyelerine sahiptir.
- `Dog`: `sound()` ekler.
- `Cat`: `sleep()` metodunu override eder ve `sound()` ekler.
- `Mouse`: `pass` kullanır ve yalnızca miras aldığı davranışları taşır.
- `Rabbit`: `super()` ile üst constructor'ı çağırır ve `is_hopping` özelliği ekler.
- `hasattr(object, name)`: Nesnede belirli attribute bulunup bulunmadığını kontrol eder.
- `animals`: Farklı sınıf nesnelerini aynı listede tutan örnek değişkendir.

## 29 - Sihirli/Dunder Metotlar

- `CustomList`: Liste benzeri davranış sağlar.
	- `__len__`: `len()` davranışı.
	- `__getitem__`: `obj[index]` okuması.
	- `__setitem__`: `obj[index] = value` ataması.
	- `__delitem__`: `del obj[index]` silmesi.
- `Greet.__call__`: Nesneyi fonksiyon gibi çağrılabilir yapar.
- `Person`: `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__` ile karşılaştırılabilir.
- `Number`: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`,
	`__pow__`, `__neg__`, `__pos__`, `__abs__`, `__str__` metotlarını uygular.
- Sıfıra bölmede `ValueError` yükseltilmelidir; hata nesnesini `return` etmek hata oluşturmaz.
- `__del__`, `del obj[index]` ile aynı şey değildir; nesne finalizer'ıdır.
- `IslevDisi.__getitem__`: Okuma yerine eleman silen özel davranış örneğidir.

## 30 - Iterator ve Attribute Dunder Metotları

- `iter(iterable)`: Iterator oluşturur.
- `next(iterator)`: Sonraki değeri döndürür; değer kalmayınca `StopIteration` oluşur.
- `Counter`: `__iter__` ve `__next__` ile özel iterator sınıfıdır.
- `__delattr__`: Attribute silme davranışını kontrol eder.
- `__getattr__`: Normal aramayla bulunamayan attribute için çalışır.
- `__setattr__`: Attribute atamasını kontrol eder.
- `hasattr()`: Attribute varlığını test eder.
- `__int__` ve `__float__`: Nesnenin `int()` veya `float()` ile dönüştürülmesini sağlar.
- Örnekte `Person.name` silinemez, `number` silinebilir.

## 31 - Kapsülleme

- Public: Her yerden erişilebilir üyeler.
- `_protected`: Python'da gerçek erişim yasağı değildir; iç kullanım konvansiyonudur.
- `__private`: Name mangling kullanır; gerçek güvenlik mekanizması değildir.
- `Car`: `brand`, `model`, `display_info()`.
- `Animal`: `_species` ve `_makeSound()` protected üyeleri.
- `Dog`: Protected üyeleri miras yoluyla kullanır.
- `BankAccount`: `account_number` public, `__balance` private attribute'tur.
- `deposit(amount)`: Pozitif miktarı bakiyeye ekler.
- `__display_balance()`: Private metottur; `get_balance()` kontrollü public arayüzdür.

## 32 - Polymorphism

- Polymorphism, aynı metot arayüzünün farklı sınıflarda farklı davranmasıdır.
- `Vehicle.move()`: Genel hareket davranışı.
- `Car.move()`: Karada sürüş; `Boat.move()`: Suda ilerleme; `Airplane.move()`: Uçuş.
- `Bicycle`: Üst sınıftaki `move()` metodunu kullanır.
- `vehicles`: Farklı türden nesneleri aynı `move()` çağrısıyla işleyen listedir.

## 33 - Abstract Class ve Duck Typing

- `ABC`: Soyut sınıf oluşturmak için kullanılan temel sınıftır.
- `@abstractmethod`: Alt sınıfların uygulaması gereken metodu belirtir; abstract metodun gövdesi olabilir.
- `Shape`: `area()` ve dosyada kullanılan `primer()`/perimeter kavramını tanımlar.
- `Rectangle`: `width`, `height`, alan ve çevre hesabı.
- `Circle`: `radius`, alan ve çevre hesabı.
- Abstract sınıftan eksik abstract metotlarla doğrudan nesne üretilemez.
- Duck typing'de kalıtım şart değildir: `Dog`, `Cat`, `Car` sınıfları `make_sound()` sağladığı
	sürece `play_sound(obj)` tarafından kullanılabilir.

## 34 - Aggregation ve Composition

- Aggregation: `Department`, dışarıda oluşturulan `Employee` nesnelerini listesinde tutar;
	çalışanlar bölümden bağımsız yaşayabilir.
- `add_employee()`: Department'a çalışan ekler.
- Composition: `Department2`, constructor içinde employee nesnelerini kendisi oluşturur;
	bölüm ve çalışan arasındaki sahiplik daha güçlüdür.
- `show_department()`: Bölüm adını ve çalışanların `name`/`emp_id` özelliklerini yazdırır.
- `Employee` ve `Employee2`: Çalışan adı ve kimliği taşıyan sınıflardır.

## 35 - İç İçe Sınıf ve Static Method

- `Car.Engine`: `Car` içinde tanımlanan inner class'tır; her `Car` nesnesi bir `Engine` nesnesi oluşturur.
- `Car` attribute'ları: `brand`, `model`, `engine`.
- `Engine` attribute'ları: `type`, `horse_power`, `fuel_type`.
- `show_details()` ve `show_engine()`: Araç/motor bilgilerini gösterir.
- `MathOperations`: Instance veya class state kullanmayan matematik metotlarını toplar.
- `@staticmethod`: `self` veya `cls` almayan metotları sınıf namespace'i içinde tanımlar.
- `add`, `sub`, `mul`, `div`, `div_floor`: Aritmetik static metotlardır.

## 36 - `classmethod`

- `@classmethod`: İlk argüman olarak sınıfı `cls` adıyla alır.
- `cls(...)`: Mevcut sınıftan nesne üretir; alt sınıflarla da uyumlu alternatif constructor sağlar.
- `Person.birth_year(name, birth_year)`: Doğum yılından yaş hesaplayıp `Person` üretir.
- `Employee.set_company()`: Sınıf seviyesinde `company` değerini ayarlar.
- `Employee.get_value()`: Maaşı `int` yaparak Employee nesnesi üretir.
- Classmethod'lar alternatif constructor ve class seviyesinde ortak veri yönetimi için kullanılır.

## 37 - Getter, Setter, Deleter

- `@property`: Bir metodu attribute gibi kullanmayı sağlar.
- Getter: Property okunduğunda çalışır ve değeri döndürür.
- Setter: `property = value` atamasını doğrular veya dönüştürür.
- Deleter: `del property` çağrısında çalışır.
- `Person.name`: Asıl saklanan instance attribute'udur.
- `name_function`: `name` için kontrollü getter/setter/deleter arayüzüdür.
- Setter boş isimde `ValueError` yükseltir; deleter adı `None` yapar.

## 38 - Metaprogramming

- Metaprogramming, programın çalışma zamanında kendi yapılarını oluşturması veya değiştirmesidir.
- `newMethod(self)`: Sonradan sınıfa bağlanacak fonksiyondur.
- `Person.newMethod = newMethod`: Runtime monkey patching ile metoda sınıf üzerinden bağlanır.
- `p1.newMethod()`: Bağlanan fonksiyonun instance metodu gibi kullanılmasını gösterir.
- Bu örnek metaprogramming'in bir uygulamasıdır; metaclass kullanımı gibi daha ileri teknikleri kapsamaz.

## Temel Kavramlar: Kısa Sözlük

- **Fonksiyon:** Girdi alabilen ve işlem sonucunu `return` ile döndüren tekrar kullanılabilir kod bloğu.
- **Değişken:** Bir değere bağlanan isim.
- **Attribute/Property:** Nesne veya sınıfa ait veri; `obj.name` biçiminde erişilir. `property`,
	getter/setter/deleter ile erişimi kontrol edebilir.
- **Class:** Nesne üretmek için attribute ve metotları bir araya getiren şablon.
- **Instance:** Bir class çağrısından üretilen nesne.
- **Method:** Bir class içinde tanımlı fonksiyon. Instance method `self`, classmethod `cls` alır;
	static method otomatik olarak `self` veya `cls` almaz.
- **Constructor:** Python'da yaygın olarak `__init__` ile nesne başlangıç değerlerini ayarlar.
- **Inheritance:** Bir sınıfın başka sınıfın davranışlarını miras alması.
- **Override:** Alt sınıfın üst sınıftaki metodu kendi davranışıyla yeniden tanımlaması.
- **Dunder method:** Başında ve sonunda çift alt çizgi bulunan özel protokol metodu; örneğin `__len__`.
