def find_area(side_a, side_b, side_c):
    semi_peri = (side_a + side_b + side_c) * 0.5
    area = (semi_peri * (semi_peri - side_a) * (semi_peri - side_b) * (semi_peri - side_c)) ** 0.5
    return area

side_a = 3
side_b = 4
side_c = 5

print(find_area(side_a , side_b , side_c))
