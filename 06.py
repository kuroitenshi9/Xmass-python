import random

def user_input():
    user_numbers = input("Please provide 6 numbers: ").split(',')
    user_numbers = [int(x) for x in user_numbers]
    return user_numbers

def loteria():
    #zmienne
    your_numbers = user_input()
    numbers = []
    win = 0
    stopien_wygranej = 0
    kwota = 0
    
    #komputer losuje zmienne
    while len(numbers) < 6:
        a = random.randint(1, 50)
        if a not in numbers:
            numbers.append(a)
    
    #sprawdzam czy jest wygrana
    for number in your_numbers:
        for number1 in numbers:
            if number == number1:
                win =+ 1       
    if win == 3:
        kwota = 10
        stopien_wygranej = 4
    elif win == 4:
        kwota = 100
        stopien_wygranej = 3
    elif win == 5:
        kwota = 3500
        stopien_wygranej = 2
    elif win == 6:
        kwota = 1000000
        stopien_wygranej = 1
    print(numbers, your_numbers, win)

    if win < 3:
        return "Sorry no win"
    else:
        return f"Wygrałeś nagrodę {stopien_wygranej} stopnia. Kwota wygranej wynosi: {kwota}"


if __name__ == '__main__':
    print(loteria())
