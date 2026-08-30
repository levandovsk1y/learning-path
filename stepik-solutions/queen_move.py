x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x1 == x2 and y1 == y2:  # standing
    print("NO")
elif (
    (x1 == x2 and y1 != y2)
    or (y1 == y2 and x1 != x2)
    or (x2 - x1 == y2 - y1)
    or (x2 - x1 == -(y2 - y1))
):  # move vertically, horizontally, or diagonally
    print("YES")
else:
    print("NO")
