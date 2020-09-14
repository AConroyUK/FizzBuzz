import sys

def main(argv):
    if len(argv) == 0:
        argv = ['3','5','7','11','13','17']
    print(argv)

    print("Enter max number")
    max = input()

    while max.isnumeric() == False:
        print("Please enter a numeric value for max number")
        max = input()

    for i in range(1,int(max)+1):
        myString = ""
        if i % 3 == 0 and '3' in argv:
            myString = myString + "-Fizz"
        if i % 5 == 0 and '5' in argv:
            myString = myString + "-Buzz"
        if i % 7 == 0 and '7' in argv:
            myString = myString + "-Bang"
        if i % 11 == 0 and '11' in argv:
            myString = "-Bong"
        if i % 13 == 0 and '13' in argv:
            index = myString.find("B")
            if index == -1:
                myString = myString + "-Fezz"
            else:
                myString = myString[:index-1] + "-Fezz" + myString[index-1:]

        myList = myString.split("-")
        if i % 17 == 0 and '17' in argv:
            myList.reverse()
        myString = str(i) + ": "
        for word in myList:
            myString = myString + word

        if myString == "":
            myString = i

        print(myString)

if __name__ == "__main__":
    main(sys.argv[1:])
