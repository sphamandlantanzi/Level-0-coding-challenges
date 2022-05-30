number_1 = 3
number_2 = 99
number_3 = 46

def maximum(number_1, number_2, number_3):
    if number_1 >= number_2 and number_1 >= number_3:
        return number_1
    if number_2 >= number_1 and number_2 >= number_3:
        return number_2
    if number_3 >= number_1 and number_3 >= number_2:
        return number_3

print(maximum(number_1, number_1, number_3))          
