 #? Karmaşık sayılar üzerinde matematiksel işlemler

import cmath

print("-----Sabitler-----")
print(f"cmath.e → {cmath.e}")
print(f"cmath.inf → {cmath.inf}")
print(f"-cmath.inf → {-cmath.inf}")
print(f"cmath.infj → {cmath.infj}")
print(f"cmath.nan → {cmath.nan}")
print(f"cmath.nanj → {cmath.nanj}")
print(f"cmath.pi → {cmath.pi}")
print(f"cmath.tau → {cmath.tau}")
print("------------------------------------------")

z = 2 + 3j

#? Kök, kuvvet ve logaritma
print("-----Kök, Kuvvet ve Logaritma-----")
print(f"cmath.sqrt(-1) → {cmath.sqrt(-1)}") #* karmaşık karekökü alır
print(f"cmath.sqrt(4 + 3j) → {cmath.sqrt(4 + 3j)}")

print(f"cmath.exp({z}) → {cmath.exp(z)}") #* e üzeri karmaşık sayıyı hesaplar

print(f"cmath.log({z}) → {cmath.log(z)}") #* doğal logaritmayı alır
print(f"cmath.log({z}, 2) → {cmath.log(z, 2)}") #* verilen tabanda logaritma alır
print(f"cmath.log10({z}) → {cmath.log10(z)}") #* 10 tabanında logaritma alır
print("------------------------------------------")

#? Trigonometrik fonksiyonlar
print("-----Trigonometrik Fonksiyonlar-----")
print(f"cmath.sin({z}) → {cmath.sin(z)}")
print(f"cmath.asin({z}) → {cmath.asin(z)}")

print(f"cmath.cos({z}) → {cmath.cos(z)}")
print(f"cmath.acos({z}) → {cmath.acos(z)}")

print(f"cmath.tan({z}) → {cmath.tan(z)}")
print(f"cmath.atan({z}) → {cmath.atan(z)}")
print("------------------------------------------")

#? Hiperbolik fonksiyonlar
print("-----Hiperbolik Fonksiyonlar-----")
print(f"cmath.sinh({z}) → {cmath.sinh(z)}")
print(f"cmath.asinh({z}) → {cmath.asinh(z)}")

print(f"cmath.cosh({z}) → {cmath.cosh(z)}")
print(f"cmath.acosh({z}) → {cmath.acosh(z)}")

print(f"cmath.tanh({z}) → {cmath.tanh(z)}")
print(f"cmath.atanh({z}) → {cmath.atanh(z)}")
print("------------------------------------------")

#? Kutupsal ve dikdörtgensel gösterim
print("-----Karmaşık Sayı Gösterimleri-----")
print(f"cmath.phase({z}) → {cmath.phase(z)}") #* karmaşık sayının açısını verir
print(f"cmath.polar({z}) → {cmath.polar(z)}") #* (uzaklık, açı) çiftini verir
print(f"cmath.rect(3.6055, 0.9828) → {cmath.rect(3.6055, 0.9828)}") #* kutupsal bilgiyi karmaşık sayıya çevirir
print(f"cmath.conjugate({z}) → {cmath.conjugate(z)}") #* eşleniğini verir
print(f"cmath.isfinite({z}) → {cmath.isfinite(z)}") #* reel ve sanal kısımların sonlu olup olmadığını kontrol eder
print(f"cmath.isinf({z}) → {cmath.isinf(z)}") #* sonsuz olup olmadığını kontrol eder
print(f"cmath.isnan({z}) → {cmath.isnan(z)}") #* NaN olup olmadığını kontrol eder
print("------------------------------------------")

#? Karşılaştırma
print("-----Yakınlık Kontrolü-----")
print(f"cmath.isclose(10 + 7j, 10 + 7j) → {cmath.isclose(10 + 7j, 10 + 7j)}")
print(f"cmath.isclose(10 + 7j, 10 + 7.001j, abs_tol=0.005) → {cmath.isclose(10 + 7j, 10 + 7.001j, abs_tol=0.005)}")
print("------------------------------------------")
print("cmath.sqrt(-1) =>",cmath.sqrt(-1)) #* karakökü alır
print("cmath.sqrt(4+3j) =>",cmath.sqrt(4+3j)) #* karakökü alır
