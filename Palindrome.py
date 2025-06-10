# Game continues until user types exit
while True:
    word = input("Enter a word to check (or type 'exit' to quit): ").lower()

    if word == "exit":
        print("Thanks for playing!")
        break

    # Reverse the word using slicing
    reversed_word = word[::-1]

    if word == reversed_word:
        print("It's a palindrome!")
    else:
        print("Not a palindrome.")
