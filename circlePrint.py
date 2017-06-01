def genArray(m, n):
    a = []
    count = 1
    for i in range(m):
        b = []
        for j in range(n):
            b.append(count)
            count += 1
        a.append(b)
    print a
    return a
def circleCount(a):
    rows = len(a)
    cols = len(a[0])
    # print rows
    # print cols
    x = 0
    y = 0
    left = 0
    right = cols
    top = 0
    down = rows
    while True:
        #print (left, right, top, down)
        for i in range(right - left):
            print a[x][y]
            y += 1
        top += 1
        if top == down:
            break
        y -= 1
        x += 1
        for i in range(down - top):
            print a[x][y]
            x += 1
        right -= 1
        if right == left:
            break
        x -= 1
        y -= 1
        for i in range(right - left):
            print a[x][y]
            y -= 1
        down -= 1
        if top == down:
            break
        y += 1
        x -= 1

        for i in range(down - top):
            print a[x][y]
            x -= 1
        left += 1
        if right == left:
            break
        x += 1
        y += 1
a = genArray(3, 5)
circleCount(a)
