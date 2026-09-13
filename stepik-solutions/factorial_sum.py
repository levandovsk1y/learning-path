n = int(input())
s = 0
product = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        product *= j
    s += product
    product = 1
print(s)