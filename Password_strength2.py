def strength_check(password):
    strength = 0
    
    if len(password) >= 8:
        strength += 1
        
    #Returns True if there's at least one digit (0–9) in the password.
    if any(char.isdigit() for char in password):
        strength += 1
        
    #Returns True if a character is one of the special characters listed in the string.
    if any(char in "!@#$%^&*()" for char in password):
        strength += 1

    #Strength category based on score    
    if strength == 3:
        return "Strong."
    elif strength == 2:
        return "Med."
    else:
        return "Weak."

#Takes user input
passw = input("Enter your password: ")
print("Your password is",strength_check(passw))

#Suggests improving weak passwords
result = strength_check(passw)
if result == "Weak.":
    print("Please use a stronger password.")
