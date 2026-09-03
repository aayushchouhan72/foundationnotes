# 92 Check if two strings are pq-balanced. S1 = "pqqp", S2 = "qpqp" Example dependent on specific "pq-balanced" definition

s1 = input("Enter the string  first ...")
s2 = input("Enter the string second ...")

def pqbal(s1,s2):
    if not (s1.count('p')  ==  s1.count('q')):
        return False
    if not (s1.count('p')  ==  s1.count('q')):
         return False
    return True


print ("pq-Balanced string " if pqbal(s1,s2) else "Not pq-balanced string")
          