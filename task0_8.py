num = 126

def clock(num):
    qoutient   = num // 60
    hour       = num / 60
    min_dec    = hour - qoutient
    min        = int(min_dec * 60)

    if qoutient <= 1:
        singular = print(qoutient,"hour,",min,"minutes")
        return singular
    if qoutient > 1:
        plural = print(qoutient,"hours,",min,"minutes")
        return plural
        
clock(num)
