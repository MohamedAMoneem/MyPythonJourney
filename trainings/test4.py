def info():
    form = {
        "name":input("what is your name? : "),
        "age":int(input("how old are you? : ")),
        "country":input("where are you from? : "),
    }
    print(form)
info()