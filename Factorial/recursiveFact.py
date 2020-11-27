def Fact(n):
    if n == 0 or n == 1:
        return 1
    
    return n * Fact(n-1)

num = int(input())
print('Factorial of number {} is {}'.format(num,Fact(num)))
