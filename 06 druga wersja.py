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
    stopien_wygranej = [0, 1, 2, 3, 4, 5, 6]
    kwota = [0, 0, 0, 10, 100, 3500, 1000000]

    #komputer losuje liczby
    while len(numbers) < 6:
        a = random.randint(1, 6)
        if a not in numbers:
            numbers.append(a)

    your_numbers1 = your_numbers.sort()
    numbers1 = numbers.sort()

    #sprawdzam czy jest wygrana
    for item in your_numbers1:
        for item1 in numbers1:
            if item == item1:
                win =+ 1

    print(numbers, your_numbers, win)

    if win < 3:
        return "Sorry no win"
    else:
        return f"Wygrałeś nagrodę {stopien_wygranej[win]} stopnia. Kwota wygranej wynosi: {kwota[win]}"


if __name__ == '__main__':
    print(loteria())
