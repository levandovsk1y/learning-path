x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 != x2 and y1 != y2) and (
    x2 - x1 == y2 - y1 or x2 - x1 == -(y2 - y1)
):  # Check if the move is diagonal by comparing coordinate differences
    print("YES")
else:
    print("NO")
