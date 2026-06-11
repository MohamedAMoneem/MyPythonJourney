#this code stores favourite color then prints it

colors = []
user_color = input("what colour do you like? : ")
colors.append(user_color)
add_option = input("do you want to add another colour? : yes or no? : ")
if add_option.lower() == "yes":
    add_color = input("add another colour : ")
    colors.append(add_color)
    print("your favourite colours are:")
    print(colors)
elif add_option.lower() == "no":
    print("your favorite colours are:")
    print(colors)
else: print("please enter yes or no")