name = "Yusuf"
SURNAME = "Doğrusoy"
age ="21"

print(name + " " + SURNAME + " " + age)

text = "name: {}, surname: {}, age: {}"
text ="Benim adım " + name + " ve soyadım " + SURNAME + " yaşım ise " + age +"."

#print(text)
print(text[1]) #e
print(text[-1]) # .
print(text[0:5]) #Benim
print((text[6:17]))
print(text[:10]) #başlangıcı belirtmeden bitişe kadar
print(text[10:]) #bitişi belirtmeden başlangıçtan itibaren

print(text[-20:-1])
print(text[0:30:2]) #2şer 2şer atlayarak yazdırır

print(text[::2]) #tersten yazdırır
print(text[::-1]) #tersten yazdırır

