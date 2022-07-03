#**EC2 Random Name Generator** Several departments share an AWS environment. 
#Ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. 
#Use Python to create your unique EC2 names that the users can then attach to the instances. 
#Allow the user to input how many EC2 instances they want names for and output the same amount of unique names.
#Allow the user to input the name of their department that is used in the unique name.
#Generate random characters and numbers that will be included in the unique name.
#ADVANCED - The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments. 
#List these departments as options and if a user puts another department, print a message that they should not use this Name Generator. 
#Be sure to account for incorrect upper or lowercase letters in the correct department. Example: a user inputs accounting vs Accounting.
#!/usr/bin/env python3.7
import uuid
import string

def instance_info(): #Create our function
    ec2 = int(input("# of ec2's you want: "))
    dept = str(input("department name: "))
    
    if dept == "Marketing": #response/conditions for which instances names will be named.
        print("EC2 ID('s) are: ")
    elif dept == "marketing":
        print("EC2 ID('s) are: ")
    elif dept == "Accounting":
        print("EC2 ID('s) are: ")
    elif dept == "accounting":
        print("EC2 ID('s) are: ")
    elif dept == "FinOps":
        print("EC2 ID('s) are: ")
    elif dept == "finops":
        print("EC2 ID('s) are: ")
    elif dept == "Finops":
        print("EC2 ID('s) are: ")
    elif dept == "finOps":
        print("EC2 ID('s) are: ")
    else: 
        print("This feature is unavailable for your department at this time. ") #response for ineligible departments
        exit() #this will end operation for ineligble departments

    def gen(ec2): #generator that will create range of instances
        for x in range(ec2):
            yield x
    
    for x in gen(ec2):
        x = uuid.uuid1() #assigns unique id to our instances
        y = (dept + str(x)) #adds dept to our id
        print(y)

instance_info()