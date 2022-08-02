def clock(number):
    qoutient   = number // 60
    hour       = number / 60
    min_dec    = hour - qoutient
    min        = round(min_dec * 60)
    
    if qoutient == 0 and min == 1:
        return f"{qoutient} hours, {min} minute"
    
    if qoutient == 0:
        return f"{qoutient} hours, {min} minutes"
    
    if qoutient <= 1 and  min == 1:
        return f"{qoutient} hour, {1} minute"

    if qoutient <= 1 and min > 1:
        return f"{qoutient} hour, {min} minutes"  

    if qoutient <= 1 and min == 0:
        return f"{qoutient} hour, {0} minutes"    
       
    if qoutient > 1 and min != 1:
        return f"{qoutient} hours, {min} minutes"

    if qoutient > 1 and  min == 1:
        return f"{qoutient} hour, {1} minute"    
    
print(clock(157))
