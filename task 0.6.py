a = int(input())
b = int(input())
c = int(input())

def maximum(a, b, c):
    if a >= b and a >= c:
        ans = print(a)
        return ans
    if b >= a and b >= c:
        ans = print(b)
        return ans
    if c >= a and c >= b:
        ans = print(c)
        return ans

maximum(a, b, c)                

