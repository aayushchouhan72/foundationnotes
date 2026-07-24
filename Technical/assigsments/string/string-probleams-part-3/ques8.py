'''

QNo 8:--
SMART TEXT PROCESSING SYSTEM

A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU
======================================================

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 :

Conditions: - Reverse the complete string - Ignore extra spaces - Keep
special characters (@,#,$,%) in their original positions - Do not use
built-in reverse functions

Example: Input: ja@va#py

Output: yp@av#aj

Test Case 1: ab@cd#ef Output: fe@dc#ba

Test Case 2: py@th#on Output: no@ht#yp

Test Case 3: java@proOutput : orpa@vaj

====================================================== Choice 2 :

Conditions: - Reverse every word separately - Words containing digits
should not be reversed - Ignore extra spaces between words - First
letter of each reversed word should become uppercase

Example: Input: java is easy123 programming

Output: Avaj Si easy123 Gnimmargorp

Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
Repoleved

Test Case 2: hello java99 world Output: Olleh java99 Dlrow

====================================================== Choice 3 :

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

Example: Input: Java python Java react Python

Output: React Python Java

Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

Test Case 2: Python React Java Python React Output: Java React Python

====================================================== Choice 4
======================================================

Program Closed Successfully

'''

while True:
    print("\n" + "=" * 20, "MENU", "=" * 20)
    print("===== Smart Text Processing System =====")
    print("1. Reverse Complete String")
    print("2. Reverse Every Word")
    print("3. Reverse Word Order")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    match choice:
        case 1:
            print("\n" + "=" * 20, "Choice 1", "=" * 20)

            st = input("Enter String: ")

            letters = ""
            special = {}
            pos = 0

            
            for ch in st:
                if ch.isalpha():
                    letters += ch
                else:
                    special[pos] = ch
                pos += 1

           
            rev = ""
            i = len(letters) - 1
            while i >= 0:
                rev += letters[i]
                i -= 1

            
            ans = ""
            j = 0

            for i in range(len(st)):
                if i in special:
                    ans += special[i]
                else:
                    ans += rev[j]
                    j += 1

            print("Output:", ans)

        
        case 2:
            print("\n" + "=" * 20, "Choice 2", "=" * 20)

            st = " ".join(input("Enter String: ").split())

            words = st.split()
            ans = ""

            for word in words:

                digit = False
                for ch in word:
                    if ch.isdigit():
                        digit = True
                        break

                if digit:
                    ans += word + " "
                else:
                    rev = ""
                    i = len(word) - 1
                    while i >= 0:
                        rev += word[i]
                        i -= 1

                    rev = rev[0].upper() + rev[1:].lower()
                    ans += rev + " "

            print("Output:", ans.strip())

        
        case 3:
            print("\n" + "=" * 20, "Choice 3", "=" * 20)

            st = " ".join(input("Enter String: ").split())

            words = st.split()

            unique = []

            for word in words:
                found = False
                for x in unique:
                    if x.lower() == word.lower():
                        found = True
                        break

                if not found:
                    unique.append(word)

            ans = ""

            i = len(unique) - 1
            while i >= 0:
                ans += unique[i] + " "
                i -= 1

            print("Output:", ans.strip())

        
        case 4:
            print("\nProgram Closed Successfully")
            break

        
        case _:
            print("Invalid Choice!")