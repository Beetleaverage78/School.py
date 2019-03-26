progress = True

CHOCOLATE_PRICE = float(2.50)
CARAMEL_PRICE = float(2.50)
CINNAMON_PRICCE = float(1.20)

customer_num = 0

def DonutQuery():
    
    
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
            user_input = Donut_Query()
        elif i == 4:
            break
        
        input_details.append(user_input)

    return input_details, customer_num



input_details = []
input_details, customer_num = InputQuery(input_details, customer_num)

print(input_details)
print("customer_num, date_order, fname, lname, customer_phone, donut_order")
print("Fname and Lnam is {}".format(input_details[2]))




"""while progress == True:
    if progress == True:
        pass"""
        


























