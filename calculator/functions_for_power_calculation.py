import math

def find_sqrt(num):
    val = int(num[0]) if '.' not in num[0] else float(num[0])
    if val < 0:
        return "Maths Error: Do not calculate Square root of negative no."
    else:
        x = math.sqrt(val)
        if int(x) == x:
            return int(x)
        else: 
            return round(x, 3)


def power(num):
    if len(num) < 2:
        return "Please input both base and power for calculation."
    x = int(num[0]) if '.' not in num[0] else float(num[0])
    n = int(num[1]) if '.' not in num[1] else float(num[1])
    if n == 0:
        return 1
    temp = x ** (n // 2)
    if n % 2 == 0:
        ans = temp * temp
        return int(ans) if int(ans) == ans else round(ans, 4)
    else:
        if n > 0:
            ans = x * temp * temp
            return int(ans) if int(ans) == ans else round(ans, 4)
        else:
            ans = (temp * temp) / x
            return int(ans) if int(ans) == ans else round(ans, 4)

def square(num):
    x = num[0]
    return power([x, '2'])

def cube(num):
    x = num[0]
    return power([x, '3'])

def cube_root(num):
    digit = int(num[0]) if '.' not in num[0] else float(num[0])
    if digit < 0:
        return "Math Error: Do not calculate cube root of negative number."
    else:
        res = math.pow(digit, 1/3)
        if int(res) == res:
            return int(res)
        else:
            return round(res, 3)
# print(cube_root(['25.5']))
