
#? dictionary
#* Sıralıdır: Kod her çalıştığında veriler hangi sırayla yazıldıysa öyle gelir
#* Değiştirilebilir: Veriler değiştirilebilir
#* Yinelenemez: Aynı veri kullanılamaz

car = {
    "brand": "skoda",
    "model": "octavia",
    "colors":["red","black","white"],
    "year":"1959"
}

print(f"{car['brand']}, {car['model']}, {car['year']}, {car['colors']} "),

person = dict(name="Veysel",age=19,country="Türkiye")

print(f"{person.get('name')}, {person.get('age')}, {person.get('country')}")

person["student"] = True #* yeni key-value oluşturur
print(person)

print()
#? Dictionary Methodlar

#? keys(): 
my_keys = car.keys() #* car dictionary'nin keylerini döner
print("car.keys() =>",my_keys)

#? values()
my_values = car.values() #* car dictionary'nin değerlerini döner
print("car.values() =>",my_values)

#? items()
result = car.items()
print(result) #* key-value çiftlerini view nesnesi olarak döner
#* sözlükteki değişiklikler view nesnesine yansır

#? update()
car.update({"tekerlek":4}) #* eğer dictionary tipinde , girilen değer(tekerlek) varsa veriyi günceller yoksa yeni bi key-value oluşturur
print("car.update({\"tekerlek\":4}) =>",car)

#? pop(silinecek_key)
car.pop("colors")
print("car.pop(\"colors\") =>",car)

#? popitem(): son keyi kaldırır
car.popitem()
print("car.popitem() =>",car)

#* clear(): dictionary içindeki verileri siler
car.clear() 

del car #*car dictionary'sini komple siler

#? copy()
kisi = person.copy() #* sığ (shallow) kopyadır; iç içe nesneler paylaşılabilir

#? 2.kopyalama yolu
kisi2 = dict(person)

print()
#? dictionary içinde dictionary

ardakaslarim = {
    "arkadas1":{
        "name":"Mehmet",
        "year":2006
    },
    "arkadas2":{
        "name":"Çaycı",
        "year":2007
    },
    "arkadas3":{
        "name":"Eren",
        "year":2009
    }
}
#? dictionary içindeki dictionary'nin property'sine erişmek
print(ardakaslarim["arkadas1"]["year"])

for outer_key,outer_value in ardakaslarim.items():
    for inner_key in outer_value:
        print(f"{inner_key}:{outer_value[inner_key]}")


print()
anahtar = ("key1","key2","key3")
deger = 7,8,3
result = dict.fromkeys(anahtar,deger) #* dictionary oluşturur
print(result)

result = person.setdefault("name","abuzer") #* 1.parametredeki keyin değerini döndürür, 1.parametredeki key yoksa , 1.ve 2.parametredekilerle yeni bir key-value oluşturur
print(result)
print(person)