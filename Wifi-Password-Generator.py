import random
import re
from string import digits,ascii_letters
from random import SystemRandom

# Karakter seti: rakamlar ve büyük/küçük harfler
symbols=digits+ascii_letters

#12 basamaklı wifi şifre oluşturucu
wifi_password="".join(SystemRandom().choice(symbols) for i in range(12))
print(f"Oluşturulan wifi şifresi:{wifi_password}")

def check_password(wifi_password):
    if len(wifi_password)<12:
        raise Exception("parola en az 12 karakter olmalıdır.")
    elif not re.search("[a-z]",wifi_password):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]",wifi_password):
        raise Exception("parola büyük harf içermelidir.")
    elif not re.search("[0-9]",wifi_password):
        raise Exception("parola rakam içermelidir.")
    elif re.search("\s",wifi_password):
        raise Exception("parola boşuluk içermemelidir.")
    else:
        print("parola oluşturuldu.")

try:
    check_password(wifi_password)
except Exception as ex:
    print(f"Hata:{ex}")

