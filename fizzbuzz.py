print("Enter max number")
max = input()

while max.isnumeric() == False:
    print("Please enter a numeric value for max number")
    max = input()

for i in range(1,int(max)+1):
    myString = ""
    if i % 3 == 0:
        myString = myString + "-Fizz"
    if i % 5 == 0:
        myString = myString + "-Buzz"
    if i % 7 == 0:
        myString = myString + "-Bang"
    if i % 11 == 0:
        myString = "-Bong"
    if i % 13 == 0:
        index = myString.find("B")
        if index == -1:
            myString = myString + "-Fezz"
        else:
            myString = myString[:index-1] + "-Fezz" + myString[index-1:]

    myList = myString.split("-")
    if i % 17 == 0:
        myList.reverse()
    myString = str(i) + ": "
    for word in myList:
        myString = myString + word

    if myString == "":
        myString = i

    print(myString)
