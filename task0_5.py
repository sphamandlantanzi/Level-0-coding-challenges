a = 3
b = 4
c = 5
def find_area(a, b, c):
    s = (a + b + c) * 0.5
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

print(find_area(a , b , c))