for a in range(1, 150):
    for b in range(a, 150):
        for c in range(b, 150):
            for d in range(c, 150):
                sum5 = a**5 + b**5 + c**5 + d**5
                e = int(sum5 ** 0.2)
                if e**5 == sum5:
                    print("Sum:", a + b + c + d + e)
                elif (e + 1)**5 == sum5:
                    print("Sum:", a + b + c + d + (e + 1))
print("stop")                    