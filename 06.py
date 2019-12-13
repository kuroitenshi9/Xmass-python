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
