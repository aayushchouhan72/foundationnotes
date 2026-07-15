'''
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5


'''

st= input("ENter your complaint message :- ").strip()

if st.count(" ") == 0:
    print("Enter the string of words its single string ...")
else:
    print(f"Total Words: {len(st.split(' '))}")

