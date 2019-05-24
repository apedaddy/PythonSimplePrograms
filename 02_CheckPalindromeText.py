    # Ask word from user and check if given text is palindrome or not
    # Any text read same on its reverse is palindrome
word = str.lower(input("Enter your word: "))
rev_word = word[::-1]
if word == rev_word:
    result = "Palindrome"
else:
    result = "Not palindrome"

print(f"\nGiven word {word} is : {result}")

