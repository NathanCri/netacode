largest_number = -999999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end progam: "))
    if number == -1:
        break
    counter += 1 
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("the largest number is largest number", largest_number)
else:
    print("you haven't entered any number.")