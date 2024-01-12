
tea = input("what tea would you like?")
sweetness = input("what sweetness would you like?")

def bobaOrder(tea, sweetness):
    if tea == "black milk tea":
        print("good choice")
    else:
        print("you should try black milk tea")
    if sweetness is not int:
        print("please enter integer")    
    if sweetness == 25:
        print("perfect choice")
    else:
        print("the only correct answer is 25")
        

bobaOrder(tea, sweetness)