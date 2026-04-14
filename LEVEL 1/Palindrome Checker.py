# Palindrome Checker

def is_palindrome(text):
    # Clean the input: remove spaces and convert to lowercase
    cleaned = ''.join(text.split()).lower()
    
    # Reverse the cleaned string
    reversed_text = cleaned[::-1]
    
    # Compare original cleaned and reversed
    return cleaned == reversed_text

# Take input from user
user_input = input("Enter a word, sentence, or number: ")

# Check palindrome
if is_palindrome(user_input):
    print("✅ It is a palindrome!")
else:
    print("❌ It is not a palindrome.")