import string

def remove_punctuation(word):
    return "".join(i.lower() for i in word if i in string.ascii_letters)

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = remove_punctuation(text)
    return text == reverse(text)

while True:
    something = raw_input("Enter text: ")
    if something == 'quit':
        break
    elif is_palindrome(something):
        print "Yes, it is a palindrome"
    else:
        print "No, it is not a palindrome"