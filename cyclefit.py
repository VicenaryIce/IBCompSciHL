import math
from multiprocessing import Value
from sqlite3 import enable_callback_tracebacks

LONG_RENTAL_HOURS = 5
late_fee = 1.5
biketype = ''
kidsCount = 0
cityCount = 0
eletricCount = 0


def get_hourly_rate(bike_type):
    global kidsCount,cityCount,eletricCount
    if bike_type.lower() == "city":
        cityCount += 1
        return 3
    elif bike_type.lower() == "electric":
        eletricCount +=1
        return 6
    elif bike_type.lower() == "kids":
        kidsCount +=1
        return 2
def calculate_cost(rate,hours,weekend):
    if weekend[0].lower() == 'y':
        week = 1.15
    else:
        week = 1
    basecost = rate * hours
    if int(hours) >= LONG_RENTAL_HOURS:
        return 0.9*basecost *week
    else:
        return basecost *week
def calculate_late(hours):
    return int(hours)*late_fee

def print_fleet(rows,bikeperrow):
    for i in range(rows+1):
       print('[B]'*int(bikeperrow))
def get_hours(hours):
    try:
        if int(hours) <0:
            return get_hours(input("Please enter a positive number: "))
        else:
            return int(hours)
    except ValueError:
        return get_hours(input("Enter a positive number, not a word: "))

def get_best_bike():
    maxcount = max(kidsCount, cityCount, eletricCount)
    
    if maxcount == 0:
        return "There was no one most popular bike"
    
    if cityCount == eletricCount == kidsCount:
        return "All three bike types were equally popular"
    
    if cityCount == eletricCount == maxcount:
        return "The city bike and electric bike were the most popular"
    elif cityCount == kidsCount == maxcount:
        return "The city bike and kids bike were the most popular"
    elif eletricCount == kidsCount == maxcount:
        return "The electric bike and kids bike were the most popular"
    
    elif kidsCount == maxcount:
        return "The kids bike was the most popular bike"
    elif cityCount == maxcount:
        return "The city bike was the most popular bike"
    elif eletricCount == maxcount:
        return "The electric bike was the most popular bike"
    
    



def mainloop():
    global biketype
    total_revenue = 0.0
    total_rentals = 0
    print_fleet(4,5)

    while biketype.lower() != 'done':
        biketype = str(input("What bike type was rented(City,Electric,Kids): "))
        if biketype == 'done':
            break
        hours = get_hours(input("How long was the bike rented for: "))
        
        latehours = int(input("Late hours(0 if on time): "))
        rate = get_hourly_rate(biketype)
        cost = calculate_cost(rate,hours,input("Is it weekend?")) + calculate_late(latehours)
        total_rentals +=1
        total_revenue+=cost
        print("Total cost: ",cost)
    
    print("---- Summary: ----")
    print("Total rentals: ",total_rentals)
    print("Total revenue: ",total_revenue)
    
    if total_rentals >0:
        print("Average revenue per rental: ",round((total_revenue/total_rentals),2))
    else:
        print("Average revenue per rental: ",0)
    print(get_best_bike())
        

mainloop()
#print(str(calculate_cost(get_hourly_rate(input("What bike type ")),input("How many hours did you rent this for?"))))
