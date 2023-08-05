menu = [ "espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffe(coffee):
    if coffee[0] == 'c':
        return coffee

map_coffee = map(find_coffe, menu)
print(map_coffee)

for x in map_coffee:
    print(x)
    
filter_coffee = filter(find_coffe, menu)
for x in filter_coffee:
    print(x)
    
    
    