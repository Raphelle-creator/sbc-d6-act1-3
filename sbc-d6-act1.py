word = input("Enter a word: ")
original_word = ''.join(word.split()).lower()
is_palindrome = True

for i in range(len(original_word) // 2):
    if original_word[i] != original_word[-i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")