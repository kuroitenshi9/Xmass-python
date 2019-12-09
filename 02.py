'''
Day2: Anagram
Napisz funkcję is_anagram(), która zwraca prawdę, 
gdy dwa napisy podane jako dwa argumenty funkcji mają taką własność, 
że da się z liter pierwszego napisu ułożyć drugi napis.
'''

def is_anagram(txt1, txt2):
    if sorted(txt1.lower().replace(" ", "")) == sorted(txt2.lower().replace(" ", "")):
        print(f'{txt1} and {txt2} are anagrams')
    else:
        print(f"{txt1} and {txt2} are not anagrams")

one =  "I am Lord Voldemort"s
two = "Tom Marvolo Riddle"

is_anagram(one, two)