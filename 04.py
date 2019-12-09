'''
Odczytaj zawartość pliku do słownika

Twój słownik po odczytaniu pliku będzie zawierał strukturę:
some_logs = {a
    20: 'ERROR',
    33: 'WARNING',
    59: 'WARNING4',
    74: 'ERROR',
    99: 'ERROR',
    81: 'WARNING',
    62: 'INFO',
    84: 'ERROR',
    36: 'WARNING',
    46: 'WARNING2',
    85: 'ERROR',
    64: 'INFO',
    71: 'ERROR1',
    7: 'ERROR',
    37: 'INFO4',
    90: 'INFO',
    13: 'INFO',
    93: 'INFO',
    68: 'ERROR',
    47: 'WARNING'
}

O pliku The first value is the timestamp, 
while the second value is the type of log that was registered in the system at a given time.

Napisz funkcję, która wyświetla wszystkie rodzaje zdarzeń / logów, 
które pojawiły się w danym przedziale czasowym.

Na potrzeby zadania timestampy zostały zamienione na zwykłe int, wy pewnie byście sobie poradziły, 
ale niech zostanie na intach - czyli zamiast interwałów czasowych do funkcji podaje się liczbę start i koniec
def get_logs (start_interv, end_interv, dict):
    pass

Czyli jak użytkownik poda 
od 10 do 20
wykona się coś takiego:
print(get_logs(10, 20, słownik_z_logami))

=> 'INFO', 'ERROR'
'''

with open('logs.csv', 'r') as fopen:
    lines = fopen.readlines()
for l in lines:
  if l != '': 
    l = l.rstrip()
    l = l.split(",")

some_logs = {}
for l in lines:
  if l != '':
    l = l.split(",")
    key = l[0]
    value = l[1]
    some_logs[key] = value

print(some_logs)

def get_logs(start_interv, end_interv, dict):
    for key, value in dict.items():
        if int(key) >= start_interv and int(key) <= end_interv:
            print(f"The log in timeline {start_interv} - {end_interv}: ", value)
        else:
            pass

get_logs(10, 20, some_logs)