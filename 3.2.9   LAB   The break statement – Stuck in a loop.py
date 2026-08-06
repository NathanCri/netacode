secret_word = "chupacabra"

question = input("enter an word ")
while question != secret_word:
    print("You still inside my loop")
    question = input("enter a word ")
else:
    print("You've successfully left the loop.")