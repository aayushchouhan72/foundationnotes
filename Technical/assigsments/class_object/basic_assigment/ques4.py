class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
        self.area = 0
        self.perimeter = 0

    def calculate_area(self):
        self.area = self.length * self.breadth

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.length + self.breadth)

    def display_result(self):
        print(f"""
Length       : {self.length}
Breadth      : {self.breadth}
Area         : {self.area}
Perimeter    : {self.perimeter}
""")


length = float(input("Enter the Length ..."))
breadth = float(input("Enter the Breadth ..."))

r1 = Rectangle(length, breadth)

r1.calculate_area()
r1.calculate_perimeter()
r1.display_result()