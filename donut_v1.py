progress = True

CHOCOLATE_PRICE = float(2.50)
CARAMEL_PRICE = float(2.50)
CINNAMON_PRICE = float(1.20)

customer_num = 0

def DonutQuery():
    donut_count = []
    donut_type = []
    user_donut = 0
    repeat = True
    print("Donut Query Function (v1)")
    print("---------------------------")
    print("What types of Donut is to be ordered?")
    print("Chocolate Donut[1] Caramel Donut[2] Cinnamon Donut[3]")
    print("Pick the Donuts corresponding with their numbers, seperated by spaces")

    while repeat == True : 
        try:
            donut_count = input("Donuts: ").split()
            if donut_count in ['1', '2', '3']:
                break
                print("Success")
            else:
                raise ValueError
            
        except ValueError:
            print("That is neither 1, 2 or 3")
            
        print(donut_count)
        donut_count = []
        
    for donut in donut_count:
        if donut == '1':
            user_input = input("How many Chocolate Donuts? ($2.50 each): ")
        elif donut == '2':
            user_input = input("How many Caramel Donuts? ($2.50 each): ")
        elif donut == '3':
            user_input = input("How many Cinnamon Donuts? ($1.20 each: )")
    
    
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
print("Fname and Lname is {}".format(input_details[2]))




"""while progress == True:
    if progress == True:
        pass"""
        


























