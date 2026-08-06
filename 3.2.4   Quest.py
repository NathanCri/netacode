secret_number = 777

print(
    """
+===============================+
| Welcome to my game, muggle!   |
| Enter an integer number       |
| and guess what number I've    |
| picked for you.               |
| So, what is the secret number?|
+===============================+
""")

number = int(input("enter you number haha: "))
 
while number != secret_number:
    print(f"Ha ha! You're stuck in my loop!")
    number = int(input("Try again: ")) #asks again inside the loop
    print("Well done, muggle! You are free now.")