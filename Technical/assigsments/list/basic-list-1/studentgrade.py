# 5.
#  Student Grade Classification System (Python List Assignment)


# A school stores student marks in a list. The system must analyze the marks and generate a **clear performance report**
# by grouping students into grade categories.

# Write a Python program to:

# * Iterate through the list of marks
# * Assign grades based on marks:

#   * **>= 90 → A**
#   * **>= 75 and < 90 → B**
#   * **>= 50 and < 75 → C**
#   * **< 50 → Fail**
# * Store each category in separate lists
# * Count students in each category
# * Display a **final structured report (important)**

# ---

# ## 📌 Output Format (Mandatory)

# Your output must be displayed exactly in this format:

# ```
# ===== STUDENT GRADE REPORT =====

# A Grade Students   : [list]
# B Grade Students   : [list]
# C Grade Students   : [list]
# Fail Students      : [list]

# --------------------------------
# A Count   : X
# B Count   : X
# C Count   : X
# Fail Count: X
# --------------------------------

# Total Students: X
# ```

# ---

#  Input

# [95, 82, 67, 45, 30]

# Output

# ```
# ===== STUDENT GRADE REPORT =====

# A Grade Students   : [95]
# B Grade Students   : [82]
# C Grade Students   : [67]
# Fail Students      : [45, 30]

# --------------------------------
# A Count   : 1
# B Count   : 1
# C Count   : 1
# Fail Count: 2
# --------------------------------

# Total Students: 5


nums=list(map(int,input("Enter marks list").split()))
studentlist=[]
ag=[]
bg=[]
cg=[]
f=[]
for i  in nums:
    if  i >= 90:
        ag.append(i)
    elif 75<= i <=90:
        bg.append(i)
    elif 50<= i <75:
        cg.append(i) 
    else:
        f.append(i)
   

print("="*10,"STUDENT GRADE REPORT","="*10,end="\n\n")

print(f" A Grade Students   : {ag}\nB Grade Students   : {bg}\nC Grade Students   : {cg}\nFail Students      : {f}",end="\n\n")

print("-"*40)
print(f"A Count   : {len(ag)}\nB Count   : {len(bg)}\nC Count   : {len(cg)}\nFail Count: {len(f)}")


print("-"*40)
print(f"Total Student:{len(nums)}")


