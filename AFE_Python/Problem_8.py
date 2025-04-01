# User should enter a no between 1 - 12 

num = int(input("Enter a number between 1 and 12: "))

match num:
    case 1:
        print("January")
    case 2:
        print("Februrary")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("Septemper")
    case 10:
        print("October")
    case 11:
        print("November")     
    case 12:
        print("december")     
    case _:
        print("Please enter a valid month.")
    