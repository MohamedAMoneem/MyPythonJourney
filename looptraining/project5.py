name = input("enter your friends full name with comma in between each name : ").split(", ")
short = []
for names in name:
    splitted = names.split()
    first = splitted[0][0]
    second = splitted[1][0]
    print(splitted)
    print(f"short names : \n{first}.{second}.")