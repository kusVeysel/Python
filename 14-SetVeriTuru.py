 #? set
#* Sırasızdır: Kod her çalıştığında veriler sırasız(karışık sırayla gelir
#* Değiştirilemez: Veriler değiştirilemez
#* Yinelenemez: Aynı veri tekrar kullanılamaz

my_set = {"veri1","veri2","veri3"}


#? Set Metotları

#* add(): Set'e tek bir eleman ekler

#* update(): Set'e başka bir iterable'ın elemanlarını ekler
# → Liste, tuple, set vb. iterable'lar eklenebilir.
# → Genellikle iki seti birleştirmek için kullanılır.

#* remove(): Belirtilen elemanı siler
#! Eleman sette yoksa KeyError hatası verir

#* discard(): Belirtilen elemanı siler
#! Eleman sette yoksa hata vermez

#* pop(): Set'ten bir elemanı siler ve döndürür
#! Set sırasız olduğu için hangi elemanın silineceği garanti edilmez

#* del: Set değişkenini tamamen siler

#* clear(): Set içindeki tüm elemanları siler
# → Set boş bir set hâline gelir.

#* intersection(): İki veya daha fazla setin kesişimini yeni bir set olarak döndürür.

#* intersection_update(): Sadece kesişen elemanları sette tutar
# → Orijinal set değiştirilir.

#* union(): Setleri birleştirir ve yeni bir set döndürür
# → Tekrarlanan elemanlar yalnızca bir kez bulunur.

#* copy(): Setin sığ(shallow) kopyasını oluşturur

#* difference(): İki set arasındaki farkı yeni bir set olarak döndürür
# → İlk sette olup ikinci sette olmayan elemanlar.

#* difference_update(): Fark elemanlarını sette tutar
# → Orijinal set değiştirilir.

#* symmetric_difference(): İki sette bulunan ancak her ikisinde aynı anda bulunmayan elemanları yeni bir set olarak döndürür

#* symmetric_difference_update(): Ortak elemanları kaldırır, sadece iki sette farklı olan elemanları tutar
# → Orijinal set değiştirilir.

#* isdisjoint(): İki setin ortak elemanı olup olmadığını kontrol eder
# → Ortak eleman yoksa True
# → Ortak eleman varsa False

#* issubset(): Bir setin diğer setin alt kümesi olup olmadığını kontrol eder
# → İlk setteki TÜM elemanlar ikinci sette varsa True
# → Aksi durumda False

#* issuperset(): Bir setin diğer seti kapsayıp kapsamadığını kontrol eder
# → İkinci setin TÜM elemanları ilk sette varsa True
# → Aksi durumda False


fruit = {"Elma","Armut"} # set veri türü
fruit2 = {"Karpuz","Ayva"} # set veri türü
print(f"fruit → {fruit}")
print(f"fruit2 → {fruit2}")
print("------------------------------------------")

#? add()
fruit.add("Salatalık")
print('fruit.add("Salatalık") →',fruit)
print("------------------------------------------")

#? update()
fruit.update(fruit2)
print('fruit.update(fruit2) →',fruit)
print("------------------------------------------")

#? remove()
fruit.remove("Ayva")
print('fruit.remove("Ayva") →',fruit)
print("------------------------------------------")

#? discard()
fruit.discard("Karpuz")
print('fruit.discard("Karpuz") →',fruit)
print("------------------------------------------")

#? pop()
silinen_veri = fruit.pop()
print(f"fruit.pop() → {fruit}, silinen veri → {silinen_veri}")
print("------------------------------------------")

#? clear()
fruit.clear()
print("fruit.clear() →",fruit)
print("------------------------------------------")

#? del
del fruit


number1 = {1,2,3,4,5,6}
number2 = {3,5,7,2,1}
print(f"number1 → {number1}")
print(f"number2 → {number2}")
print("------------------------------------------")

#? intersection()
result = number1.intersection(number2)
print('result = number1.intersection(number2) →',result)
print("------------------------------------------")

#? intersection_update()
number1.intersection_update(number2)
print('number1.intersection_update(number2) →',number1)
print("------------------------------------------")


meyve1 = {"üzüm","kiraz","kapruz","kavun","armut","elma"}
meyve2 = {"hurma","domates","şeftali"}
print(f"meyve1 → {meyve1}")
print(f"meyve2 → {meyve2}")
print("------------------------------------------")

#? union()  
result = meyve1.union(meyve2)
print('result = meyve1.union(meyve2) →',result)
print("------------------------------------------")

#? copy()
kopya = meyve2.copy()
print('kopya = meyve2.copy() →',kopya)
print("------------------------------------------")

number3 = {1,2,3,4,5,6}
number4 = {3,5,7,2,1}
print(f"number3 → {number3}")
print(f"number4 → {number4}")
print("------------------------------------------")

#? difference()
fark = number3.difference(number4)
print('fark = number3.difference(number4) →',fark)
print("------------------------------------------")

#? difference_update()
number3.difference_update(number4)
print('number3.difference(number4) →',number3)
print("------------------------------------------")


number5 = {1,2,3,4,5,6}
number6 = {3,5,7,2,1}
print(f"number5 → {number5}")
print(f"number6 → {number6}")
print("------------------------------------------")

#? symmetric_difference()
result = number5.symmetric_difference(number5)
print('result = number5.symmetric_difference(number6) →',result)
print("------------------------------------------")

#? symmetric_difference_update()
number5.symmetric_difference_update(number6)
print('number5.symmetric_difference(number6) →',number5)
print("------------------------------------------")


number7 = {1,2,3,4,5,6}
number8 = {3,5,7,2,1}
print(f"number7 → {number7}")
print(f"number8 → {number8}")
print("------------------------------------------")

#? isdisjoint()
result = number7.isdisjoint(number8)
print('result = number7.isdisjoint(number8) →',result)
print("------------------------------------------")

#? issubset()
result = number7.issubset(number8)
print('result = number7.issubset(number8) →',result)
print("------------------------------------------")

#? issuperset(): 
result = number7.issuperset(number8)
print('result = number7.issuperset(number8) →',result)
print("------------------------------------------")
