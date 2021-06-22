def add(num):
    ans = 0
    for n in num:
        x = 0
        if "." in n:
            x =  float(n)
        else:
            x = int(n)
        ans += x
    return ans


def sub(num):
    ans = int(num[0]) if '.' not in num[0] else float(num[0])
    for n in range(1, len(num)):
        x = 0
        if "." in num[n]:
            x = float(num[n])
        else:
            x = int(num[n])
        ans -= x
    return round(ans, 1)

def multiply(num):
    ans = int(num[0]) if '.' not in num[0] else float(num[0])
    for n in range(1, len(num)):
        x = 0
        if "." in num[n]:
            x = float(num[n])
        else:
            x = int(num[n])
        ans *= x
    return round(ans, 1)

def divide(num):
    x = int(num[0]) if '.' not in num[0] else float(num[0])
    y = int(num[1]) if '.' not in num[0] else float(num[1])
    ans = x/y
    if int(ans) == ans:
        return int(ans)
    return round(x/y, 2)


# print(divide(['4', '2']))