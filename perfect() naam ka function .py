def isPerfect( n ):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1
    return (True if sum == n and n!=1 else False)
print("Below are all perfect numbers till 1000")
n = 2
for n in range (1000):
    if isPerfect (n):
        print(n , " is a perfect number")
                     
# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n
# print(perfect_number(6))



