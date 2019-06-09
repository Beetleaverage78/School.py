
def display():
    print("=========== Donut Calculator Initialised =============")
    print("=================== Program Log ======================")

def calculate_method(self, donut, price, count, msg):
    sub_total = 0
    count += donut
    if count < 5:
        msg = "Minimum of 5 Donuts"
        judge = False
        print("Error - Amount of Donuts is less than 5")
        return judge, sub_total, msg
            
    elif count  >= 30:
        msg = "Maximum of 30 Donuts"
        judge = False
        print("Error - Amount of Donuts is greater than 30")
        return judge, sub_total, msg
            
    elif count >= 5 or count <= 30:
        sub_total = donut * price
        judge = True
        print("Calculated Sub_Cost of Donuts with corresponding Prices")
        return judge, sub_total, msg

def customer_details(f_name, l_name):
    if f_name.isalpha():
        print("Aight f_name it is a letter")
        if l_name.isalpha():
            print("Aight l_name it is a letter")
            return f_name, l_name
        
        else:
            print("Aight l_name is integer")
            l_name = False
            return f_name, l_name
        
    else:
        print("Aight f_name is integer")
        f_name = False
        return f_name, l_name

def save_orders(donut, count, total):
    print("Calling orders")
    msg = "{} Donuts - Amount: {}, Cost: ${:.2f}".format(donut, count, total)
    return msg
            
