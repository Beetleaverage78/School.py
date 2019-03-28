
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

    donut_type = input("Donuts: ").split()     
    
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

    for donut, amount in donut_count.items():
        if donut == "Chocolate" or donut == "Caramel":
            donut_type_cost = CHOCOLATE_CARAMEL_PRICE * amount
        elif donut == "Cinnamon":
            donut_type_cost = CINNAMON_PRICE * amount

        donut_total_cost += donut_type_cost
        donut_type_cost = "${0:.2f}".format(donut_type_cost)
        amount = "{} donuts".format(amount)
        donut_type_total.append([donut, donut_type_cost, amount])
        

    return donut_type_total, donut_total_cost

def InputQuery(input_details, customer_num):
    user_input = 0 
    customer_num += 1
    input_details.append(customer_num)
    donut_total_cost = 0
    donut_type_total = {}
    
    """customer_num, date_order, fname, lname, delivery_date, customer_phone, donut_order, total_cost"""

    for i in range(5):
        if i == 0:
            user_input = input("Date of Order: ")
        elif i == 1:
            user_input = input("Customer's First & Last Name: ").split()
        elif i == 2:
            user_input = input("Customer's Phone Number: ")
        elif i == 3:
            donut_type_total, donut_total_cost = DonutQuery()

        elif i == 4:
            break
        
        input_details.append(user_input)
        
    return input_details, donut_type_total, donut_total_cost

def CalculateQuery(input_details, donut_total, donut_type_details):
    count = 0
    checker = 0
    total_cost = 15
    total_cost += donut_total
    print("--------------------------")
    print("Final Customer Details")
    print("--------------------------")


    print("----- Customer Number 00{} -----".format(input_details[0]))
    print("----- {} -----".format(input_details[1]))
    print("Customer's First and Last Name: {}".format(' '.join(input_details[2])))
    print("Delivery Date: IdkLOL too hard..")
    print("Customer Phone Number: {}".format(input_details[3]))

    print("--------------------------")
    print("Donut Orders")
    print("--------------------------")
    for num in range(len(donut_type_details)):
        print("Order for {} donuts".format(donut_type_details[num][count]))
        while True:
            if count == 1:
                print("Total Cost: {}".format(donut_type_details[num][count]))
            elif count == 2:
                print("Amount: {}".format(donut_type_details[num][count]))
            elif count == 3:
                checker == 'finish'
                break
            count += 1
        count = 0
        print("--------------------------")
        
    print("---- Total Donut Cost: ${} ----".format(donut_total))
    print("--------------------------")
    print("Travel Fee($15) + Donut Cost(${})".format(donut_total))
    print("---- Total Cost: ${} ----".format(total_cost))

input_details = []
input_details, donut_type_details, donut_total = InputQuery(input_details, customer_num)
final_details = CalculateQuery(input_details, donut_total, donut_type_details)
