import math 

appleWeightKG = (1 / 5)

appleWeightLBS = (2.2 / 5)

appleRequest = int(input("Hello, how many apples would you like today?"))
weightRequest = input("Great! would you like them weighed in LBS or KG?")


if weightRequest == "lbs":
    lbsApple = appleWeightLBS * appleRequest
    print("Your Apples Weigh:", lbsApple, "lbs") 
elif weightRequest == "kg":
    kgApple = appleWeightKG * appleRequest
    print("Your Apples Weigh:", kgApple, "kg")
else:
    print("Please try again. Invalid input")

    