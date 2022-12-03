'''1) write a program to take a input from the user and print the details
   *Employee Name
   *Employee Age
   *Employee Phone Number\
   *EMployee Address
along with this print the type of all the variables
'''

'''
eName=input("Enter Employee Name : \n")
eAge=int(input("Enter Employee Age : \n"))
ePhone=int(input("Enter Employee Number : \n"))
eAddress=input("Enter Employee Adress : \n")
print("Employee Name",eName)
print("Employee age",eAge)
print("Employee num",ePhone)
print("Employee address",eAddress)
print("Employee Name type",type(eName))
print("Employee age type",type(eAge))
print("Employee num type",type(ePhone))
print("Employee address type",type(eAddress)) '''

'''

2)write a program to take a input from the user and print the details
  *Student Name 
  *Student maths marks
  *Student science marks

->print student name in Upper case
->add students marks (math+science) then print the total marks
->then find the average of two subjects


'''
name=input("Enter Your Name\n")
maths=int(input("enter the maths marks :\n"))
science=int(input("enter the science marks :\t"))
print("i am converting the name into uppercase")

print("Name is ",name.upper())
total=maths+science                                                     
print("total marks obtained by ",name,':',total)
print("average marks obtained by ",name,':',total//2)