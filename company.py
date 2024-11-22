class Company:
    def getdetails(self):
        print("Enter the company details")
        self.companyname=input("Enter the company name")
    def showdetails(self):
        print("Companyname",self.companyname,end=" ")
class Development(Company):
    def getdetails1(self):
        Company.getdetails(self)
        print("Enter the developer details")
        self.developername=input("Enter the developername")
    def showdetails1(self):
        Company.showdetails(self)
        print("developerid",self.developerid,end=" ")
        print("developername",self.developername,end=" ")
class Testing(Company):
    def getdetails2(self):
        print("Enter the tester details")
        self.testerid=input("enter the testerid")
        self.testername=input("enter the testername")
    def showdetails2(self):
        print("testerid",self.testerid,end=" ")
        print("testername",self.testername,end=" ")


class Project(Development,Testing):
    def getdetails3(self):
        Development.getdetails1(self)
        Testing.getdetails2(self)
        print("Enter the project details")
        self.projectid=input("Enter the projectid")
        self.projectname=input("Enter the project name")
    def showdetails3(self):
        Development.showdetails(self)
        Testing.showdetails(self)
        print("project id",self.projectid,"projectname",self.projectname,end=" ")
p=Project()
p.getdetails3()
p.showdetails3()

