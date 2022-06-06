def clock(number):
    qoutient   = number // 60
    hour       = number / 60
    min_dec    = hour - qoutient
    min        = int(min_dec * 60)

    if qoutient == 0 and min == 1:
        return f"{qoutient} hour, {min} minute"
    
    if qoutient == 0:
        return f"{qoutient} hour, {min} minutes"
    
    if qoutient <= 1:
        return f"{qoutient} hour, {min} minutes"
       
    if qoutient > 1:
        return f"{qoutient} hours, {min} minutes"
    
print(clock(116))
