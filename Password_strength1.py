passw = input("Enter your password: ")
strength = 0 

#Checks length of password
if len(passw) >=8:
    strength += 1

#Checks for at least one digit in password
if any(char.isdigit() for char in passw):
    strength += 1

#Checks for special characters in password
if any(char in "!@#$%^&*()" for char in passw):
    strength += 1

#Final total strength
if strength == 3:
    print ("Your password is Strong. ")
elif strength == 2:
    print ("Your password is Medium. ")
else:
    print("Your password is Weak.")
