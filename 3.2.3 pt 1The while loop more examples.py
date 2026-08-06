odd_number = 0 #odd number count
even_number = 0 #even number count

number = int(input("Enter a number o type 0 to stop: "))

while number != 0: #if number is diferent from zero the code will continue to loop
    
    if number % 2 == 1: #calculate if number is odd 
        odd_number += 1
    else: #to calculate even number you have to "even_number % 2 == 0" 
        even_number += 1

        number = int(input("Enter a number or type 0 to stop: ")) #continue

print(f"total odd numbers is {odd_number}")
print(f"total even numbers is {even_number}")