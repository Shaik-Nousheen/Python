n = int(input("enter the number: "))
count = 0
sum = 0
x = n
y = n


while  n > 0:

    r = n % 10
    # print(c)
    count += 1
    n = n // 10



while x > 0:
    r = x % 10
    sum = sum +  (r ** count)
    x = x // 10
if sum == y:
    print(y, "is armstrong number")
else:
    print(y, "is not a armstrong number")