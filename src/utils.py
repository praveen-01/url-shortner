import time

def current_milli_time():
    return round(time.time() * 1000)

BASE = 62
CHARSET_DEFAULT = "sAYBX3ptCazn10F2kJjVMhuwDqvWmRgf5obLcxQ7iZNd89ryUKeTGSl4HEOP6"
length_of_string = 7

def encode(charset=CHARSET_DEFAULT):
    n = current_milli_time()
    chs = []
    while n > 0:
        n, r = divmod(n, BASE)
        chs.insert(0, charset[r])
    if not chs:
        return charset[0]
    return charset[0]*(length_of_string-len(chs))+"".join(chs)
