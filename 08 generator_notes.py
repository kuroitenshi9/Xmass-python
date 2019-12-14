def square_numbers(numbs):
    result = []
    for i in numbs:
        result.append(i*i)
    return result

def square_numbers_generator(numbs):
    for i in numbs:
       yield (i*i)


my_nums = [1,2,3,4,5]
print(square_numbers(my_nums))
print(square_numbers_generator(my_nums))
print(next(square_numbers_generator(my_nums)))
