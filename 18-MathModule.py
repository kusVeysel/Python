 #? Math Module
#* math modülü matematiksel sabitleri ve fonksiyonları içerir.

import math

#? Sabitler
print("-----Sabitler-----")
print(f"math.e → {math.e}")
print(f"math.inf → {math.inf}")
print(f"-math.inf → {-math.inf}")
print(f"math.nan → {math.nan}")
print(f"math.pi → {math.pi}")
print(f"math.tau → {math.tau}")
print("------------------------------------------")

#? Trigonometrik ve hiperbolik fonksiyonlar
print("-----Açılar ve Trigonometri-----")
print(f"math.sin(math.pi / 2) → {math.sin(math.pi / 2)}")
print(f"math.asin(0.55) → {math.asin(0.55)}")
print(f"math.sinh(1) → {math.sinh(1)}")
print(f"math.asinh(7) → {math.asinh(7)}")

print(f"math.cos(math.pi) → {math.cos(math.pi)}")
print(f"math.acos(0.55) → {math.acos(0.55)}")
print(f"math.cosh(1) → {math.cosh(1)}")
print(f"math.acosh(7) → {math.acosh(7)}")

print(f"math.tan(math.pi / 4) → {math.tan(math.pi / 4)}")
print(f"math.atan(0.4) → {math.atan(0.4)}")
print(f"math.tanh(1) → {math.tanh(1)}")
print(f"math.atanh(0.59) → {math.atanh(0.59)}")
print(f"math.atan2(8, 5) → {math.atan2(8, 5)}")

print(f"math.degrees(8.9) → {math.degrees(8.9)}") #* radyanı dereceye çevirir
print(f"math.radians(180) → {math.radians(180)}") #* dereceyi radyana çevirir
print("------------------------------------------")

#? Yuvarlama ve sayı biçimlendirme
print("-----Yuvarlama ve Sayı İşlemleri-----")
print(f"math.ceil(1.1) → {math.ceil(1.1)}") #* yukarı yuvarlar
print(f"math.floor(1.9) → {math.floor(1.9)}") #* aşağı yuvarlar

print(f"math.trunc(45.7438057) → {math.trunc(45.7438057)}") #* ondalık kısmı atar
print(f"math.fabs(-7) → {math.fabs(-7)}") #* mutlak değeri float olarak verir
print(f"math.copysign(7, -19) → {math.copysign(7, -19)}") #* ilk sayıya ikinci sayının işaretini verir
print(f"math.fmod(19, 4) → {math.fmod(19, 4)}") #* float kalanını verir
print(f"math.remainder(19, 4) → {math.remainder(19, 4)}") #* en yakın tam sayı katına göre kalanı verir
print(f"math.modf(10.5) → {math.modf(10.5)}") #* ondalıklı ve tam kısmı ayırır
print(f"math.frexp(19) → {math.frexp(19)}") #* sayıyı katsayı ve 2 üssü olarak ayırır
print(f"math.ldexp(10, 2) → {math.ldexp(10, 2)}") #* x * 2**i işlemini yapar
print(f"math.nextafter(1, 2) → {math.nextafter(1, 2)}") #* hedefe doğru bir sonraki float değerini verir
print(f"math.ulp(1) → {math.ulp(1)}") #* bir sonraki float değeriyle arasındaki farkı verir
print("------------------------------------------")

#? Kök, kuvvet ve logaritma
print("-----Kök, Kuvvet ve Logaritma-----")
print(f"math.cbrt(27) → {math.cbrt(27)}") #* küp kökü alır
print(f"math.sqrt(10) → {math.sqrt(10)}") #* karekökü alır
print(f"math.isqrt(10) → {math.isqrt(10)}") #* tam sayı karekökünü aşağı yuvarlar

print(f"math.pow(10, 2) → {math.pow(10, 2)}") #* kuvvet alır ve float döndürür

print(f"math.exp(1) → {math.exp(1)}") #* e üzeri x işlemini yapar
print(f"math.exp2(3) → {math.exp2(3)}") #* 2 üzeri x işlemini yapar
print(f"math.expm1(1) → {math.expm1(1)}") #* exp(x) - 1 işlemini hassas hesaplar

print(f"math.log(16, 2) → {math.log(16, 2)}") #* verilen tabanda logaritma alır
print(f"math.log10(100) → {math.log10(100)}") #* 10 tabanında logaritma alır
print(f"math.log1p(100) → {math.log1p(100)}") #* log(1 + x) işlemini hassas hesaplar
print(f"math.log2(100) → {math.log2(100)}") #* 2 tabanında logaritma alır
print("------------------------------------------")

#? Kombinasyon, permütasyon ve sayı dizileri
print("-----Kombinasyon, Permütasyon ve Diziler-----")
print(f"math.comb(7, 4) → {math.comb(7, 4)}") #* kombinasyon hesaplar
print(f"math.perm(10, 5) → {math.perm(10, 5)}") #* permütasyon hesaplar
print(f"math.factorial(7) → {math.factorial(7)}") #* faktöriyel hesaplar
print(f"math.gcd(19, 4) → {math.gcd(19, 4)}") #* en büyük ortak böleni verir
print(f"math.lcm(19, 4) → {math.lcm(19, 4)}") #* en küçük ortak katı verir
print(f"math.prod([2, 3, 4]) → {math.prod([2, 3, 4])}") #* listedeki elemanları çarpar
print(f"math.fsum([0.1, 0.2, 0.3]) → {math.fsum([0.1, 0.2, 0.3])}") #* hassas float toplamı alır
print(f"math.sumprod([1, 2, 3], [4, 5, 6]) → {math.sumprod([1, 2, 3], [4, 5, 6]) if hasattr(math, 'sumprod') else 'Python 3.12+'}")
print("------------------------------------------")

#? Uzaklık ve özel fonksiyonlar
print("-----Uzaklık, Özel Fonksiyonlar ve Kontroller-----")
p = [3, 3]
q = [6, 7]
print(f"math.dist(p, q) → {math.dist(p, q)}") #* iki nokta arasındaki mesafeyi hesaplar
print(f"math.hypot(3, 4) → {math.hypot(3, 4)}") #* dik üçgende hipotenüsü hesaplar
print(f"math.erf(0.7) → {math.erf(0.7)}") #* hata fonksiyonunu hesaplar
print(f"math.erfc(0.7) → {math.erfc(0.7)}") #* tamamlayıcı hata fonksiyonunu hesaplar
print(f"math.gamma(7) → {math.gamma(7)}") #* gamma fonksiyonunu hesaplar
print(f"math.lgamma(7) → {math.lgamma(7)}") #* gamma fonksiyonunun mutlak logaritmasını hesaplar
print(f"math.isclose(0.1 + 0.2, 0.3) → {math.isclose(0.1 + 0.2, 0.3)}") #* iki sayının yakınlığını kontrol eder
print(f"math.isfinite(7) → {math.isfinite(7)}") #* sonlu olup olmadığını kontrol eder
print(f"math.isinf(7) → {math.isinf(7)}") #* sonsuz olup olmadığını kontrol eder
print(f"math.isnan(7) → {math.isnan(7)}") #* NaN olup olmadığını kontrol eder
