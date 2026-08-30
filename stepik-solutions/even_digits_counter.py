n = int(input())
length = len(str(n))
count = 0
for i in range(1, length + 1):
    d = n // 10 ** (length - i) % 10
    if d % 2 == 0:
        count += 1
        print(count, "-th even digit is ", d, sep="")
if count == 0:
    print("There are no even digits in the number")
