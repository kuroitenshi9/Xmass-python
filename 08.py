'''
W ramach ćwiczenia można sobie przypomnieć 
ciąg fibonacciego iteracyjnie i spróbować 
napisać generator (to naprawdę nic trudnego)

a teraz już zadanie na dzisiaj:

Poniższy kod jest generatorem ciągu liczb naturalnych. 
Napisz nowy generator, który będzie zwracał listę N 
kolejnych elementów z tego ciągu.
def gen_numbers():
    num = 0
    while True:
        num += 1
        yield num
Generator zwraca 1,2,3,4,5,6,7,8 ...
Nowy generator ma dla N=2 zwrócić
[1,2], [3,4], [5,6], [7,8] �a dla N=4 
[1,2,3,4], [5,6,7,8] itd.
'''

# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#          return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

def fibonacci(some_list):
    for n in some_list:
        for n in [0,1]:
            yield(n)
    else:
        yield(fibonacci(n-1) + fibonacci(n-2))

if __name__ == "__main__":
    # print(fibonacci(0)
    # print(fibonacci(1))
    # print(fibonacci(2))
    numbers = [0,1,2,3,4,5,6,7]

    print(next(fibonacci(numbers)))
    print(next(fibonacci(numbers)))


