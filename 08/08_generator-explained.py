#JAK DZIAŁA GENERATOR - WYTŁUMACZONE NA PRZYKŁADZIE

#jakiś generator dla kolejnych liczb całkowitych
def gen_numbers():
    num = 0
    while True:
        num += 1
        yield num

# hmmm generator ciągle od nowa - doesn't make snese
print(next(gen_numbers()))
print(next(gen_numbers()))
print(next(gen_numbers()))
print(next(gen_numbers()))
print(next(gen_numbers())) # nadal 1

print("~~~~~~~~~generator~~~~~~~~~~~~~~")
# utworzenie genertora
natural_numbers = gen_numbers()
# wraz z kolejnym wyświetleniem uruchomiam generator 
# (ale poprzednie uruchomienie "zostaje w pamięci" generatora dzięki zmiennej),
# dlatego ruszamy od poprzedniego zatrzymania się generatora a nie ciągle od nowa
print(next(natural_numbers))
print(next(natural_numbers))
print(next(natural_numbers))
print(next(natural_numbers))
print(next(natural_numbers)) # 5

print("**********a tu w pętli*************")

# wersja w pętli
loop_numbers = gen_numbers()
for n in range(5):
  print(next(loop_numbers))
