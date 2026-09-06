import statistics

data = [1,6,7,8,2]

print("statistics.harmonic_mean(data) =>",statistics.harmonic_mean(data)) #* harmonic ortalamasını bulur
print("statistics.mean(data) =>",statistics.mean(data)) #* aritmetik ortalamayı bulur
print("statistics.median(data) =>",statistics.median(data)) #* ortadaki değeri bulur (sayılar karışık olsa bile kendi içinde küçükten büyüğe sıralar)
print("statistics.median_grouped(data) =>",statistics.median_grouped(data))
print("statistics.median_high(data) =>",statistics.median_high(data)) #* çift adet veri varsa, ortadaki iki sayının büyük olanını alır
print("statistics.median_low(data) =>",statistics.median_low(data)) #* çift adet veri varsa, ortadaki iki sayının küçük olanını alır
print("statistics.mode(data) =>",statistics.mode(data)) #* en çok tekrar eden veriyi getirir, tekrar eden veriler eşitse ilk gördüğü sayıyı getirir(index'i küçük olanı)
print("statistics.multimode(data) =>",statistics.multimode(data)) #* birden fazla tekrar eden veri olduğunda mod gibi ilk gördüğünü değil hepsini de getirir
print("statistics.pstdev(data) =>",statistics.pstdev(data)) #* anakütle standart sapması
print("statistics.stdev(data) =>",statistics.stdev(data)) #* örneklem standart sapması
print("statistics.pvariance(data) =>",statistics.pvariance(data)) #*standart sapmanın(pstdev) karesi
print("statistics.variance(data) =>",statistics.variance(data)) #* stdev'in karesi