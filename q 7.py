# Reverse a String  Word by Word

def reverse_words(input_str):
    words = input_str.split()
    reversed_words = ' '.join([word[::-1] for word in words])
    return reversed_words

input_string = "Hello World"
reversed_string = reverse_words(input_string)
print("Reversed string :", reversed_string)
