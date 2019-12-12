# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words 
# in given set of strings and number of times they occured, case insensitive
# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2
# Good luck! You can write all the code in this file.

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopi',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

def most_repeated(list):
    my_list= {}
    for strings in list:
        ssplit = strings.split()
        for word in ssplit:
            if word in my_list: 
                my_list[word] += 1
            else:
                 my_list[word] = 1
    top3 = {k: my_list[k] for k in sorted(my_list, key=my_list.get, reverse=True)[:3]}
    return f"Three most repeated words are {top3}" 
  
if __name__ == '__main__':
  print(most_repeated(sentences))