cookie_max = 10
cupcake_max = 10
cake_max = 5


def start():
    print("Baker Method Imported Successfully")

def calculate_method(order, price, count):
    print("------------------------------------------------------")
    print("Order Requested - Checking Maximum and Minimum orders")
    print("------------------------------------------------------")
    sub_total = 0
    count += order
    if price != 59.50:
        if count <= 0:
            judge = False
            return judge, sub_total
        elif count > 10:
            judge = False
            sub_total = count * price
            return judge, sub_total
        elif count > 0:
            judge = True
            sub_total = count * price
            return judge, sub_total
    elif price == 59.50:
        if count <= 0:
            judge = False
            return judge, sub_total
        elif count > 5:
            judge = False
            sub_total = count * price
            return judge, sub_total
        elif count > 0:
            judge = True
            sub_total = count * price
            return judge, sub_total
