# =========================================================
# ASSIGNMENT 3: PRODUCT INVENTORY MANAGEMENT SYSTEM
# =========================================================

# SCENARIO
# --------
# A retail shop wants to manage product details, prices,
# categories, and available stock using Python PDBC.

# CONCEPTS TO PRACTICE
# --------------------
# 1. INSERT
# 2. SELECT
# 3. UPDATE
# 4. DELETE
# 5. LIKE operator
# 6. Parameterized queries
# 7. commit()
# 8. fetchall()
# 9. Menu-driven programming


# TABLE STRUCTURE
# ===============

# Table Name: product_pdbc

# Column       Data Type
# --------------------------------
# pid          INT PRIMARY KEY
# pname        VARCHAR(60)
# category     VARCHAR(40)
# price        DECIMAL(10,2)
# quantity     INT


# SAMPLE DATA
# ===========

# pid   pname       category       price       quantity
# ------------------------------------------------------------
# 301   Laptop      Electronics    55000.00    10
# 302   Mouse       Electronics      800.00    50
# 303   Keyboard    Electronics     1500.00    30
# 304   Notebook    Stationery       100.00   100
# 305   Pen         Stationery        20.00   200


# MENU
# ====

# ===== PRODUCT INVENTORY SYSTEM =====
# 1. Add Product
# 2. Display All Products
# 3. Search Product by Name
# 4. Update Product Price
# 5. Delete Product
# 6. Exit

# Enter your choice:


# TASK 1: ADD PRODUCT
# ===================

# INPUT
# -----
# Enter your choice: 1
# Enter Product ID: 306
# Enter Product Name: Monitor
# Enter Category: Electronics
# Enter Price: 12000
# Enter Quantity: 15

# OUTPUT
# ------
# Product inserted successfully.


# TASK 2: DISPLAY ALL PRODUCTS
# ============================

# INPUT
# -----
# Enter your choice: 2

# OUTPUT
# ------
# ID    Product       Category       Price       Quantity
# ------------------------------------------------------------
# 301   Laptop        Electronics     55000.00    10
# 302   Mouse         Electronics       800.00    50
# 303   Keyboard      Electronics      1500.00    30
# 304   Notebook      Stationery        100.00   100
# 305   Pen           Stationery         20.00   200
# 306   Monitor       Electronics     12000.00    15


# TASK 3: SEARCH PRODUCT BY NAME USING LIKE
# =========================================

# INPUT
# -----
# Enter your choice: 3
# Enter product name to search: o

# OUTPUT
# ------
# Matching products:

# ID    Product       Category       Price       Quantity
# ------------------------------------------------------------
# 301   Laptop        Electronics     55000.00    10
# 302   Mouse         Electronics       800.00    50
# 304   Notebook      Stationery        100.00   100
# 306   Monitor       Electronics     12000.00    15

# NOTE
# ----
# Use:
# WHERE pname LIKE %s

# Pass:
# '%' + search_name + '%'


# TASK 4: UPDATE PRODUCT PRICE
# ============================

# INPUT
# -----
# Enter your choice: 4
# Enter Product ID: 302
# Enter New Price: 900

# OUTPUT
# ------
# Product price updated successfully.


# TASK 5: DELETE PRODUCT
# ======================

# INPUT
# -----
# Enter your choice: 5
# Enter Product ID: 305

# OUTPUT
# ------
# Product deleted successfully.


# TASK 6: EXIT
# ============

# INPUT
# -----
# Enter your choice: 6

# OUTPUT
# ------
# Thank you for using Product Inventory System.


# add these scenarios also:--

# 1. Display all products from Electronics category.
# 2. Display all products from Stationery category.
# 3. Search products whose names contain 'oo'.
# 4. Search products whose names start with 'M'.
# 5. Search products whose names end with 'e'.
# 6. Display products whose price is greater than 1000.
# 7. Display products whose quantity is less than 20.
# 8. Update product quantity.
# 9. Update product category.
# 10. Delete a product by ID.
# 11. Display products whose category contains 'tron'.
# 12. Search products by a user-provided price range.



# SUGGESTED SUCCESS MESSAGES
# ==========================

# INSERT:
# Record inserted successfully.

# SELECT:
# Records displayed successfully.

# UPDATE:
# Record updated successfully.

# DELETE:
# Record deleted successfully.

# NOT FOUND:
# No record found for the given ID.

# INVALID CHOICE:
# Invalid choice. Please try again.

# EXIT:
# Thank you for using the system.

import mysql.connector


# Database Connection
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='komal',
        database='assigment_pdbc'
    )


# Application Functions

def add_product(id, name, cat, price, qty):
    try:
        db = connect_db()
        cur = db.cursor()

        cur.execute(
            'insert into product_pdbc(pid, pname, category, price, quantity) '
            'values(%s,%s,%s,%s,%s)',
            (id, name, cat, price, qty)
        )

        db.commit()

        print("Product Added Successfully ✅✅")

    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection", e)



def display_product(display=True):
    try:
        db = connect_db()
        cur = db.cursor()

        cur.execute("select * from product_pdbc")
        rows = cur.fetchall()

        if display:
            print('ID    Name        Category        Price       Quantity')

            for row in rows:
                print(f'{row[0]}   {row[1]}   {row[2]}   {row[3]}   {row[4]}')

        return rows

    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection", e)



def search_by_name(name):
    try:
        db = connect_db()
        cur = db.cursor()

        cur.execute(
            "select * from product_pdbc where pname like %s",
            ("%" + name + "%",)
        )

        rows = cur.fetchall()

        if not rows:
            print("Product not found ..")
            return

        print('ID    Name        Category        Price       Quantity')

        for row in rows:
            print(f'{row[0]}   {row[1]}   {row[2]}   {row[3]}   {row[4]}')

        return rows

    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection", e)



def update_product_price(pid, newprice):
    try:
        db = connect_db()
        cur = db.cursor()

        cur.execute(
            "update product_pdbc set price=%s where pid=%s",
            (newprice, pid)
        )

        db.commit()

        print("Product price updated successfully ✅✅")

    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection", e)


# Delete Product
def delete_product(pid):
    try:
        db = connect_db()
        cur = db.cursor()

        cur.execute(
            "delete from product_pdbc where pid=%s",
            (pid,)
        )

        db.commit()

        print("Product deleted successfully ✅✅")

    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection", e)


# Custom Exceptions


class Invalidproductname(Exception):
    pass


class Invalidcategory(Exception):
    pass


class Invalidprice(Exception):
    pass


class Invalidquantity(Exception):
    pass


class Invalidproducttoupdate(Exception):
    pass


class Invalidproducttodelete(Exception):
    pass


# Valid Categories

categories = [
    "electronics",
    "stationery",
    "clothing",
    "food",
    "furniture",
    "books",
    "sports",
    "beauty",
    "toys",
    "mobile",
    "computer"
]


while True:

    print("""
 ===== PRODUCT INVENTORY MANAGEMENT SYSTEM =====

 1. Add Product
 2. Display All Products
 3. Search Product by Name
 4. Update Product Price
 5. Delete Product
 6. Exit

 """)

    try:

        choice = int(input("Enter the choice "))

        match choice:
            case 1:

                id = int(input("Enter the product id "))

                name = input("Enter the product name ").lower()

                for i in name:
                    if not (97 <= ord(i) <= 122):
                        raise Invalidproductname(
                            "Enter the valid product name.."
                        )

                cat = input("Enter the category ").lower()

                if cat not in categories:
                    raise Invalidcategory(
                        "Enter the valid category"
                    )

                price = float(input("Enter the product price "))

                if price <= 0:
                    raise Invalidprice(
                        "Invalid product price"
                    )

                qty = int(input("Enter the quantity "))

                if qty < 0:
                    raise Invalidquantity(
                        "Invalid quantity"
                    )

                add_product(id, name, cat, price, qty)


            case 2:

                display_product()

            case 3:

                name = input("Enter the product name to search ")

                search_by_name(name)

            case 4:

                pid = int(input("Enter the product id "))

                newprice = float(input("Enter new price "))

                if newprice <= 0:
                    raise Invalidprice(
                        "Invalid product price"
                    )

                products = display_product(display=False)

                for row in products:

                    if row[0] == pid:
                        break

                else:
                    raise Invalidproducttoupdate(
                        "Invalid product to update "
                    )

                update_product_price(pid, newprice)

            case 5:

                pid = int(input("Enter the product id "))

                products = display_product(display=False)

                for row in products:

                    if row[0] == pid:
                        break

                else:
                    raise Invalidproducttodelete(
                        "Invalid product to delete "
                    )

                delete_product(pid)


            # Exit
            case 6:

                print("Closing an application")

                break

    except (
        Invalidcategory,
        Invalidprice,
        Invalidproductname,
        Invalidquantity,
        Invalidproducttoupdate,
        Invalidproducttodelete
    ) as e:

        print(e)

    except ValueError:

        print("Invalid value enter ")