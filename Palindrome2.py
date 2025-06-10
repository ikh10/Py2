# Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]  # Reverse the word using slicing

# Ask user for input
text = input("Enter a word: ")

# Check and print result
if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
