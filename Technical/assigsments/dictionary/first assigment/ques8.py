
# 8.

# =========================================
# LIBRARY BOOK ISSUE TRACKER
# ==========================

# A library records issued books.

# books = [
# "Python",
# "Java",
# "Python",
# "C++",
# "Java",
# "Python"
# ]

# Write a program to:

# * Count how many times each book was issued.

# Sample Output:
# {
# 'Python':3,
# 'Java':2,
# 'C++':1
# }

# ---

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]


dic ={}
for i in books:
    dic[i] = dic.get(i,0)+1
print("{")
for k,v in dic.items():
      print(f"'{k}':{v}")
print("}")