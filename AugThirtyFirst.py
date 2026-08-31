initial_string = "BAJAJ-SHOE-10-RED"
brand = initial_string[0:5].lower()
type = initial_string[6:10].lower()
size = str(initial_string[11:13])
color = initial_string[14:17].lower()
print(color)

URL = "shop.com/"+brand+"/"+type+'/'+color+'/'+size
print(URL)