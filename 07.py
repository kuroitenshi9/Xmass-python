"""
Dzień 8

Dla tablicy liczb całkowitych, chcemy, 
aby liczby całkowite parzyste poprzedzały nieparzyste w tablicy

Przykładowa tablica:
numbers = [7,7,4,0,9,8,2,4,1,9]

***Optymalizacja:
Operate on the array in-place, with a constant amount of extra space. 
The answer should scale linearly in time with respect to the size of the array.
"""

def sort_odds2even(lista):
    even = []
    odd = []
    for i in lista:
        if (i % 2) == 0:
            even.append(i)
        else:
            odd.append(i)
    sorted_list = even + odd
    return print(sorted_list)

def main():
    numbers = [7,7,4,0,9,8,2,4,1,9]
    sort_odds2even(numbers)

if __name__ == '__main__':
    main()
