'''
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

def gen_numbers():
    num = 0
    while True:
        num += 1
        yield num

# def gen_numbers_list(n):
#     nums = gen_numbers()
#     list_nums = []
#     while True:
#         for _ in range(n):
#             list_nums.append(next(nums))
#         yield list_nums
#         list_nums.clear()

def gen_list(N):
    nums = gen_numbers()
    nums_list = []
    while True:
       for _ in range(N):
            nums_list.append(next(nums))
    yield nums_list
    nums_list.clear()

if __name__ == "__main__":
    test1 = gen_list(2)
    print(next(test1))
    print(next(test1))
    test2 = gen_list(4)
    print(next(test2))
    print(next(test2))

