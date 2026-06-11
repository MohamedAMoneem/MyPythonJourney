# this code chooses random person from group inserted to pay


# import random
# name_string = input("""
# i will choose who pays!
#     please enter names with comma between them
# """)
# name = name_string.split(", ")
# name_len = int(len(name)) - 1
# choice = random.randint(0,name_len)
# print(f"i choose {name[choice]} to pay")

#simplified version

import random
names = input(f"""
i will choose who pay
      enter names between comma : 
""").split(", ")
print(f"i choose {random.choice(names)} to pay")