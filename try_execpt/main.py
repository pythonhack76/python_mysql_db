value = 10

x = -1
errore = "abbiamo un errore"

try:
    print(value)
except:
    print(errore)
#fa sempre qualcosa il finally
finally:
    print("nessun problema")


if i < 0:
    raise Exception("numero minore di zero")

print("test")

