# 12.

# =========================================
# ONLINE FOOD DELIVERY ANALYSIS
# =============================

# orders = [
# "Pizza",
# "Burger",
# "Pizza",
# "Pasta",
# "Burger",
# "Pizza",
# "Pasta"
# ]

# Write a program to:

# * Count orders of each food item.
# * Find the most ordered item.

# Sample Output:
# Pizza : 3
# Burger : 2
# Pasta : 2

# Most Ordered : Pizza

# ---
orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

dic ={}
for i in orders:
    dic[i] = dic.get(i,0)+1

maxcity=''
maxcount=0
for k,v in dic.items():
    if maxcount <v:
        maxcity=k
        maxcount=v


print(dic)
print("Most orderd iteam , ",maxcity)