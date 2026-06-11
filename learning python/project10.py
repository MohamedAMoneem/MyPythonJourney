# this code is about a rabbit game
rows =[["🌿" , "🌿" , "🌿"],["🌿" , "🌿" , "🌿"],["🌿" , "🌿" , "🌿"]]
print(f"welcome to place the rabbit\n\n{rows[0]}\n{rows[1]}\n{rows[2]}\n")
rabbit = "🐇"
location = input(f"where should the rabbit go? {rabbit}\nplease choose column and row: ")
rows[int(location[0])-1][int(location[1])-1] = rabbit
print(f"\n{rows[0]}\n{rows[1]}\n{rows[2]}\n")