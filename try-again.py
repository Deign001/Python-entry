




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

    def gen(instance_info): #instance range generator
        for i in range(ec2):
            yield i
            
    import uuid
    
    def instance_id(string_length=10):
    #Returns a random string of length string_length.
        random = str(uuid.uuid4()) # Convert UUID format to a Python string.
        random = random.upper() # Make all characters uppercase.
        random = random.replace("-","") # Remove the UUID '-'.
        return random[0:string_length] # Return the random string.
    print(dept + instance_id(6))

instance_info() 
