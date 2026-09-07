 #* Girilen 4 basamaklı bir sayının yazıya çevrilmesi

def number_to_words(number):
    ones = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
    tens = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
    if not(1000 <= number <= 9999):
        return "4 basamaklı sayı giriniz!"

    one_digit = number % 10
    ten_digit = (number // 10) % 10
    hundred_digit = (number // 100) % 10
    thousand_digit = number // 1000

    result = ""
    if(thousand_digit>0):
        if(thousand_digit>1):
            result += f"{ones[thousand_digit]} bin "
        else:
            result += "bin "
    if(hundred_digit>0):
        if(hundred_digit>1):
            result += f"{ones[hundred_digit]} yüz "
        else:
            result += "yüz "
    if(ten_digit>0):
        result += f"{tens[ten_digit]} "
    if(one_digit>0):
        result += f"{ones[one_digit]} "

    return result.strip()

number = int(input("4 basamaklı bir sayı giriniz:"))

print(number_to_words(number))