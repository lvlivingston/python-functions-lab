# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
def sum_to(n):
    return sum(range(1, n+1))

print( sum_to(6) )
print( sum_to(10) )



# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
def largest(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print( largest([1, 3, 7, 231, 305, 10, 8]))
print( largest([1, 3, 7, 3, 4, 10, 8]))



# Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
def occurrences(a, b):
    total = 0
    start = 0
    while start < len(a):
        index = a.find(b, start)
        if index == -1:
            break
        total += 1
        start = index +1
    return total

print ( occurrences('Jan', 'a') )
print ( occurrences('fleep floop', 'e') )




# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print( product(1, -4))
print( product(10, 10))
print( product(0, 10))
print( product(2, 3))




# Write a function named steps_to_zero that accepts a non-negative integer as an argument, and returns the number of steps it took to reduce the integer to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
def steps_to_zero(num):
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        steps += 1
    return steps

print( steps_to_zero(14))
    