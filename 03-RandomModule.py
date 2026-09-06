 #? Random Module

#* random(): 0 ile 1 (1 dahil değil) arasında sayı üretir.

#* seed(): Üreteci verilen tohumla başlatır; aynı tohum aynı rastgele diziyi üretir.
# → Tohum verilmezse sistem rastgeleliği veya işletim sistemi zamanı kullanılır.

#* getstate(): Rastgele sayı üretecinin mevcut durumunu(state) kaydeder.

#* getrandbits(x): x bitlik rastgele sayı üretir.

#* randrange(BaşlangıçDeğeri, BitişDeğeri(DahilDeğil),ArtışMiktarı): Belirli aralıklarda belirli örüntüyle rastgele sayılar üretir.

#* randint(BaşlangıçDeğeri, BitişDeğeri): iki sayı arasında tamsayı üretir (başlangıç ve bitiş dahildir).

#* choices(dizi, weights = [GelmeOranı], k = Liste_kaç_adet): Diziden k adet rastgele seçim yapar. Aynı eleman birden fazla kez seçilebilir. weights ile seçim olasılıkları ağırlıklandırılabilir.
# choice(dizi): Diziden rastgele bir eleman döndürür

#* shuffle(dizi): Verilen dizinin elemanlarını rastgele karıştırır.

#* sample(Seri, k = x): Seriden tekrarsız k adet eleman seçer ve yeni bir liste döndürür.
# x: adet

#* uniform(Başlangıç_değeri, Bitiş_değeri): iki sayı arasında rastgele ondalıklı sayı üretir.
# → Alt ve üst sınırların seçilmesi kayan nokta yuvarlamasına bağlıdır.

#* triangular(Başlangıç_değeri, Bitiş_değeri, mode): 2 sayı arası sayı üretir.
# mode → kime yakınsa o sayıya yakın sayılar üretir


#* betavariate(alpha, beta): Büyük alpha dağılımı 1'e, büyük beta dağılımı 0'a doğru yoğunlaştırır.

#* expovariate(): Üstel dağılıma göre rastgele sayı döndürür.

#* gammavariate(): Gamma dağılıma göre rastgele sayı döndürür.

#* gauss(): Gaussian/Normal dağılıma göre rastgele sayı döndürür

#* lognormvariate(): Log-normal dağılıma göre rastgele sayı döndürür

#* normalvariate(): Normal dağılıma göre rastgele sayı döndürür

#* vonmisesvariate(): Von Mises(dairesel normal) dağılıma göre rastgele sayı döndürür

#* paretovariate(): Pareto dağılıma göre rastgele sayı döndürür

#* weibullvariate(): Weibull dağılıma göre rastgele sayı döndürür


import random 

#? random()
print(f"random.random() → {random.random()}")

#? seed()
random.seed()
print("------------------------------------------")
print(f"random.random() → {random.random()}")

#? getstate()
state = random.getstate()
next_number = random.random()

random.setstate(state)
print(f"random.setstate(state) sonrası aynı sayı → {random.random()} = {next_number}")

#? getrandbits()
print("------------------------------------------")
print(f"random.getrandbits(8) → {random.getrandbits(8)}") 
print("------------------------------------------")

#? randrange()
print(f"random.randrange(1,20,3) → {random.randrange(1,20,3)}")
print("------------------------------------------")
# 3.parametreden dolayı : 1,4,7,10,13,16,19 sayıları üretir

#? randint()
print(f"random.randint(1,10) → {random.randint(1,10)}")
print("------------------------------------------")

#? choice()
print(f"random.choice(['white','red','green','yellow','black']) → {random.choice(['white','red','green','yellow','black'])}")
print("------------------------------------------")

#? choices()
print(f"random.choices(['cherry','strawberry','grape','banana','apple'],weights=[10,3,5,1,1],k=20) → {random.choices(['cherry','strawberry','grape','banana','apple'], weights=[10,3,5,1,1],k=20)}")
print("------------------------------------------")

#? shuffle()
arabalar = ['skoda', 'bmw', 'audi', 'nissan', 'toyota', 'hyundai', 'volvo']
random.shuffle(arabalar)
print("random.shuffle(arabalar) →", arabalar)
print("------------------------------------------")

#? sample()
print(f"random.sample(['skoda','bmw','audi','nissan','toyota','hundai','volvo'], k = 3) → {random.sample(['skoda','bmw','audi','nissan','toyota','hundai','volvo'], k = 3)}")
print("------------------------------------------")

#? uniform()
print(f"random.uniform(10,30) → {random.uniform(10,30)}")
print("------------------------------------------")

#? triangular()
print(f"random.triangular(10,30,10) → {random.triangular(10,30,10)}")
print("------------------------------------------")



print("\n------Belirli Dağılımlara Göre Float Sayı Üreten Fonksiyonlar------")
print()

#? betavariate()
print("------------------------------------------")
print(f"random.betavariate(6,2) → {random.betavariate(6,2)}") 
print("------------------------------------------")

#? expovariate()
print(f"random.expovariate(1.0) → {random.expovariate(1.0)}")
print("------------------------------------------")

#? gammavariate()
print(f"random.gammavariate(110,2) → {random.gammavariate(110,2)}")
print("------------------------------------------")

#? gauss()
print(f"random.gauss(200,50) → {random.gauss(200,50)}")
print("------------------------------------------")

#? lognormvariate()
print(f"random.lognormvariate(0,0.25) → {random.lognormvariate(0,0.25)}")
print("------------------------------------------")
 
#? normalvariate()
print(f"random.normalvariate(100,50) → {random.normalvariate(100,50)}")
print("------------------------------------------")

#? vonmisesvariate()
print(f"random.vonmisesvariate(0,5) → {random.vonmisesvariate(0,5)}")
print("------------------------------------------")

#? paretovariate()
print(f"random.paretovariate(3) →{random.paretovariate(3)}")
print("------------------------------------------")

#? weibullvariate()
print(f"random.weibullvariate(1,1.5) → {random.weibullvariate(1,1.5)}")
print("------------------------------------------")