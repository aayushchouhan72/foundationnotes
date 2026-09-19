def add_doctor():
    did = int(input("Enter the patient id ..."))
    dname=  input("Enter the patient name ...")
    spec = input("Enter the specialization ...")
    exp =  int(input("Enter the exprience ..."))
    fess=float(input("Enter the consultation fees ..."))
    info = {
        "pid":did,
        "name":dname,
        "spec":spec,
        "exprience":exp,
        "fess":fess   
    }
    return info

def display_doctor(data):
    for i in data: 
        print(i)
     