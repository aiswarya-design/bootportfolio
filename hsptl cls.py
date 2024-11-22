class Hospital:
    def __init__(self):
        self.hosname=input("Enter the name kof the Hospital")
        self.hosphone=int(input("Enter trhe number"))
        self.location=input("Enter the location")
    def showdetails(self):
        print("Hospitalname",self.hosname,"Hospitalnum",self.hosphone,"Location",self.location)

class Department:
    def __init__(self):
        self.dname=input("Enter the department name")
        self.dphone=int(input("Enter the phone number"))
        self.doctorname=input("Enter the doctor name")
    def showdetails1(self):
        print("Departmentname",self.dname,"Departmentnum",self.dphone,"Doctorname",self.doctorname)

class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patientname=input("Enter the name")
        self.age=int(input("Enter the age"))
        self.gender=input("Enter the gender")
        self.mobile=int(input("Enter the number"))
        self.address=int(input("Enter the address"))
    def showdetails2(self):
        Hospital.showdetails(self)
        Department.showdetails1(self)
        print("Patientname",self.patientname,"age",self.age,"gender",self.gender,"mobile",self.mobile,"address",self.address)

p=Patient()
p.showdetails2()

