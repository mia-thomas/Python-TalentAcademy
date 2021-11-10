appleWeightKG = 0.2
appleWeightLB = 0.4
appleRequest = input("Hello, how many apples would you like today?")
appleAmmount = int(appleRequest)

print("you would like "+ appleRequest + " Apples.")

print("Would you like your apples to be weighed in lbs or kgs?")

appleMass = input("If you would like your apples weighed in KG please type 1, if you would like your apples weighed in LBS please type 2: ")
massValue = int(appleMass)

if massValue == 1:
    appleCostKG = float(appleAmmount) * appleWeightKG
    print("Your Apples weigh",appleCostKG, "Kgs")
elif massValue == 2:
    appleCostLB = int(appleRequest) * appleWeightLB
    print("Your Apples weighs" * appleCostLB, "lbs")
else: 
    print("invalid input")



#apples = 5 * appleWeight

