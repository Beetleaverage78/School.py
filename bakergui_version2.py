import datetime as dt
import baker_calculator as bc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mg

COOKIES_PRICE = float(16.20)
CUPCAKES_PRICE = float(21)
CAKE_PRICE = float(59.50)

COOKIES_MAX = 10
CUPCAKES_MAX = 10
CAKE_MAX = 5

date = dt.datetime.now()
bc.start()

class DonutGui(tk.Frame):
    def __init__(self, master, exit_program, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.root = master
        self.init_window()

    def variables(self):
        print("Variables Initialised")
        global cookies_count, cookies_total, cupcakes_count, cupcakes_total, cakes_count, cakes_total, var1, var2, var3
        cookies_count = 0
        cookies_total = 0

        cupcakes_count = 0
        cupcakes_total = 0

        cakes_count = 0
        cakes_total = 0

        var1 = tk.IntVar(root)
        var2 = tk.IntVar(root)
        var3 = tk.IntVar(root)
        
        var1.set(0)
        var2.set(0)
        var3.set(0)

    def reset(self):
        check = mg.askyesno("Reset", "Do you want to reset the program")
        if check == True:
            self.init_window()
        else:
            mg.showinfo("Cancelled", "Okay, program will resume")

    def exit(self):
        quit()

    def process_orders(self):
        check = mg.askyesno('Final Orders?', "Is this the final order?")
        if check == True:
            pass
        else:
            return
        while True:
            fname = self.fname_entry.get()
            lname = self.lname_entry.get()
            judge, msg = bc.name_method(fname, lname)
            if judge == True:
                mg.showinfo('Successful', msg)
                break
            elif judge == False:
                mg.showerror('Invalid Name', msg)
                return
            else:
                mg.showerror('Missing Values', msg)
                return
        orders = {}
        orders['Cookies'] = [cookies_count, round(cookies_total)]
        orders['Cupcakes'] = [cupcakes_count, round(cupcakes_total)]
        orders['Cakes'] = [cakes_count, round(cakes_total)]
        mg.showinfo('Order Details', orders)
        mg.showinfo('Resetting', "Program will now reset to prepare for another order")
        self.init_window()
                             
    def calculate(self):
        global cookies_count, cookies_total, cupcakes_count, cupcakes_total, cakes_count, cakes_total, total_cost
        judge = 0
        total = 0
        total_cost = 0
        
        cookies = int(var1.get())
        if cookies != 0:
            judge, total = bc.calculate_method(cookies, COOKIES_PRICE, cookies_count, COOKIES_MAX)
            if judge == True:
                cookies_count += cookies
                cookies_total += total
                self.cookies_sub_label['text'] = "${:.2f}".format(cookies_total)
            else:
                mg.showerror('Invalid Input', "That is more than 10 Cookie packs, You are trying to order {} more, When you have already {}".format(cookies, cookies_count))
        else:
            if cookies_count > 0:
                self.cookies_sub_label['text'] = "${:.2f}".format(cookies_total)
        cupcakes = int(var2.get())
        if cupcakes != 0:
            judge, total = bc.calculate_method(cupcakes, CUPCAKES_PRICE, cupcakes_count, CUPCAKES_MAX)
            if judge == True:
                cupcakes_count += cupcakes
                cupcakes_total += total
                self.cupcakes_sub_label['text'] = "${:.2f}".format(cupcakes_total)
            else:
                mg.showerror('Invalid Input', "That is more than 10 Cupcake packs, You are trying to order {} more, When you have already ordered {}".format(cupcakes, cupcakes_count))
        else:
            if cupcakes > 0:
                self.cupcakes_sub_label['text'] = "${:.2f}".format(cupcakes_total)
        cakes = int(var3.get())
        if cakes != 0:
            judge, total = bc.calculate_method(cakes, CAKE_PRICE, cakes_count, CAKE_MAX)
            if judge == True:
                cakes_count += cakes
                cakes_total += total
                self.cakes_sub_label['text'] = "${:.2f}".format(cakes_total)
                self.cake_label['text'] = "Cakes: {}".format(cakes)
            else:
                mg.showerror('Invalid Input', "That is more than 5 Cakes, You are trying to order {} more, When you have already ordered {}".format(cakes, cakes_count))
        else:
            if cakes > 0:
                self.cakes_sub_label['text'] = "${:.2f}".format(cakes_total)
            
        var1.set(0)
        var2.set(0)
        var3.set(0)

        if cookies > 0 or cupcakes > 0 or cakes > 0:
            self.process_button['state'] = 'normal'
            total_cost = cookies_total + cupcakes_total + cakes_total + 10
            self.total_label['text'] = "${:.2f}".format(total_cost)
            self.output_frame['text'] = "Output: Successful Calculation"
        else:
            self.output_frame['text'] = "Output: No Orders were made"
            mg.showinfo("Zero Orders", "No Orders were made")
            
    def init_window(self):
        self.variables()
        global var1, var2, var3
        __order_quantity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        __cake_quantity = [0, 1, 2, 3, 4, 5]

        # Window Title ---------------------------
        self.root.title("Bakery Order Calculator")
        self.grid(column=0, row=0, sticky='nsew')
        # ----------------------------------------

        # Separators ---------------------------------------------------------------------------
        ttk.Separator(self, orient='horizontal').grid(column=0, row=3, columnspan=9, sticky='we')
        ttk.Separator(self, orient='horizontal').grid(column=0, row=7, columnspan=9, sticky='we')
        # --------------------------------------------------------------------------------------

        # Main Buttons --------------------------------------------------------
        self.reset_button = tk.Button(self, text='Reset', command=self.reset)
        self.reset_button.grid(column=2, row=1, columnspan=1, sticky='we')
        
        self.exit_button = tk.Button(self, text='Exit', command=self.exit)
        self.exit_button.grid(column=5, row=1, columnspan=1, sticky='we')
        
        self.process_button = tk.Button(self, text='Process Orders', state='disabled', command=self.process_orders)
        self.process_button.grid(column=0, row=9, sticky='we')

        self.calculate_button = tk.Button(self, text='Calculate', command=self.calculate)
        self.calculate_button.grid(column=1, row=9, columnspan=5, sticky='we')
        # -----------------------------------------------------------------------
        
        # Output & Total Cost ----------------------------------------------
        self.output_frame = tk.LabelFrame(self, text='Output: No Orders were Made', bd='2px')
        self.output_frame.grid(column=0, row=10, columnspan=8, sticky='nesw')

        self.cookie_pack_label = tk.Label(self.output_frame, text='Cookie Packs: 0')
        self.cookie_pack_label.grid(column=0, row=1, sticky='w')

        self.cupcake_pack_label = tk.Label(self.output_frame, text='Cupcake Packs: 0')
        self.cupcake_pack_label.grid(column=1, columnspan=2, row=1, sticky='w')

        self.cake_label = tk.Label(self.output_frame, text='Cakes: 0')
        self.cake_label.grid(column=4, row=1, sticky='we')

        self.total_frame = tk.LabelFrame(self, text='Total Cost', bd='2px')
        self.total_frame.grid(column=0, row=13, columnspan=8, sticky='nesw')
        
        self.total_label = tk.Label(self.total_frame, text='$0.00')
        self.total_label.grid(column=0, row=0)
        # ------------------------------------------------------------------

        # Customer Details ------------------------------------------------------------
        self.customer_frame = tk.LabelFrame(self, text='Customer Details', bd='2px', height=100)
        self.customer_frame.grid(column=0, row=1, columnspan=1, sticky='esw')

        self.fname_label = tk.Label(self.customer_frame, text='First Name')
        self.fname_label.grid(column=1, row=1)

        self.fname_entry = tk.Entry(self.customer_frame)
        self.fname_entry.grid(column=2, row=1)

        self.lname_label = tk.Label(self.customer_frame, text='Last Name')
        self.lname_label.grid(column=1, row=2)

        self.lname_entry = tk.Entry(self.customer_frame)
        self.lname_entry.grid(column=2, row=2)
        # -----------------------------------------------------------------------------

        # Cookies Input ---------------------------------------------------------------
        self.cookies_entry = tk.OptionMenu(self, var1, *__order_quantity)
        self.cookies_entry.grid(column=1, row=4, columnspan=4, sticky='we')
        
        self.cookies_sub_frame = tk.LabelFrame(self, text='Sub Total')
        self.cookies_sub_frame.grid(column=5, row=4, sticky='we')

        self.cookies_sub_label = tk.Label(self.cookies_sub_frame, text='$0.00')
        self.cookies_sub_label.grid(column=0, row=0)
        # -----------------------------------------------------------------------------

        # Cupcakes Input --------------------------------------------------------------
        self.cupcakes_entry = tk.OptionMenu(self, var2, *__order_quantity)
        self.cupcakes_entry.grid(column=1, row=5, columnspan=4, sticky='we')
        
        self.cupcakes_sub_frame = tk.LabelFrame(self, text='Sub Total')
        self.cupcakes_sub_frame.grid(column=5, row=5, columnspan=1, sticky='we')

        self.cupcakes_sub_label = tk.Label(self.cupcakes_sub_frame, text='$0.00')
        self.cupcakes_sub_label.grid(column=0, row=0)
        # -----------------------------------------------------------------------------

        # Cakes Input -----------------------------------------------------------------
        self.cakes_entry = tk.OptionMenu(self, var3, *__cake_quantity)
        self.cakes_entry.grid(column=1, row=6, columnspan=4, sticky='we')
        
        self.cakes_sub_frame = tk.LabelFrame(self, text='Sub Total', height=100)
        self.cakes_sub_frame.grid(column=5, row=6, columnspan=1, sticky='we')

        self.cakes_sub_label = tk.Label(self.cakes_sub_frame, text='$0.00')
        self.cakes_sub_label.grid(column=0, row=0)
        # -----------------------------------------------------------------------------

        # Initialise Labels -----------------------------------------------------------------------------------------------------------
        tk.Label(self, text="{} {} {} - {}".format(date.strftime("%d"), date.strftime("%B"), date.strftime("%Y"), date.strftime("%I:%M %p"))).grid(column=0, row=0, columnspan=8)
        tk.Label(self, text='Max Order is [] - Minimum is []').grid(column=0, row=3, columnspan=8)
        tk.Label(self, text='Cookie Pack of 12 - ${:.2f} each pack'.format(COOKIES_PRICE)).grid(column=0, row=4, columnspan=1, sticky='w')
        tk.Label(self, text='Cupcake Pack of 6- ${:.2f} each pack'.format(CUPCAKES_PRICE)).grid(column=0, row=5, columnspan=1, sticky='w')
        tk.Label(self, text='Single Cake - ${:.2f} each'.format(CAKE_PRICE)).grid(column=0, row=6, columnspan=1, sticky='w')
        # -----------------------------------------------------------------------------------------------------------------------------

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)



if __name__ == '__main__':
    while True:
        root = tk.Tk()
        gui = DonutGui(root, "")
        root.mainloop()
        
