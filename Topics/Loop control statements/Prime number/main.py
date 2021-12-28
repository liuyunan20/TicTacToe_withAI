n = int(input())
prime = ""
if n <= 1:
    prime = "not "
else:
    for x in range(2, n):
        if n % x == 0:
            prime = "not "
            break
print(f"This number is {prime}prime")
