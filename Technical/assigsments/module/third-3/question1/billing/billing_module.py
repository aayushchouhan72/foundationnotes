def generate_bill():
    pid=  input("Enter the patient id  ...")
    cons= int(input("Enter the Consultation Charges"))
    med= int(input("Enter the Medicine Cost"))
    test=int(input("Enter Test Charges"))
    info = {
        "pid":pid,
        "cons":cons,
        "med":med,
        "test":test,
        "total":cons+med+test
    }
    return info

def show_bill(data):
    for i in data: 
            print(*i)
         