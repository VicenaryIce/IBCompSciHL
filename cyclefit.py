import math

LONG_RENTAL_HOURS = 5
late_fee = 1.5
biketype = ''


def get_hourly_rate(bike_type):
    if bike_type.lower() == "city":
        return 3
    elif bike_type.lower() == "electric":
        return 6
    elif bike_type.lower() == "kids":
        return 2
def calculate_cost(rate,hours):
    basecost = rate*int(hours)
    if int(hours) >= LONG_RENTAL_HOURS:
        return 0.9*basecost
    else:
        return basecost
def calculate_late(hours):
    return int(hours)*late_fee

def print_fleet(rows,bikeperrow):
    for i in range(rows+1):
       print('[B]'*int(bikeperrow))



def mainloop():
    global biketype
    total_revenue = 0.0
    total_rentals = 0
    print_fleet(4,5)

    while biketype.lower() != 'done':
        biketype = str(input("What bike type was rented(City,Electric,Kids): "))
        if biketype == 'done':
            break
        hours = int(input("How long was this rented?: "))
        latehours = int(input("Late hours(0 if on time): "))
        rate = get_hourly_rate(biketype)
        cost = calculate_cost(rate,hours) + calculate_late(latehours)
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
        

mainloop()
#print(str(calculate_cost(get_hourly_rate(input("What bike type ")),input("How many hours did you rent this for?"))))
