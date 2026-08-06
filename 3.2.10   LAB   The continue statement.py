user_word = input("Enter an word ")
user_word = user_word.upper()
vowels = "AEIOU"
for letter in user_word:
    if letter in vowels:
        continue
    else:
        sep="\n"
        print(letter)