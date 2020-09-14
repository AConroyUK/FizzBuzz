for i in range(200):
    myString = ""
    if i % 3 == 0:
        myString = myString + "Fizz"
    if i % 5 == 0:
        myString = myString + "Buzz"
    if i % 7 == 0:
        myString = myString + "Bang"
    if i % 11 == 0:
        myString = "Bong"
    if i % 13 == 0:
        index = myString.find("B")
        if index == -1:
            myString = myString + "Fezz"
        else:
            myString = myString[:index] + "Fezz" + myString[index:]
    if myString == "":
        myString = i
    #myString = str(i) + ": " + myString
    print(myString)
