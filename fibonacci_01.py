def recursive_fibonacci(n):
    if n <=1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def non_recursive_fibonacci(n):
    first = 0
    second = 1
    print(first)
    if n > 1:
        print(second)
    
    while n - 2 > 0:
        third = first + second
        first = second
        second = third
        print(third)
        n -= 1

num = int(input("Enter the number of terms: "))

print("\nFibonacci series using recursion:")

for i in range(num):
        print(recursive_fibonacci(i))

print("\nFibonacci series using non-recursion:")
non_recursive_fibonacci(num)