import calculate

length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(F"The area of the rectangle is: {area}")
print(F"The perimeter of the rectangle is:{perimeter}")