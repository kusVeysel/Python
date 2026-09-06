
#? set
#* Sırasızdır: Kod her çalıştığında veriler sırasız(karışık sırayla gelir
#* Değiştirilemez: Veriler değiştirilemez
#* Yinelenemez: Aynı veri kullanılamaz

fruits = {"üzüm","kiraz","kapruz","kavun","armut","elma"}
fruits2 = {"hurma","domates","şeftali"}

print(fruits)

#? Set Methodları

#? add(eklenecek_eleman)
fruits.add("salatalık")
print("fruits.add(\"salatalık\") =>",fruits)

#? update(eklenecek_veri): extend ile aynı işlev
fruits.update(fruits2)
print("fruits.update(fruits2) =>",fruits)

#? remove(silinecek_eleman)
fruits2.remove("hurma")
print("fruits2.remove(\"hurma\") =>",fruits2)

#? discard(silinecek_eleman)
fruits2.discard("domates")
print("fruits2.discard(\"domates\") =>",fruits2)

#* remove() ile discard() arasındaki fark , eğer parametredeki veri, sette içermiyorsa remove() hata verirken discard() vermez

#? pop(): rastgele veri kaldırır
silinen_veri = fruits.pop()
print(f"silinen veri: {silinen_veri}")

#? clear(): setin içindeki verileri siler
fruits.clear()
print(fruits)

#? del: seti komple siler
del fruits2


number1 = {1,2,3,4,5,6}
number2 = {3,5,7,2,1}

#? intersection(set): kesişen veriler set olarak döner
result2 = number1.intersection(number2)
print("number1.intersection(number2) =>",result2)

#? intersection_update(set): kesişen veriler kalır
number1.intersection_update(number2)
print("number1.intersection_update(number2) =>",number1)


meyve1 = {"üzüm","kiraz","kapruz","kavun","armut","elma"}
meyve2 = {"hurma","domates","şeftali"}

#? union(set): setleri birleştirir ve yeni bi set döndürür  
result = meyve1.union(meyve2)
print("meyve1.union(meyve2) =>",result)

#? copy(): setin kopyasını döner
kopya = meyve2.copy()
print("kopya = meyve2.copy() =>",kopya)

number1 = {1,2,3,4,5,6}
number2 = {3,5,7,2,1}

#? difference(set): fark veri setini döner
fark = number1.difference(number2) #* number1'de olup number2'de olmayanları döner
print("number1.difference(number2) =>",fark)

number1.difference_update(number2) #* number1'de olup number2'de olmayanları tutar
print("number1.difference(number2) =>",number1)


number1 = {1,2,3,4,5,6}
number2 = {3,5,7,2,1}

#? symmetric_difference(set): kesişim dışındaki verileri döner
result = number1.symmetric_difference(number2)
print("number1.symmetric_difference(number2) =>",result)

#? symmetric_difference_update(set): kesişim dışındaki verileri atar
number1.symmetric_difference_update(number2)
print("number1.symmetric_difference(number2) =>",number1)


number1 = {1,2,3,4,5,6}
number2 = {3,5,7,2,1}

#? isdisjoint(set): ortak eleman varsa False, yoksa True döner
result = number1.isdisjoint(number2)
print("number1.isdisjoint(number2) =>",result)

#? issubset(set): elemanlar varsa True yoksa False döner, contains gibi(içeriyor mu?)
result = number1.issubset(number2) #* number1'deki tüm veriler number2'de var mı
print("number1.issubset(number2) =>",result)

#? issuperset(set): elemanlar varsa True yoksa False döner, contains gibi(içeriyor mu?)
result = number1.issuperset(number2) #* number2'deki tüm veriler number1'de var mı
print("number1.issuperset(number2) =>",result)
