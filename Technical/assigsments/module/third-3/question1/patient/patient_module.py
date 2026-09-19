
def add_patient():
    pid = int(input("Enter the patient id ..."))
    pname=  input("Enter the patient name ...")
    age = int(input("Enter the age ..."))
    gender = input("Enter the gender ...")
    dis = input("Enter the Disease ...")
    mnumber = int(input("Enter the number ..."))
    info = {
        "pid":pid,
        "name":pname,
        "age":age,
        "gender":gender,
        "dis":dis,
        "mnumber":mnumber,   
    }
    return info

def display_patient(data):
    for i in data:
        print(i)

def search_patient(data,find):
    for i in data:
        if find in i.keys():
            print(i)
    else:
         return "Data not Found"
     