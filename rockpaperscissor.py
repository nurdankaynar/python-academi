import random

computerChoice = random.choice(['tas', 'kagit', 'makas'])



player_score, computer_score = 0, 0

while True:

    userChoice = input('\nTaş,kağit ve makastan birini seç. Eğer oyundan çikmak istersen "q" harfine basman yeterli. İyi şanslar.?\n')
    
    if userChoice == 'q':
        break

    print('Computer: ' + str(computerChoice) + '\nYou: ' + str(userChoice))

    if computerChoice == userChoice:
        print('\nBerabere')
    elif userChoice == 'tas' and computerChoice == 'makas':
        print('\nTebrikler, sen kazandin :)')
        player_score += 5
    elif computerChoice == 'kagit' and userChoice == 'makas':
        print('\nTebrikler, sen kazandin :)')
        player_score += 5
    elif userChoice == 'kagit' and computerChoice == 'tas':
        print('\nTebrikler, sen kazandin :)')
        player_score += 5
    else:
        print('\nÜzgünüm bilgisayar kazandi.')
        computer_score += 5

print(f"Oyuncunun puani: {player_score}\nBilgisayarin puani: {computer_score}")
