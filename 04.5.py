"""
Day 04
Przesyłam wersję "pełną" wczorajszego zadnia

Dany jest słownik logów jakiegoś programu. Kluczem jest - timestamp (czas wystąpienia), a wartością rodzaj loga. Waszym zadaniem jest stworzyć funkcję, która dla zadanego interwału zwraca jakiego rodzaju logi w tym czasie wystąpiły (unikalne nazwy typów loga)

def get_logs (start_interv, end_interv, some_logs):
    pass

w załączniku lista logów



logs_timestamp.csv

Przykładowy słownik logów:

some_logs = {
    1564517408: 'ERROR',
    1562514432: 'WARNING',
    1564015907: 'WARNING4',
    1563822588: 'ERROR',
    1563125949: 'ERROR',
    1564225949: 'WARNING',
    1562491290: 'INFO',
    1563184020: 'ERROR',
    1562956120: 'WARNING',
    1564477808: 'WARNING2',
    1564421475: 'ERROR',
    1562764321: 'INFO',
    1562709301: 'ERROR1',
    1563900303: 'ERROR',
    1564125540: 'INFO4',
    1564010897: 'INFO',
    1564279899: 'INFO',
    1564456120: 'INFO',
    1564452850: 'ERROR',
    1564528675: 'WARNING'
}




Ponieważ są to timestampy - czyli punkty czasowe możemy założyć, że użytkownik będzie podawał zakres czasowy w bardziej ludzkim formacie, jakim to już wasza decyzja 😛 
żeby wyjaśnić tutaj przykład odpakowania timestampu do formatu czasu https://repl.it/repls/HardtofindRoundSquares
jeśli użytkownik podaje czas to raczej będzie do podawał w jakimś ludzkim formacie a nie timestampie, przy czym jeśli rozwiązałyście zadanie z intami, to funkcja nie powinna się tak naprawdę zmienić 🙂 
Jedynie jest potrzebne pobranie czasu od użytkownika w odpowiednim formacie i konwersja do timestamp
"""

from datetime import datetime

def get_logs(start_interv, end_interv, dict):
    looking_logs = []
    start_interv = datetime.strptime(start_interv, "%d-%m-%Y")
    end_interv = datetime.strptime(end_interv,"%d-%m-%Y")
    start_interv = datetime.timestamp(start_interv)
    end_interv = datetime.timestamp(end_interv)
    for key, value in dict.items():
        if int(key) > start_interv and int(key) < end_interv:
            looking_logs.append(value)
        else:
            pass
    if len(looking_logs) > 0:
        return print(f"The log in the timeline {start_interv} - {end_interv}: ", looking_logs)
    else:
        return print(f"Sorry, no logs found in the timeline {start_interv} - {end_interv}")


with open('logs_timestamp.csv', 'r') as fopen:
    lines = fopen.readlines()
for l in range(len(lines)):
	lines[l] = lines[l].strip()

some_logs = {}
for l in lines:
    if l != '':
        l = l.split(",")
        key = l[0]
        value = l[1]
        some_logs[key] = value

# print(some_logs)

get_logs('01-01-2019', '03-12-2019', some_logs)

# def main():
#     start_interv = str(input("Give start date in format dd-mm-yyyy: "))
#     end_interv = str(input("Give end date in format dd-mm-yyyy: "))
#     print(get_logs(start_interv, end_interv, some_logs))

# if __name__ == '__main__':
#   main()