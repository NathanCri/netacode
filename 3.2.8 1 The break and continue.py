print("stuck in material world") #break test
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the world.", i)
print("Outide de world")

print("The continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("inside the material world", i)

print("Outside the material world")