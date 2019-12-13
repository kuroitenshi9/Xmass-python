import random

your_numbers = [1,2,3,4,5,6]
numbers = [1,2,3,4,5,6]

def loteria():
    #zmienne
    win = 0
    win_info = {
        6 : ["szóstego stopnia", "1000000"],
        5 : ["piątego stopnia", "3500"],
        4 : ["czwartego stopnia", "100"],
        3 : ["trzeciego stopnia", "10"]
    }    
    
    for number in your_numbers:
        for number1 in numbers:
            if number == number1:
                win =+ 1  

    if win < 3:
        return "Sorry no win"
    else:
        return f"Wygrałeś nagrodę {win_info[win][0]} stopnia. Kwota wygranej wynosi: {win_info[win][1]}"


if __name__ == '__main__':
    print(loteria())
