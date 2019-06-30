from tkinter import messagebox as mg
def start():
    print("Baker Method Imported Successfully")

def name_method(fname, lname):
    judge = 'missing'
    f_count = 0
    l_count = 0
    if fname == "" and lname != "":
        msg = "Missing Customer's First Name"
        return judge, msg
    elif lname == "" and fname != "":
        msg = "Missing Customer's Last Name"
        return judge, msg
    elif fname == "" and lname == "":
        msg = "Missing Customer's First & Last Name"
        return judge, msg
    mg.showinfo('Processing', "Processing Customer Details")
    print("-------Name Checking Intensifies----------")
    print("Checking Length of name is appropriate")
    if len(fname) < 2:
        judge = False
        msg = "First Name is too short, needs to be 2 or more characters long"
        return judge, msg
    elif len(lname) < 2:
        judge = False
        msg = "Last Name is too short, needs to be 2 or more characters long"
        return judge, msg
    
    print("Checking for Spaces")
    for letter in fname:
        if (letter.isspace()) == True:
            f_count += 1
    for letter in lname:
        if (letter.isspace()) == True:
            l_count += 1
    if f_count > 0 and l_count > 0:
        judge = False
        msg = "There are spaces in both the First & Last Name of the customer"
        return judge, msg
    elif f_count > 0:
        judge = False
        msg = "There are spaces in the First Name of the customer"
        return judge, msg
    elif l_count > 0:
        judge = False
        msg = "There are spaces in the Last Name of the customer"
        return judge, msg
    
    else:
        print("Checking if name is in the alphabet")
        if fname.isalpha() == True and lname.isalpha() == True:
            judge = True
            msg = "Valid Customer Details"
            print("-----Successful Name Checking------")
            return judge, msg
        elif fname.isalpha() == False and lname.isalpha() == False:
            judge = False
            msg = "First & Last Name is Invalid"
            return judge, msg
        elif fname.isdigit() or fname.isalpha() == False:
            judge = False
            msg = "First Name is Invalid"
            return judge, msg
        elif lname.isdigit() or lname.isalpha() == False:
            judge = False
            msg = "Last Name is Invalid"
            return judge, msg


def calculate_method(order, price, count, order_max):
    sub_total = 0
    count += order
    if count <= 0:
        judge = False
        return judge, sub_total
    elif count > order_max:
        judge = False
        sub_total = count * price
        return judge, sub_total
    elif count > 0:
        judge = True
        sub_total = count * price
        print("-----Successful Calculation----")
        return judge, sub_total
        
