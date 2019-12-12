'''
Day 03

Napisz funkcję, która jako parametr przyjmuje listę liczb całkowitych. Funkcja zwraca tę liczbę, 
która pojawia się w tej liście najczęściej. Jeśli mamy remis, zwróć którąkolwiek z tych liczb.


Ważna uwaga - żeby nie używać gotowych metod listy np. do sortowania, 
można sobie to zrobić jako wersję dodatkową (wtedy będzie ładne króciutkie). 
Można za to korzystać z wszystkich struktur danych jak słowniki.


Day 03. Rozszerzenie
Z modyfikuj funkcje example_function(examole_list) opcjonalny parametr rev (reversed). 
Jeżeli rev=True funkcja ma zadziałać odwrotnie, zwrócić element, o najmniejszej liczbie wystąpień
'''

lista = [1, 2, 3, 4, 4, 4, 5, 5, 9, 7, 7, 7]
def mode(list, rev = False):
    frequency_dic = {}
    for number in list:
        if number in frequency_dic : 
             frequency_dic[number] += 1
        else:
            frequency_dic[number] = 1
    if rev == True:
        return  min(frequency_dic, key=frequency_dic.get)
    else:
        return  max(frequency_dic, key=frequency_dic.get)

if __name__ == '__main__':
    print(mode(lista))
    print(mode(lista, True))
