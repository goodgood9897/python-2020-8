password = "1234567890000"
attempt = input("Please enter the password:")
while True:   
    if attempt == password:
        print("Password is correct")
        print("Door is open")
        break
        else:
        print("Password is not correct")
        print("Please enter again")
        attempt = input("Please enter the password:")