# baklava dilimi 
print("Baklava dilimi\n")
satir =int(input("Satır sayısı giriniz :"))
for i in range(satir):
    for j in range((satir)-i):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    print()
for i in range(satir,0,-1):
    for l in range((satir)-i):
        print(" ",end="")
    for m in range(i*2-1):
        print("*",end="")
    print()

print("\n\n\n")

print("Piramit şekli\n")
#piramit
satir=9
for i in range(satir):
    print(' '*(satir-i-1) + '*'*(2*i+1))

print("\n\n\n")

print("Dik üçgen şekli\n")
#dik üçgen
for i in range(0,5):
    for j in range(0,4):
      print(end = " ")
    k -= 1
    for j in range (0, i+1):
      print("* ", end='')
    print() 

print("\n\n\n")

print("Ters dik üçgen şekli\n")
#ters dik üçgen 
satir = 5
for i in range(satir,0,-1):
    print( " "*(satir-i) + "*"*(i))