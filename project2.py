#this code is a price of a meter calculator

str_length = input("what is the length:\n")
str_width = input("what is the width:\n")
length = float(str_length)
width = float(str_width)
float_area = (length * width)
area = str(float_area)
print("Area is = " + (area))
str_price = input("price of meter:\n")
price = float(str_price)
total = price * float_area
lastprice = str(total)
print("total price is = $" + (lastprice))
