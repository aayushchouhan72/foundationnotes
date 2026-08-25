# 3.

# =========================================
# WEBSITE PAGE VISIT TRACKER
# ==========================

# A website records page visits.

# pages = ["Home","About","Home","Contact","Home","About"]

# Write a program to:

# * Count visits of each page using a dictionary.
# * Display page name and visit count.

# Sample Output:
# Home visited 3 times
# About visited 2 times
# Contact visited 1 time

# ---

pages = ["Home","About","Home","Contact","Home","About"]

dic ={}
for i in pages:
    dic[i] = dic.get(i,0)+1

for k,v in dic.items():
      print(f"The {k} appered {v} times... ")