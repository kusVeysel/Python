
#? global/local variables

text = "metin" # bu bir global değişkendir

def myFunction():
    a = 18 # bu bir local değişkendir
    #! global kelimesi ile local değişken globale çevrilebilir
    global b
    b = 1
    print("bu bir",text)

myFunction()
print(text)
print(b) # b değişkeni global hale çevrildiği için dışarıdan erişilebildi


#? Veri Tipler

name = "String" #* string
age = 24 #* integer
weight = 84.15 #* float
comp = 2j #* complex
myList = ["Apple","Grape","Cherry","Matermelon","Lemon","Banana"] #* list 
myTuple = ("Red","Blue","White","Black","Pink","Grey") #* tuple
myRange = range(7)  #* 0'dan, girilen sayının 1 eksiğine kadar olan sayıları yazar
myDict = {"name":"Veysel", "age":18} #* dictionary
mySet = {"name","age","surname"} #* set
myFrozen = frozenset({"name","age","surname"}) #* frozenset
mybool = True #* bool
x = None #* NoneType: Null'dan farkı yok


#? E kullanımı
#* float sayılar destekler

x = 2e4 # E-e fark etmez
print(x)
