'''
W ramach ćwiczenia można sobie przypomnieć 
ciąg fibonacciego iteracyjnie i spróbować 
napisać generator (to naprawdę nic trudnego)
'''


#normal function
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
         return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#one solution
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

#second solution
def gen_fib():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b


g = gen_fib()
fibs = [next(g) for _ in range(10)] 

if __name__ == "__main__":
    a = int(input('Give amount: '))
    print(list(fib(a)))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(fibs)


