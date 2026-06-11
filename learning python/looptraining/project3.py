#the shop caluclator code
cart = []
total_price = []

print("welcome to the shop calculator")
product_number = int(input("how many products do you have in your basket: "))
for i in range(1,product_number + 1):
    name = input(f"what is product number {i}: ").lower()
    cart.append(name)
    product_amount = float(input("insert amount number: "))
    price = float(input("insert price"))
    total_price.append(product_amount * price)
answer = input("would ypu like to see what is in your basket? yes/no: ").lower()
if answer == "yes":
    print(cart)
answer2 = input("do you want to know full price? yes/no: ").lower()
if answer2 == "yes":
    print(sum(total_price))
print("thanks for using our service!")
