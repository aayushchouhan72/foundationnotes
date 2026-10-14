
# =========================================
# MOBILE APP DOWNLOAD COUNTER
# ===========================

# Downloads received from different cities:

# cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

# Write a program to:

# * Count downloads city-wise.
# * Display city with maximum downloads.

# Sample Output:
# {'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
# Most Downloads : Indore

# ---

ities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

dic ={}
for i in ities:
    dic[i] = dic.get(i,0)+1

maxcity=''
maxcount=0
for k,v in dic.items():
    if maxcount <v:
        maxcity=k
        maxcount=v


print(dic)
print("Max count city , ",maxcity)
    