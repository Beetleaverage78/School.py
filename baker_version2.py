import datetime as dt

COOKIES_PRICE = 16.20
CUPCAKES_PRICE = 21
CAKE_PRICE = 59.50

cookie_cupcake_max = 10
cake_max = 5

SET_DATE = dt.datetime.now()
print("--------------------")
print("{} - {}".format(SET_DATE.strftime("%D"), SET_DATE.strftime("%A")))
print("--------------------")

def systemMain():
    customer_name = []
    total_cost = 0
    save_order = []
    progress = True
    while progress == True:
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
            order_list = []
            order_count = {}
            sub_total = []
            local_order = []
            while True:
                try:
                    print("Enter either Cookies(1) Cupcakes(2) Cake(3)")
                    print("In the order of 1 2 3")
                    order_list = input("What was ordered?: ").split()
                    if order_list == ['1'] or order_list == ['1', '2'] or order_list == ['1', '3'] or order_list == ['1', '2', '3'] or order_list == ['2'] or order_list == ['2', '3'] or order_list == ['3']:
                        break
                    else:
                        raise ValueError
                        
                except ValueError:
                    order_list = []
                    print("Thats not 1, 2, or 3.")
                    
            def MaxMinOrder(msg, maximum):
                while True:
                    try:
                        owner_input = int(input(msg))
                        if owner_input <= maximum and owner_input != 0:
                            return owner_input
                        elif owner_input > maximum:
                            print("That is greater than {}".format(maximum))
                        else:
                            raise ValueError
                            
                    except ValueError:
                        owner_input = 0
                        print("That is not a number")
                
            for order in order_list:
                if order == '1':
                    owner_input = "Quantity of Cookie Packs(${0:.2f} pack): ".format(COOKIES_PRICE)
                    owner_input = MaxMinOrder(owner_input, cookie_cupcake_max)
                    cost = round(owner_input * COOKIES_PRICE)
                    order_count["Cookies Pack"] = [owner_input, cost]
                    
                elif order == '2':
                    owner_input = "Quantity of Cupcakes Packs(${0:.2f} each): ".format(CUPCAKES_PRICE)
                    owner_input = MaxMinOrder(owner_input, cookie_cupcake_max)
                    cost = round(owner_input * CUPCAKES_PRICE)
                    order_count["Cupcakes Pack"] = [owner_input, cost]
                    
                elif order == '3':
                    owner_input = "Quantity of Cakes(${0:.2f} each): ".format(CAKE_PRICE)
                    owner_input = MaxMinOrder(owner_input, cake_max)
                    cost = round(owner_input * CAKE_PRICE)
                    order_count["Cakes"] = [owner_input, cost]

            local_order.append(customer_name)
            print("======================")
            print("Current Order Details")
            print("----------------------")
            for goods, amount in order_count.items():
                local_order.append([goods, amount[0], amount[1]])
                sub_total.append(amount[1])
                print("Order for {}".format(goods))
                print("Amount: {}".format(amount[0]))
                print("Sub Total: ${0:.2f}".format(amount[1]))
                print("======================")
            save_order.append(local_order)
            
        except StopIteration:
            pass
        
        finally:
            print("Grand Total")
            print("-------------------")
            print(save_order)
            print("-------------------")
            total_cost += sum(sub_total, 10)
            print("Total Cost + $10 Travel Fee: ${0:.2f}".format(total_cost))
            print("======================")
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
                    
        if progress == False:
            order_file = open("order_book.txt", "a")
            order_file.write("====================================")
            order_file.write("\n{} - {} Order Details".format(SET_DATE.strftime("%D"), SET_DATE.strftime("%A")))
            order_file.write("\n[BakedGoods][Amount][SubCost]")
            order_file.write("\n------------------------------------\n")
            for name in save_order:
                count = 0
                while True:
                    order_file.write("Order for: {}".format(name[0]))
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
                            
def systemAdmin():
    print("Local Bakery Calculator")
    print("----------------------")
    systemMain()
                
systemAdmin()
