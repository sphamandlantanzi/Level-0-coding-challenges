a = int(input())
b = int(input())
c = int(input())
def area(a, b, c):
    s = (a + b + c) * 0.5
    A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return A

print(area(a , b , c))    