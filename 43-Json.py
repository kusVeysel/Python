import json

#? JSON Nedir?
#* JSON, verilerin saklanması ve aktarılması için kullanılan bir veri formatıdır
#* Python'un kendine ait bir JSON veri türü yoktur
#* JSON verisi Python'a çevrildiğinde dict, list, str, int, bool vb. türlere dönüşür


#? Python Dict → JSON String

person1 = {
    "name": "Veysel",
    "age": 19,
    "city": "Kahramanmaraş",
    "hobbies": ["Kod yazma", "Film İzleme", "Masa Tenisi Oynama"]
}

#* Python'da person1 bir dict veri türüdür
print(type(person1))


#? JSON String

person2 = '{"name": "Veysel", "age": 19, "city": "Kahramanmaraş", "hobbies": ["Kod yazma", "Film İzleme", "Masa Tenisi Oynama"]}'

#* person2 Python açısından str veri türüdür
#* İçeriği JSON formatında olduğu için JSON string olarak kullanılır
print(type(person2))


#? json.dumps()
#* Python verisini JSON formatındaki string'e çevirir

result1 = json.dumps(
    person1,
    ensure_ascii=False,
    indent=4,
    sort_keys=True,
    separators=(",", ": ")
)

#* ensure_ascii=False → Türkçe karakterlerin düzgün görünmesini sağlar
#* indent=4 → Veriyi 4 boşluk girintili şekilde düzenler
#* sort_keys=True → Anahtarları alfabetik olarak sıralar
#* separators=(".", "= ") → JSON'daki ayraçları belirler

print(result1)


#? json.loads()
#* JSON string'i dict veri türüne çevirir
#* JSON object → Python dict
#* JSON array → Python list

result2 = json.loads(person2)

print(type(result1))  # str
print(type(result2))  # dict


print("------------------------------------------")
#? Dosyadan JSON Veri Okuma

with open("data.json", "r", encoding="utf-8") as f:

    #* json.load() → JSON dosyasındaki veriyi okur ve dict veri türüne çevirir, dosyadan json okunurken loads() değil load() kullanılır

    convert = json.load(f)

    print(convert["name"])
    print(convert["age"])
    print(convert["city"])

    for hobby in convert["hobbies"]:
        print(hobby, end=" ")


print("\n------------------------------------------")
#? Python Dict → JSON Dosyası

with open("people.json", "w", encoding="utf-8") as f:

    #* json.dump() → Python verisini JSON formatında doğrudan dosyaya yazar, dosyaya yazarken dumps() değil dump() kullanılır

    json.dump(
        person1,
        f,
        ensure_ascii=False,
        indent=4
    )


#? Kısa Mantık

#* dumps()  : Python(dict) → JSON string
#* loads()  : JSON string  → Python(dict)
#* dump()   : Python(dict) → JSON dosyası
#* load()   : JSON dosyası → Python(dict)