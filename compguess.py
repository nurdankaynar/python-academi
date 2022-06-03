import random

def compguess(min,max): # tahminde bulunulması istenilen sayı aralığı
    count = 1
    print("Aklindan bir sayi tut ve bilgisayar tahmin etmeye çalişsin.")
    
    computerNum = random.randint(min,max) 
    print(f'Aklindan tuttuğun sayi: {computerNum}')
    while True:
        result = input("Doğru ise E, yanlis ise Y harfine bas!\n")
        if result == 'E':
            break
        else:
            print("Tüh! Yanlis tahminde bulundum.")
        computerNum = random.randint(min,max)
        count += 1
        print("O zaman aklindan tuttuğun sayi ",computerNum)
         
    print(f'Harika {count}. tahminde aklindan tuttuğun sayiyi buldum. :)')

compguess(2,8) 

