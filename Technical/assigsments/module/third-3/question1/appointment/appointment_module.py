
def book_appointment():
    appid=int(input("Enter the appointmentID ..."))
    pid=  input("Enter the patient id  ...")
    did = input("Enter the dotor id ...")
    data= input("Enter the appointment date..")
    time = input("Enter the time ...")
    info = {
        "appointmentid":appid,
        "pid":pid,
        "did":did,
        "data":data,
        "time":time   
    }
    return info

def show_appointments(data):
    for i in data: 
            print(*i)
         

