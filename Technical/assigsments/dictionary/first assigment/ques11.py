# 11.

# =========================================
# PRODUCT SALES ANALYSIS
# ======================

# sales = [
# "Mobile",
# "Laptop",
# "Mobile",
# "Tablet",
# "Laptop",
# "Mobile"
# ]

# Write a program to:

# * Count sales of each product.
# * Display products in sorted order.

# Sample Output:
# Laptop : 2
# Mobile : 3
# Tablet : 1

# ---

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]
sales.sort()


dic ={}
for i in sales:
    dic[i] = dic.get(i,0)+1

for k,v in dic.items():
      print(f"{k}:{v}")
