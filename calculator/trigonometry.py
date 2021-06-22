import math


def sin_value(num):
    val = int(num[0]) if '.' not in num[0] else float(num[0])
    return round(math.sin(math.radians(val)), 3)

def cos_value(num):
    val = int(num[0]) if '.' not in num[0] else float(num[0])
    return round( math.cos(math.radians(val)), 3)

def tan_value(num):
    val = int(num[0]) if '.' not in num[0] else float(num[0])
    return round(math.tan(math.radians(val)), 3)

def sinh_value(num):
    val = int(num[0]) if '.' not in num[0] else float(num[0])
    return round(math.sinh(math.radians(val)), 3)

def cosh_value(num):
    val = int(num[0]) if '.' not in num[0] else float(num[0])
    return round(math.cosh(math.radians(val)), 3)

def tanh_value(num):
    val = int(num[0]) if '.' not in num[0] else float(num[0])
    return round(math.tanh(math.radians(val)), 3)

def log(num):
    val = int(num[0]) if '.' not in num[0] else float(num[0])
    base = int(num[1]) if '.' not in num[0] else float(num[0])
    return round(math.log(val, base), 3)
