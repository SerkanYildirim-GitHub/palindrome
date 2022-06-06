# a simple code to check if a user input is palindrome or not.
# Function to check the input and the "reverse of input" equals
import string
word = ""
def isPalindrome(word):
    # Get input word from user to check if it is Palindrome 
    ask = input("Which word would you like to check if it is a palindrome ?") 
    # remove spaces if user input is a sentence
    no_space = ask.replace(' ', '')
    # convert all letters to lowercase
    word = no_space.lower()
    if word == word[::-1]:
        print(f"\nYes! the word \"{ask}\" is a palindrome.!\n--------------------------------------------")
    else:
        print(f"\nNo, the word \"{ask}\" is NOT a palindrome.!\n--------------------------------------------")
    
    word = input("Want to check another word? (y)es / (n)o ")
    
    if word.lower() == "y":
        isPalindrome(ask)
    elif word.lower() =="n":
        print("Thank you for using our automated palindrome service. Bye! ")
    else:
        print("Invalid selection. BYE!")
        pass
isPalindrome(word)
