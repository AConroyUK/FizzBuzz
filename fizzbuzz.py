for i in range(100):
    str = ""
    if i % 3 == 0:
        str = str + "Fizz"
    if i % 5 == 0:
        str = str + "Buzz"
    if i % 7 == 0:
        str = str + "Bang"
    if i % 11 == 0:
        str = "Bong"

    if str == "":
        str = i
    print(str)
