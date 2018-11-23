from LC21_2_PersonClass import Person as pr
import pickle
import io
import os


class Employee(pr):
	empidcount=7332211
	resigned={}
	active={}
	
	def __init__(self,name,address,mobileno,aadharno,gender,salary,desig,location,division,projectname,email):
		pr.__init__(self,name,address,mobileno,aadharno,gender)
		self.empid=Employee.empidcount
		Employee.empidcount+=1
		self.__salary=salary
		self.desig=desig
		self.location=location
		self.division=division
		self.projectname=projectname
		self.email=email
		Employee.active[self.empid] = self
		
	
	def removeemployee(self,id):
		if id in Employee.active:
			print("Employee Removed")
			Employee.resigned[id]=Employee.active[id]
			del Employee.active[id]
		else:
			print("Employee not present")
			
	
	def updateaddress(self,addr):
		pr.updateaddress(self,addr)
		
	def updatename(self,name):
		pr.updatename(self,name)
		
	def updatemobile(self,no):
		pr.updatemobile(self,no)
	
	def salary(self):
		return self.__salary
	
	def __repr__(self):
		return "Emp Id: "+str(self.empid)+str(pr.__repr__(self))+"\nDesignation: "+str(self.desig)+"\nLocation: "+str(self.location)+"\nDivision: "+str(self.division)+"\nProject: "+str(self.projectname)+"\nEmail: "+str(self.email)+"\n"
	
	def updatesalary(self,amount):
		self.__salary=amount
	def updatedesig(self,desig):
		self.desig=desig
	def updatelocation(self,location):
		self.location=location
	def updatedivision(self,division):
		self.division=division
	def updateemail(self,email):
		self.email=email

def manager(ch):
	if ch==1:
		print("\nADD Employee")
		name=input("Enter name:\t")
		address=input("Address:\t")
		mobileno=eval(input("Enter mobile:\t"))
		aadharno=eval(input("Enter aadharno:\t"))
		gender=input("Enter gender (male/felmale):\t")
		salary=eval(input("Enter salary:\t"))
		desig=input("Enter Designation:\t")
		location=input("Enter Location:\t")
		division=input("Enter division:\t")
		projectname=input("Enter Project name:\t")
		email=input("Enter Email address:\t")
		S = Employee(name,address,mobileno,aadharno,gender,salary,desig,location,division,projectname,email)
		
	elif ch==2:
		print("\nRemove Employee")
		rmid=eval(input("Enter Employee ID no:\t"))
		if rmid in Employee.active :
			rm=Employee.active[rmid]
			rm.removeemployee(rmid)
		print("done")
	elif ch==3:
		print("\nUpdate Employee")
		updateemployee()
	elif ch==4:
		print("\nSearch")
		id=eval(input("Enter Emp id"))
		if id in Employee.active:
			print("Active  Employee")
		elif id in Employee.resigned:
			print("Resigned Employee")
		else:
			print("Invalid Id")
	elif ch==5:
		file='LC21_3_Employee.txt'
		os.remove(file)
		f=open(file,"wb")
		f.close()
		f=open(file,'ab')
		pickle.dump(Employee.empidcount,f)
		pickle.dump(Employee.active,f)
		pickle.dump(Employee.resigned,f)
		
		f.close()
		print("done")
		
		
def updateemployee():
	id=eval(input("Enter Employee  Id:\t"))
	ch=eval(input("\n\tUpdate:\n\t1.name\n\t2.address\n\t3.mobileno\n\t4.desig\n\t5.location\n\t6.Salary\n\t7.division\n\t8.email\n\tchoice:\t"))
	emp=Employee.active[id]
	if id in Employee.active:
		if ch==1:
			name=input("Enter Name:\t")
			emp.updatename(name)
		elif ch==2:
			addr=input("Enter address:\t")
			emp.updateaddress(addr)
		elif ch==3:
			mob=input("Enter mobileno:\t")
			emp.updatemobile(mob)
		elif ch==4:
			desig=input("Enter designation:\t")
			emp.updatedesig(desig)
		elif ch==5:
			loc=input("Enter location:\t")
			emp.updatelocation(loc)
		elif ch==6:
			sal=input("Enter salary:\t")
			emp.updatesalary(sal)
		elif ch==7:
			divi=input("Enter division:\t")
			emp.updatedivision(divi)
		elif ch==8:
			mail=input("Enter mailid:\t")
			emp.updateaddress(mail)
		else :
			print("Invalid choice")
			return
		
def main():
	ch=0
	file='LC21_3_Employee.txt'
	checkfile(file)
	
	while ch!=6:
		print(Employee.empidcount,"Employee class id")
		print(Employee)
		print(Employee.resigned)
		print(Employee.active)
		ch=eval(input("\n1.Add\n2.Remove\n3.Update\n4Search\n5.Save data to file\n6.Exit\nEnter choice:\t"))
		manager(ch)
	
	for i in Employee.active:
		print(Employee.active[i])
		print("------------")
	
def checkfile(file):
	exists = os.path.isfile(file)
	if exists:
		resp=eval(input("file exists do you want to load file(1) or dont (2):\t"))
		if resp==1 and os.path.getsize(file)>0:
			f=open(file,"rb")
			Employee.empidcount = pickle.load(f)
			Employee.active = pickle.load(f)
			Employee.resigned = pickle.load(f)
			f.close()

		else:
			os.remove(file)
	else:
		f=open(file,"wb")
		f.close()
	
if __name__=="__main__":
	main()