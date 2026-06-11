#this code checks if user is eligable for driving

age = int(input("how old are you\n"))
state = str(input("do you have license?\n"))
if age >= 18 and state.lower() == "yes":
    print("you can drive")
else:
    print("you cannot drive")