def perimeter(n):
    sum = 0
    for i in range(n+2):
        sum += fib_recursive(i+1)
    return sum*4

def fib_recursive(n):
    if(n<=0):
        return 0
    elif(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

#https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series
def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print(perimeter(5))
print(perimeter(7))
print(perimeter(20))
print(perimeter(30))
print(perimeter(100))