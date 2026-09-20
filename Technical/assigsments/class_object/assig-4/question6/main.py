from models.customer import Customer


customers = []

print("=" * 50)
print("       CUSTOMER MANAGEMENT SYSTEM")
print("=" * 50)



for i in range(5):

    print(f"\nEnter details of Customer {i + 1}")

    customer_id = int(input("Enter Customer Id : "))
    customer_name = input("Enter Customer Name : ")
    city = input("Enter City : ")
    purchase_amount = float(input("Enter Purchase Amount : "))

    customer = Customer(
        customer_id,
        customer_name,
        city,
        purchase_amount
    )

    customers.append(customer)


print("\n" + "=" * 50)
print("All Customers:")
print("=" * 50)

for customer in customers:
    customer.display()


search_city = input("\nEnter City : ")

print(f"\nCustomers from {search_city}:")

found = False

for customer in customers:

    if customer.city.lower() == search_city.lower():

        print(
            customer.customer_id,
            customer.customer_name,
            customer.purchase_amount
        )

        found = True

if not found:
    print("No customers found.")



print("\nCustomers with purchase amount greater than 10000:")

for customer in customers:

    if customer.purchase_amount > 10000:

        print(
            customer.customer_id,
            customer.customer_name,
            customer.purchase_amount
        )


highest_customer = customers[0]

for customer in customers:

    if customer.purchase_amount > highest_customer.purchase_amount:
        highest_customer = customer


print("\nHighest Purchase Customer:")
print(
    highest_customer.customer_id,
    highest_customer.customer_name,
    highest_customer.purchase_amount
)



total_sales = 0

for customer in customers:

    total_sales = total_sales + customer.purchase_amount


print("\nTotal Sales:")
print(total_sales)


# Average purchase amount
average_purchase = total_sales / len(customers)

print("\nAverage Purchase Amount:")
print(average_purchase)


# Search customer using ID
search_id = int(input("\nSearch Customer Id : "))

found = False

for customer in customers:

    if customer.customer_id == search_id:

        print("\nCustomer Found:")
        customer.display()

        found = True
        break

if not found:
    print("\nCustomer Not Found")