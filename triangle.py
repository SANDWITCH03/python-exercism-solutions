def is_valid_triangle(sides):
    a, b, c = sides

    return (
        a > 0 and
        b > 0 and
        c > 0 and
        a + b > c and
        b + c > a and
        a + c > b
    )


def triangle_type(sides):
    if not is_valid_triangle(sides):
        return "Not a valid triangle"

    a, b, c = sides

    if a == b == c:
        return "Equilateral triangle"

    elif a == b or b == c or a == c:
        return "Isosceles triangle"

    else:
        return "Scalene triangle"


# User input
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

sides = [a, b, c]

print(triangle_type(sides))