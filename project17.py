import os
import time
def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")
def loading():
    time.sleep(3)
def calc(country,country2):
    dollar = currency["USD"]
    num1 = float(currency[country] / dollar)
    num2 = float(currency[country2] / dollar)
    rate = float(num2 / num1)
    return rate


print("""
                ______________
    __,.,---'''''              '''''---..._
 ,-'             .....:::''::.:            '`-.
'           ...:::.....       '
            ''':::'''''       .               ,
|'-.._           ''''':::..::':          __,,-
 '-.._''`---.....______________.....---''__,,-
      ''`---.....______________.....---''

_______________________________________________
      
""")
currency = {
    "USD":1,
    "EGP":49.3,
    "SAR":13.7,
    "YEN":254
}
for i in currency:
    print(f"{i}:{currency[i]}")
exit_all_loops = False
while True:
    choice1 = input("insert currency you have: ").upper()
    clear()
    choice2 = input("insert currency you want to convert to: ").upper()
    loading()
    if choice1 not in currency or choice2 not in currency:
        print("invalid currency. . .")
        clear()
    else:
        clear()
        rate = calc(choice1,choice2)
        print("trying to find best prices!. . . ")
        loading()
        print("calculating. . . . . ")
        loading()
        print(f"rate of {choice1} to {choice2} is: {rate}")
        choice3 = int(input("do you want to proceed? (1)\ndo you want to change options? (2)\nexit program? (3)\ninsert number: "))
        if choice3 == 3:
            break
        elif choice3 == 2:
            continue
        else:
            while True:
                choice4 = float(input("insert amount you want to convert: "))
                if input("confirm? yes, no: ").lower() == "no":
                    continue
                else:
                    clear()
                    print("converting. . . .")
                    loading()
                    print("converting completed! printing results. . . ")
                    loading()
                    print(f"transaction completed!, you now have {choice4 * rate}{choice2} in your account")
                    if input("do you want to exit program or do another transaction? yes/no: ").lower() == "yes":
                        clear()
                        exit()
                    else:
                        clear()
                        break
            continue
                
