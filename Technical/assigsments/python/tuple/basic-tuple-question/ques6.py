lis = []
number = int(input("Enter the number of products "))

print()
for i in range(number):
    print()
    product_id = input("Enter the product id ....")
    product_name = input("Enter the product name ....")
    price = int(input("Enter product price ...."))
    lis.append((product_id, product_name, price))
    print()

maximum = lis[0]
minimum = lis[0]
total = 0

print("All Products:")
for i in lis:
    print(i)

    if maximum[2] < i[2]:
        maximum = i

    if minimum[2] > i[2]:
        minimum = i

    total += i[2]

print()

print("Costliest Product:")
print(maximum)

print()

print("Cheapest Product:")
print(minimum)

print()

print("Average Price:")
print(total / number)

print()

print("Products Above ₹50,000:")
for i in lis:
    if i[2] > 50000:
        print(i)