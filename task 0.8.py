num = int(input())

def clock(num):
    qoutient   = num // 60
    hour       = num / 60
    min_dec    = hour - qoutient
    min        = int(min_dec * 60)

    if qoutient <= 1:
        a = print(qoutient,"hour,",min,"minutes")
        return a
    if qoutient > 1:
        b = print(qoutient,"hours,",min,"minutes")
        return b
        
clock(num)
