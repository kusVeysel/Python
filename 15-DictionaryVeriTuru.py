 #? dictionary
#* Sıralıdır: Kod her çalıştığında veriler hangi sırayla yazıldıysa öyle gelir
#* Değiştirilebilir: Veriler değiştirilebilir
#* Yinelenemez: Aynı veri tekrar kullanılamaz

car = {
    "brand" : "skoda",
    "model" : "octavia",
    "colors" : ["red","black","white"],
    "year" : "1959"
} # dictionary veri türü

print(f"{car['brand']}, {car['model']}, {car['year']}, {car['colors']} ") #* değerlere dict["key"] ile erişilir

person = dict(name = "Veysel", age = 19, country = "Türkiye") #* dictionary veri türü (2.oluşturma yöntemi)

print(f"{person.get('name')}, {person.get('age')}, {person.get('country')}") #* değerlere get("key") ile de erişilebilir

person["student"] = True #! Keyin değerini günceller, key yoksa yeni key-value oluşturur
print(person)


#? Dictionary Metotları

#* keys(): Dictionary'nin key'lerini (anahtarlarını) döndürür
# → dict_keys view nesnesi döner.

#* values(): Dictionary'nin değerlerini döndürür
# → dict_values view nesnesi döner.

#* items(): Key-value çiftlerini view nesnesi olarak döndürür
# → dict_items view nesnesi döner.
# → Dictionary'deki değişiklikler view nesnesine yansır.

#* update(): Dictionary'yi başka key-value çiftleriyle günceller
# → Key varsa değerini günceller.
# → Key yoksa yeni bir key-value oluşturur.
# → Dictionary veya key-value çiftleri içeren iterable alabilir.

#* pop(): Belirtilen key'e ait key-value çiftini siler
# → Silinen value'yu geri döndürür.
#! Belirtilen key yoksa varsayılan değer verilmemişse KeyError verir.

#* popitem(): Son eklenen key-value çiftini siler ve döndürür
# → (key, value) tuple'ı döndürür.

#* clear(): Dictionary içindeki tüm key-value çiftlerini siler
# → Dictionary boş hâle gelir.

#* del: Belirtilen key'i veya dictionary'nin tamamını silebilir
# → del car["marka"]
# → del car

#* copy(): Dictionary'nin sığ (shallow) kopyasını oluşturur
#! İç içe mutable nesneler varsa bu nesneler iki dictionary arasında paylaşılabilir.


print("------------------------------------------")

#? keys()
my_keys = car.keys()
print("my_keys = car.keys() →",my_keys)
print("------------------------------------------")

#? values()
my_values = car.values()
print("my_values = car.values() →",my_values)
print("------------------------------------------")

#? items()
result = car.items()
print("result = car.items() →",result)
print("------------------------------------------")

#? update()
car.update({"tekerlek":4})
print('car.update({"tekerlek":4}) →',car)
print("------------------------------------------")

#? pop()
car.pop("colors")
print('car.pop("colors") →',car)
print("------------------------------------------")

#? popitem()
car.popitem()
print("car.popitem() →",car)
print("------------------------------------------")

#? copy()
new_dict = car.copy()
print("new_dict = car.copy() →",new_dict)
print("------------------------------------------")

#? 2.kopyalama yolu
person2 = dict(person)
print("dict(person) →",person2)
print("------------------------------------------")

#? clear()
car.clear() 
print("car.clear() →",car)
print("------------------------------------------")

del car


#? Dictionary İçinde Dictionary

ardakaslarim = {
    "arkadas1":{
        "name" : "Mehmet",
        "year" : 2006
    },
    "arkadas2":{
        "name" : "Çaycı",
        "year" : 2007
    },
    "arkadas3":{
        "name" : "Eren",
        "year" : 2009
    }
}

#? dictionary içindeki dictionary'nin property'sine erişmek
print(ardakaslarim["arkadas1"]["year"])

for outer_key,outer_value in ardakaslarim.items():
    for inner_key in outer_value:
        print(f"{inner_key}: {outer_value[inner_key]}")


print()

#? Dictionary oluşturma

anahtar = ("key1","key2","key3")
deger = 7,8,3
result = dict.fromkeys(anahtar,deger)
print(result)


result2 = person.setdefault("name","abuzer") #* 1.parametredeki keyin değerini döndürür, 1.parametredeki key dictionaryde yoksa , 1. ve 2.parametredekilerle yeni bir key-value oluşturur
print(result2)
print(person)