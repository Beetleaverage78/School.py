import datetime as dt
#=============================
# Initialise Variables
#=============================
COOKIES_PRICE = 16.20
CUPCAKES_PRICE = 21
CAKE_PRICE = 59.50
TRAVEL_FEE = 10

cookie_max = 10
cupcake_max = 10
cake_max = 5

SET_DATE = dt.datetime.now()
print("--------------------")
print("{} - {}".format(SET_DATE.strftime("%D"), SET_DATE.strftime("%A")))
print("--------------------")
#=============================

def max_min_order(msg, maximum, price):
    #==================================================================
    # Max and Min Order Function - Processes quantity of baked products
    #==================================================================
    while True:
        try:
            owner_input = 0
            print("Maximum: {} Min: 0".format(maximum))
            owner_input = int(input(msg))
            if owner_input <= maximum and owner_input != 0 and owner_input > 0:
                amount_cost = round(owner_input * price)
                print("-------------------")
                return owner_input, amount_cost
            elif owner_input > maximum:
                print("That is greater than {}".format(maximum))
            else:
                raise ValueError
                            
        except ValueError:
            print("That is not a number")
                        
def system_main():
    #=============================
    # Main Code of Program
    #=============================
    customer_name = []
    total_cost = 0
    save_order = []
    progress = True
    # Main While Loop - Until owner decides to stop entering orders
    #==================================================================
    while progress == True:
        # Customer First & Last Name Input Block
        while True:
            owner_input = str(input("Customer First & Last Name: "))
            if all(x.isalpha() or x.isspace() for x in owner_input):
                customer_name = owner_input
                print("--------------------")
                print("Order for {}".format(customer_name))
                break
            else:
                print("That does not look like a name at all. Required Format (e.g. Ellan Bugas)")
        try:
            # Order Type Input Block - Whether the order consists of Cookies or Cupcakes or Cakes
            order_list = []
            order_count = {}
            sub_total = []
            local_order = []
            type_count = {'Cookies': 1, 'Cupcakes': 1, 'Cakes': 1}
            while True:
                try:
                    print("Enter either Cookies(1) Cupcakes(2) Cake(3)")
                    compare = ['1', '2', '3']
                    print("In the order of 1 2 3 - As long as its one of these numbers.")
                    order_list = input("What was ordered?: ").split()
                    print("-------------------")
                    if any({*order_list} & {*compare}) and len(order_list) <= 3:
                        break
                    else:
                        raise ValueError
                        
                except ValueError:
                    order_list = []
                    print("Thats not 1, 2, or 3.")
                    print("--------------------")
            
            # Processes each order and Calls MaxMinOrder() function
            # - For loop with Conditional Statements to check orders input is '1','2','3',
            for order in order_list:
                if order == '1' and type_count.get('Cookies') == 1:
                    owner_input = "Quantity of Cookie Packs(${0:.2f} pack): ".format(COOKIES_PRICE)
                    owner_input, cost = max_min_order(owner_input, cookie_max, COOKIES_PRICE)
                    order_count["Cookies Pack"] = [owner_input, cost]
                    type_count['Cookies'] = 2
                    
                elif order == '2' and type_count.get('Cupcakes') == 1:
                    owner_input = "Quantity of Cupcakes Packs(${0:.2f} each): ".format(CUPCAKES_PRICE)
                    owner_input, cost = max_min_order(owner_input, cupcake_max, CUPCAKES_PRICE)
                    order_count["Cupcakes Pack"] = [owner_input, cost]
                    type_count['Cupcakes'] = 2
                    
                elif order == '3' and type_count.get('Cakes') == 1:
                    owner_input = "Quantity of Cakes(${0:.2f} each): ".format(CAKE_PRICE)
                    owner_input, cost = max_min_order(owner_input, cake_max, CAKE_PRICE)
                    order_count["Cakes"] = [owner_input, cost]
                    type_count['Cakes'] = 2

            # Show Owner Current Order Details
            local_order.append(customer_name)
            print("----------------------")
            print("Current Order Details")
            print("======================")
            for goods, amount in order_count.items():
                local_order.append([goods, amount[0], amount[1]])
                sub_total.append(amount[1])
                print("Order for {}".format(goods))
                print("Amount: {}".format(amount[0]))
                print("Sub Total: ${0:.2f}".format(amount[1]))
                print("======================")
            save_order.append(local_order)
            
        except StopIteration:
            # Except Block - Used in Next Standard
            pass
        
        finally:
            # Show Owner Total_Cost with Travel_Fee and All Orders
            print("Grand Total")
            print("-------------------")
            total_cost += sum(sub_total, TRAVEL_FEE)
            print("Total Cost + ${0:.2f} Travel Fee = ${1:.2f}".format(TRAVEL_FEE, total_cost))
            print("======================")
            # Repeat Program Block - If necessary, owner can input another order without exiting.
            while True:
                print("Do you want to enter another order?")
                owner_input = input("Yes/No: ")
                if owner_input == 'Yes' or owner_input == 'yes':
                    print("-------------------")
                    print("Resetting Variables - Total_Cost and Sub_Total is saved")
                    print("-------------------")
                    break
                elif owner_input == 'No' or owner_input == 'no':
                    print("-------------------")
                    print("Alright..")
                    print("Order Details Imported to order_book.txt - {}".format(SET_DATE.strftime("%D")))
                    progress = False
                    break
                else:
                    owner_input = 0
                    print("That is neither Yes or No, please try Again")

        # Write Order Details - When progress is False, write to order_book.txt and exit           
        if progress == False:
            order_file = open("order_book.txt", "a")
            order_file.write("====================================")
            order_file.write("\n{} - {} Order Details".format(SET_DATE.strftime("%D"), SET_DATE.strftime("%A")))
            order_file.write("\n------------------------------------\n")
            for name in save_order:
                count = 0
                while True:
                    order_file.write("Order for: {}".format(name[0]))
                    order_file.write("\n[BakedGoods][Amount][SubCost]")
                    for i in range(len(name)):
                        if i != count:
                            break
                        else:
                            if count != 0:
                                order_file.write("\n{}".format(name[count]))
                        count += 1
                    break
                order_file.write("\n------------------------------------\n")      
            order_file.write("Total Cost of Orders + Travel Fee = ${}".format(total_cost))
            order_file.write("\n------------------------------------\n")
            order_file.close()
        #==================================================================

# Main routine
if __name__ == "__main__":
    # Call systemMain() Function
    print("Local Bakery Calculator")
    print("----------------------")
    system_main()
