progress = True

CHOCOLATE_CARAMEL_PRICE = float(2.50)
CINNAMON_PRICE = float(1.20)

customer_num = 0

def DonutQuery():
    donut_type = []
    donut_type_total = []
    donut_count = {}
    donut_total_cost = 0

    print("---------------------------")
    print("Donut Query Function (v2)")
    print("---------------------------")
    print("What types of Donut is to be ordered?")
    print("Chocolate Donut[1] Caramel Donut[2] Cinnamon Donut[3]")
    print("Pick the Donuts corresponding with their numbers, seperated by spaces")

    donut_count = input("Donuts: ").split()     
    print(donut_count)
    
    for donut in donut_type:
        if donut == '1':
            user_input = int(input("How many Chocolate Donuts? ($2.50 each): "))
            donut_count["Chocolate"] = user_input
        elif donut == '2':
            user_input = int(input("How many Caramel Donuts? ($2.50 each): "))
            donut_count["Caramel"] = user_input
        elif donut == '3':
            user_input = int(input("How many Cinnamon Donuts? ($1.20 each: "))
            donut_count["Cinnamon"] = user_input

    print(donut_type)
    for donut, amount in donut_count.items():
        if donut == "Chocolate" or donut == "Caramel":
            donut_type_cost = CHOCOLATE_CARAMEL_PRICE * amount
        elif donut == "Cinnamon":
            donut_type_cost = CINNAMON_PRICE * amount
            
        donut_type_total.extend([donut, donut_type_cost])
        donut_total_cost += donut_type_cost
    
    print(donut_total_cost)
    print(donut_type_total)
    
    
def CalculateQuery():
    pass

def InputQuery(input_details, customer_num):
    user_input = 0 
    customer_num += 1
    input_details.append(customer_num)
    
    """customer_num, date_order, fname, lname, delivery_date, customer_phone, donut_order, total_cost"""

    for i in range(5):
        if i == 0:
            user_input = input("Date of Order: ")
        elif i == 1:
            user_input = input("Customer's First & Last Name: ").split()
        elif i == 2:
            user_input = input("Customer's Phone Number: ")
        elif i == 3:
            user_input = DonutQuery()
        elif i == 4:
            break
        
        input_details.append(user_input)
        
    return input_details, customer_num



input_details = []
input_details, customer_num = InputQuery(input_details, customer_num)

print(input_details)
print("customer_num, date_order, fname, lname, customer_phone, donut_order")
print(input_details[2])
