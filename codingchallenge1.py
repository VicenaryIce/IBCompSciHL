

global smallPrice,mediumPrice,largePrice,addInPrice,plantMilkPrice,vat

smallPrice = 5
mediumPrice = 10
largePrice = 15
addInPrice = 2
plantMilkPrice = 5
vat = 0.21



def get_base_price():
    smoothieSize = input("What smoothie size do you want(S,M or L)? \n")

    if smoothieSize == "S":
        return smallPrice
    elif smoothieSize =="M":
        return mediumPrice
    elif smoothieSize =="L":
        return largePrice
    else:
        smoothieSize = input("You have input an invalid value. Please enter only S, M or L for size. What size would you like? \n")
        return get_base_price(smoothieSize)
def get_clean_addIns():
    addIns = input("How many add ins do you want? Put a whole number \n")
    try:
        return abs(int(addIns))
    except ValueError:
        print("Invalid value entered")
        return get_clean_addIns()

def get_clean_milk():
    plantMilk = input("Would you like plant-based milk in your smoothie(y/n)? \n").lower()
    if plantMilk == "y" or plantMilk == 'n':
        return plantMilk
    else:
        print('invalid value, please enter a valid value')
        return get_clean_milk()
basePrice = get_base_price()
addIns = get_clean_addIns()
milk = get_clean_milk()   




def calculate_total(basePrice,addIns, plantMilk,vat):
    totalprice = 0
    totalprice += basePrice
    totalprice +=  addIns *addInPrice
    if plantMilk =='y':
        totalprice += plantMilkPrice
    if input("Do you have a promo code to apply? \n") == "FRESH10":
        totalprice *=0.9

    totalprice *= (1+vat)
    return round(totalprice,2)


def test_totals():
    assert calculate_total(5,1,"y",0) == 12
    assert calculate_total(5,1,"y",0.1) == 13.2

print("Your total is: " + str(calculate_total(basePrice,addIns,milk,vat)))
print("Your base price was: " + str(basePrice))
print("The cost for your addins was: " +str(int(addIns*addInPrice)))
if milk == 'y':
    print("Because you ordered plant milk, you were charged " + str(plantMilkPrice) + " dollars extra")
else:
    print("You did not order plant milk")
print("The vat rate was: " +str(int(100*vat)) + "%")
