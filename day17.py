#sum any given number for arguments using arbitrary arguments
def sum_all(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_all(2, 5, 9))  
print(sum_all(3, 14, 56, 67, 89))  