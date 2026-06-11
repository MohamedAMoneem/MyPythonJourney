# this code is about cities
area = input("choose your area (tanta) or (cairo) or (mansoura):\n")
if area.lower() == "cairo":
    print("we love cairo!")
elif area.lower() == "tanta":
    print("oh, tanta is intresting")
elif area.lower() == "mansoura":
    print("cool, i am from mansoura too!")
else:
    print(f"sorry, {area} is not supported")