status = (input("Enter 0 if you are fresher, Enter 1 if you are experienced "))

if status == "0":
    print("1- Web Dev\n")
    print("2- App Dev\n")
    print("3- DS AI ML\n")
    field = (input("Enter the number corresponding to respective field displayed above  you want to make your career in \n"))
    if field == "1":
        print("1-Learn HTML,CSS\n")
        print("2-Learn Python\n")
        print("3-Learn Django\n")
    elif field == "2":
        print("1-Learn Java+\n")
        print("2-Learn DSA\n")
        print("3-Learn Build Project\n")
    elif field == "3":
        print("1-Learn Python\n")
        print("2-Learn Maths\n")
        print("3-Learn SQL\n")
    else: 
        print("Re-enter and choose from given value\n")
        
elif status == "1":
    print("1- Data Analytics\n")
    print("2- Cloud Computing\n")
    print("3- Front End\n")
    field = int(input("Enter the number corresponding to respective field displayed above  you want to make your career in \n"))
    if field == "1":
        print("1-Learn Python\n")
        print("2-Learn Excel\n")
        print("3-Learn Powerbi\n")
    elif field == "2":
        print("1-Learn Devops\n")
        print("2-Learn Python for automation\n")
    elif field == "3":
        print("1-Learn Python\n")
        print("2-Learn Django for Backend\n")
    else: 
        print("Re-enter and choose from given value")
        
else:
    print("Re-enter and choose from 1 or 0")
        
    
    