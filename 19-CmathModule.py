import cmath
#? Karmaşık sayılar üzerinde matematiksel işlemler

print("-----Sabitler-----")
print("cmath.e =>",cmath.e)
print("cmath.inf =>",cmath.inf)
print("-cmath.inf =>",-cmath.inf)
print("cmath.infj =>",cmath.infj)
print("cmath.nan =>",cmath.nan)
print("cmath.nanj =>",cmath.nanj)
print("cmath.tau =>",cmath.tau)

print("cmath.sqrt(-1) =>",cmath.sqrt(-1)) #* karakökü alır
print("cmath.sqrt(4+3j) =>",cmath.sqrt(4+3j)) #* karakökü alır


#? Açılar
print("-----Açılar-----")
print("math.acos(2+3j) =>",cmath.acos(2+3j))
print("math.acosh(2+3j) =>",cmath.acosh(2+3j))
print("math.asin(2+3j =>",cmath.asin(2+3j))
print("math.asinh(2+3j) =>",cmath.asinh(2+3j))
print("math.atan(2+3j) =>",cmath.atan(2+3j))
print("math.atanh(2+3j) =>",cmath.atanh(2+3j))

#? 
print()
print("cmath.exp(2+3j) =>",cmath.exp(2+3j))
print("cmath.isfinite(2+3j) =>",cmath.isfinite(2+3j))
print("cmath.isinf(2+3j) =>",cmath.isinf(2+3j))
print("cmath.isnan(2+3j) =>",cmath.isnan(2+3j))

#?
print()
print("cmath.isclose(10+7j,10+7j,abs_tol=0.005) =>",cmath.isclose(10+7j,10+7j,abs_tol=0.005))
print("cmath.phase(2+3j) =>",cmath.phase(2+3j))
print("cmath.atan(3/2) =>",cmath.atan(3/2)) #* gerçek sayı girdisi için sonucu verir; üstteki karmaşık girdiden farklıdır
print("cmath.polar(2+3j) =>",cmath.polar(2+3j)) #* 2.değeri yukarıdaki ile aynı
print("cmath.rect(3.163326435434,1.249045637405) =>",cmath.rect(3.163326435434,1.249045637405))
print("cmath.log(1+1j) =>",cmath.log(1+1j))
print("cmath.log10(1+1j) =>",cmath.log10(1+1j))

