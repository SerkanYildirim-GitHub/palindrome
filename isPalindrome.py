# a simple code to check if a user input is palindrome or not.
# Function to check the input and the "reverse of input" equals
word = ""
def isPalindrome(word):
    # Get input word from user to check if it is Palindrome 
    word = input("Which word would you like to check if it is a palindrome ?") 
    
    if word == word[::-1]:
        print(f"\nYes! the word \"{word}\" is a palindrome.!\n--------------------------------------------")
    else:
        print(f"\nNo, the word \"{word}\" is NOT a palindrome.!\n--------------------------------------------")
    
    word = input("Want to check another word? (y)es / (n)o ")
    
    if word.lower() == "y":
        isPalindrome(word)
    elif word.lower() =="n":
        print("Thank you for using our automated palindrome service. Bye! ")
    else:
        print("Invalid selection. BYE!")
        pass
isPalindrome(word)


# Remove spaces from palindrome sentence

sentence = "This is a test sentence"
print(sentence)
new_sentence = sentence.replace(' ', '')
print(new_sentence)
