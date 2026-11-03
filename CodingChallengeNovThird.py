menu = (('bagel',2.50),('muffin',2),('smoothie',3.75),('wrap',4.25),('juice',1.5))
customer_order = ['bagel','bagel']
seating = [["X", "X", "E", "X"],
           ["X", "X", "X", "X"],
           ["E", "X", "E", "E"]]       


def get_price(item):
    for i in menu:
        if i[0] ==item:
            return i[1]
    return -1

def add_to_order(order,item):
    for i in menu:
        if i[0]==item:
            order.append(item)
            
def remove_from_order(order,item):
    for i in range(0,len(order)+1):
        if order[i] == item:
            
            order.pop(i)
            print(order)
            break


#remove_from_order(customer_order,'bagel')
def get_cost(order,cost):
    for i in order:
        for x in menu:
            if i ==x[0]:
                cost +=x[1]
    return cost


def count_seats(seatingchart,count):
    for i in range(0,len(seatingchart)):
        for x in range(0,len(seatingchart[i])):
            if seatingchart[i][x] =='E':
                count +=1
    return count
print(count_seats(seating,0))

#print(get_cost(customer_order,0))
#print(get_price('ring'))