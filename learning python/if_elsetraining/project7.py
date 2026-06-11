#advanced version of checking eligablity of getting egyptian license using nested if statement

nation = input("are you egyptian? (yes or no)\n")
if nation.lower() == "yes":
    age = int(input("how old are you?\n"))
    if age >= 18:
        print("you can get license")
    else: 
        print("you are not old enough")
elif nation.lower() == "no":
    print("you are not egyptian, you cannot apply")
else:
    print(f"your answer ({nation}) is unrecognized")