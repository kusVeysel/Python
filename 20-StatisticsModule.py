 #? Statistics Module

#* statistics modülü sayısal veriler üzerinde istatistiksel hesaplamalar yapar.

import statistics

data = [1, 2, 3, 4, 4, 5, 6, 7, 8]
sample = [2, 4, 6, 8, 10]

#? Ortalama ve merkezî eğilim ölçüleri
print("-----Ortalama ve Merkezî Eğilim-----")
print(f"statistics.mean(data) → {statistics.mean(data)}") #* aritmetik ortalamayı bulur
print(f"statistics.fmean(data) → {statistics.fmean(data)}") #* float olarak aritmetik ortalamayı bulur
print(f"statistics.geometric_mean(data) → {statistics.geometric_mean(data)}") #* geometrik ortalamayı bulur
print(f"statistics.harmonic_mean(data) → {statistics.harmonic_mean(data)}") #* harmonik ortalamayı bulur
print(f"statistics.median(data) → {statistics.median(data)}") #* ortanca değeri bulur
print(f"statistics.median_low(data) → {statistics.median_low(data)}") #* iki orta değerden küçüğünü seçer
print(f"statistics.median_high(data) → {statistics.median_high(data)}") #* iki orta değerden büyüğünü seçer
print(f"statistics.median_grouped(data) → {statistics.median_grouped(data)}") #* gruplanmış ortancayı bulur
print(f"statistics.mode(data) → {statistics.mode(data)}") #* en sık tekrar eden değeri verir
print(f"statistics.multimode(data) → {statistics.multimode(data)}") #* eşit sıklıktaki tüm modları verir
print("------------------------------------------")

#? Yayılım ölçüleri
print("-----Varyans ve Standart Sapma-----")
print(f"statistics.pvariance(data) → {statistics.pvariance(data)}") #* anakütle varyansını bulur
print(f"statistics.variance(sample) → {statistics.variance(sample)}") #* örneklem varyansını bulur
print(f"statistics.pstdev(data) → {statistics.pstdev(data)}") #* anakütle standart sapmasını bulur
print(f"statistics.stdev(sample) → {statistics.stdev(sample)}") #* örneklem standart sapmasını bulur
print("------------------------------------------")

#? Veri sıralama ve yüzdelikler
print("-----Sıralama ve Yüzdelikler-----")
print(f"statistics.quantiles(data, n=4) → {statistics.quantiles(data, n=4)}") #* çeyreklik değerleri verir
print(f"statistics.quantiles(data, n=4, method='inclusive') → {statistics.quantiles(data, n=4, method='inclusive')}")
print("------------------------------------------")

#? İki veri kümesinin ilişkisi
print("-----İlişki ve Regresyon-----")
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 8, 10]
print(f"statistics.covariance(x, y) → {statistics.covariance(x, y)}") #* kovaryansı bulur
print(f"statistics.correlation(x, y) → {statistics.correlation(x, y)}") #* korelasyon katsayısını bulur
regression = statistics.linear_regression(x, y)
print(f"statistics.linear_regression(x, y) → {regression}") #* doğrusal regresyon eğimini ve kesişimini verir
print("------------------------------------------")

#? Normal dağılım
print("-----Normal Dağılım-----")
normal = statistics.NormalDist(mu=100, sigma=15)
print(f"normal.mean → {normal.mean}")
print(f"normal.stdev → {normal.stdev}")
print(f"normal.pdf(100) → {normal.pdf(100)}") #* olasılık yoğunluk fonksiyonunu verir
print(f"normal.cdf(100) → {normal.cdf(100)}") #* kümülatif dağılım fonksiyonunu verir
print(f"normal.inv_cdf(0.5) → {normal.inv_cdf(0.5)}") #* yüzdelik değerini tersine çevirir
print(f"normal.overlap(statistics.NormalDist(110, 15)) → {normal.overlap(statistics.NormalDist(110, 15))}")
print("------------------------------------------")
