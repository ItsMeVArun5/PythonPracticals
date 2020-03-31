class Error(Exception):
    pass

class LargeValueError (Error):
    pass

class SmallValueError (Error):
    pass

n = 4
while True:
    try:
        num = int(input("Enter a number:"))
        if num < n:
            raise SmallValueError
        elif num > n:
            raise LargeValueError
        else:
            raise Error

    except SmallValueError:
            print("You entered a small value")
            print()

    except LargeValueError:
            print ("You entered a large value")
            print ()
    
    except Exception:
            print("something went wrong")
