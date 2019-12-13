"""
Dzień 7
Loteria Użytkownik, podobnie jak w klasycznym totolotku, 
podaje ciąg 6 swoich liczb w zakresie od 1 do 50. 
Komputer niezależnie losuje 6 liczb totolotka.

Wygrana zależy od tego ile liczb zostało trafionych przez użytkownika

Stopnień wygranych Trafienia Twoja wygrana

stopien wygranej	trafienia	wygrana [PLN]
1	6	1 000 000
2	5	3500
3	4	100
4	3	10
Wyświetl komunikat o wygranej np. 
"Wygrałeś nagrodę stopien_wygranej stopnia. Kwota wygranej wynosi: kwota "
"""

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
    win_info = {
        6 : ["szóstego stopnia", "1000000"],
        5 : ["piątego stopnia", "3500"],
        4 : ["czwartego stopnia", "100"],
        3 : ["trzeciego stopnia", "10"]
    }
    
    #komputer losuje zmienne
    while len(numbers) < 6:
        a = random.randint(1, 50)
        if a not in numbers:
            numbers.append(a)
    
    #sprawdzam czy jest wygrana
    win = (set(your_numbers) & set(numbers)) 
    win = len(win)
    print("Your numbers are: ", your_numbers, "and computer numbers are: ", numbers)

    if win < 3:
        return "Sorry no win"
    else:
        return f"Wygrałeś nagrodę {win_info[win][0]} stopnia. Kwota wygranej wynosi: {win_info[win][1]}"


if __name__ == '__main__':
    print(loteria())
