import random

def guess(num):
    randomNum = random.randint(1,num)
    count = 1
    guess = int(input(f'1 ile {num} arasinda bir sayi tahmininde bulunun.'))
    
    while randomNum != guess:
        count += 1
        if guess < randomNum:
            print("Üzgünüm yanliş tahmin lütfen daha büyük bir sayi tahmin edin!")
        else:
            print("Üzgünüm, yanlis tahmin lütfen daha küçük bir sayi tahmininde bulunun.") 
        
        guess = int(input("Lütfen tekrardan sayi tahmininde bulunun: "))
    
    print(f'Tebrikler! {count}. tahminde doğru sayiyi bulabildin.')
guess(10)