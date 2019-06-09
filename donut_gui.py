import sys
import donut_calculator as dc
import time as t
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog as sd
from tkinter import messagebox as mg

CHOCOLATE_PRICE = float(2.50)
CARAMEL_PRICE = float(2.50)
CINNAMON_PRICE = float(1.20)

msg = ""
dc.display()
class DonutCalculator(ttk.Frame):
    
    def __init__(self, master, exit_program, *args, **kwargs):
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.root = master
        self.init_window()

    def reset(self):
        global choc_count, caram_count, cinna_count, total_cost, choc_total, caram_total, cinna_total, var1, var2, var3
        choc_count = 0
        caram_count = 0
        cinna_count = 0

        choc_total = 0
        caram_total = 0
        cinna_total = 0

        total_cost = 0

        var1 = tk.DoubleVar(value=0)
        var2 = tk.DoubleVar(value=0)
        var3 = tk.DoubleVar(value=0)
        
    def exit_program(self):
        print("YEEET MY YAH")
        quit()

    def process_orders(self):
        f_name = self.first_name_entry.get()
        l_name = self.last_name_entry.get()

        f_name, l_name = dc.customer_details(f_name, l_name)
        if f_name != False and l_name != False:
            check = mg.askyesno("Process Orders", "Is this the final order?")
            if check == True:
                self.finish_button['state'] = 'disabled'
                self.calculate_button['state'] = 'disabled'
                t.sleep(1)    
                self.message_label['text'] ="""Order Details Written to File\n--------------------------------\nCheck Terminal behind this Window"""

                if choc_count > 0:
                    donut = 'Chocolate'
                    choc_list = dc.save_orders(donut, choc_count, choc_total)
                else:
                    print("No Chocolate Donuts Ordered")
                    print("---------------------")
                    choc_list = 'No Chocolate Donuts Ordered'
                    
                if caram_count > 0:
                    donut = 'Caramel Donuts'
                    caram_list = dc.save_orders(donut, caram_count, caram_total)
                else:
                    print("No Caramel Donuts Ordered")
                    print("---------------------")
                    caram_list = 'No Caramel Donuts Ordered'
                    
                if cinna_count > 0:
                    donut = 'Cinnamon'
                    cinna_list = dc.save_orders(donut, cinna_count, cinna_total)
                else:
                    cinna_list = 'No Cinnamon Donuts'
                    print("No Cinnamon Donuts Ordered")
                    print("---------------------")

                print("=================================")
                print("Program has been Reset")
                self.quit()
                mg.showinfo('Final Order Details', "Orders For: {} {} \n---------------------------\n{}, \n{}, \n{} \n---------------------------".format(f_name, l_name, choc_list, caram_list, cinna_list))
                mg.showinfo('Order Details Saved', "The program has been reset, the order details were saved into [place filename].txt, you can enter another order or click Exit")
            else:
                return
        elif f_name == False:
            mg.showerror('Invalid Input', "First Name is not a Valid Name ")
        elif l_name == False:
            mg.showerror('Invalid Input', "Last Name is not a Valid Name")
        
    def calculate(self):
        global choc_count, caram_count, cinna_count, total_cost, choc_total, caram_total, cinna_total, var1, var2, var3  
        msg = ""
        judge = 0
        total = 0
        donut1 = int(self.donut1_entry.get())
        if donut1 != 0:
            judge, total, msg = dc.calculate_method(self, donut1, CHOCOLATE_PRICE, choc_count, msg)
            if judge == True:
                choc_count += donut1
                choc_total += total
                self.sub_total_label1a['text'] = "Success!- Currently {} Donuts".format(choc_count)
                self.sub_total_label1b['text'] = "${:.2f}".format(choc_total)
            else:
                self.sub_total_label1a['text'] = msg
        else:
            if choc_count > 0:
                self.sub_total_label1a['text'] = "Current Donuts: {}".format(choc_count)
            else:
                self.sub_total_label1a['text'] = "No Donuts Ordered"
            
        donut2 = int(self.donut2_entry.get())
        if donut2 != 0:
            judge, total, msg = dc.calculate_method(self, donut2, CARAMEL_PRICE, caram_count, msg)
            if judge == True:
                caram_count += donut2
                caram_total += total
                self.sub_total_label2a['text'] = "Success!- Currently {} Donuts".format(caram_count)
                self.sub_total_label2b['text'] = "${:.2f}".format(caram_total)
            else:
                self.sub_total_label2a['text'] = msg
        else:
            if caram_count > 0:
                self.sub_total_label2a['text'] = "Current Donuts: {}".format(caram_count)
            else:
                self.sub_total_label2a['text'] = "No Donuts Ordered"
            
        donut3 = int(self.donut3_entry.get())
        if donut3 != 0:
            judge, total, msg = dc.calculate_method(self, donut3, CINNAMON_PRICE, cinna_count, msg)
            if judge == True:
                cinna_count += donut3
                cinna_total += total
                self.sub_total_label3a['text'] = "Success!-Currently {} Donuts".format(cinna_count)
                self.sub_total_label3b['text'] = "${:.2f}".format(cinna_total)
            else:
                self.sub_total_label3a['text'] = msg
        else:
            if cinna_count > 0:
                self.sub_total_label3a['text'] = "Current Donuts: {}".format(cinna_count)
            else:
                self.sub_total_label3a['text'] = "No Donuts Ordered"

        var1.set('0')
        var2.set('0')
        var3.set('0')
        
        if choc_count > 0 or caram_count > 0 or cinna_count > 0 and total != 0:
            self.message_label['text'] = "Ready to Write to [filename].txt"
            total_cost = choc_total + caram_total + cinna_total + 10
            self.grand_total_label['text'] = "${:.2f}".format(total_cost)
            self.finish_button['state'] = 'normal'
        else:
            self.message_label['text'] = "No orders were made"
            
    def init_window(self):
        self.reset()
        self.root.title('Donut Order Calculator')
        self.root.option_add('*tearOff', 'FALSE')
        self.grid(column=0, row=0, sticky='nsew')

        # Separator helps order the info on the GUI -------------------------------------
        ttk.Separator(self, orient='horizontal').grid(column=0,row=3, columnspan=9, sticky='we')
        ttk.Separator(self, orient='horizontal').grid(column=0,row=7, columnspan=9, sticky='we')
        # -------------------------------------------------------------------------------

        # Middle Button - command=lambda: self.calculate("Chocolate Donuts")
        self.finish_button = ttk.Button(self, text='Process Orders', command=self.process_orders, state='disabled')
        self.finish_button.grid(column=0, row=9, columnspan=1, sticky='we')
        
        self.calculate_button = ttk.Button(self, text='Calculate', command=self.calculate)
        self.calculate_button.grid(column=1, row=9, columnspan=2, sticky='nesw')

        self.calc_button = ttk.Button(self, text='Exit', command=self.exit_program)
        self.calc_button.grid(column=3, row=9, columnspan=2, sticky='we')
        
        # Message Label to inform user to use correct data type -------------------------
        self.message_frame = ttk.LabelFrame(self, text='Output',height=100)
        self.message_frame.grid(column=0, row=10, columnspan=8, sticky='nesw')
 
        self.message_label = ttk.Label(self.message_frame, text="No instructions called")
        self.message_label.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Total Cost Output -------------------------------------------------------------
        self.grand_total_frame = ttk.LabelFrame(self, text='Total Cost',height=100)
        self.grand_total_frame.grid(column=0, row=11, columnspan=8, sticky='nesw')
 
        self.grand_total_label = ttk.Label(self.grand_total_frame, text='0')
        self.grand_total_label.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Customer Name Input -----------------------------------------------------------
        self.customer_frame = ttk.LabelFrame(self, text='Customer Details', height=100)
        self.customer_frame.grid(column=0, row=1, columnspa=5, sticky='esw')

        self.first_name_label = ttk.Label(self.customer_frame, text='First Name')
        self.first_name_label.grid(column=1, row=1)
        
        self.first_name_entry = ttk.Entry(self.customer_frame)
        self.first_name_entry.grid(column=2, row=1)

        self.last_name_label = ttk.Label(self.customer_frame, text='Last Name')
        self.last_name_label.grid(column=1, row=2)

        self.last_name_entry = ttk.Entry(self.customer_frame)
        self.last_name_entry.grid(column=2, row=2)

        # -------------------------------------------------------------------------------

        # Chocolate Donut Input ---------------------------------------------------------
        self.donut1_entry = tk.Spinbox(self, from_=0, to=10, textvariable=var1, state='readonly')
        self.donut1_entry.grid(column=1, row=4)
        
        self.sub_total_frame1a = ttk.LabelFrame(self, text='Amount',height=100)
        self.sub_total_frame1a.grid(column=3, row=4, columnspan=3, sticky='nesw')

        self.sub_total_label1a = ttk.Label(self.sub_total_frame1a, text='None')
        self.sub_total_label1a.grid(column=0, row=0)

        self.sub_total_frame1b = ttk.LabelFrame(self, text='Sub Total',height=100)
        self.sub_total_frame1b.grid(column=2, row=4, columnspan=1, stick='esw')

        self.sub_total_label1b = ttk.Label(self.sub_total_frame1b, text='0')
        self.sub_total_label1b.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Caramel Donut Input -----------------------------------------------------------
        
        self.donut2_entry = tk.Spinbox(self, from_=0, to=10, textvariable=var2, state='readonly')
        self.donut2_entry.grid(column=1, row=5)

        self.sub_total_frame2a = ttk.LabelFrame(self, text='Amount',height=100)
        self.sub_total_frame2a.grid(column=3, row=5, columnspan=2, sticky='esw')

        self.sub_total_label2a = ttk.Label(self.sub_total_frame2a, text='None')
        self.sub_total_label2a.grid(column=0, row=0)

        self.sub_total_frame2b = ttk.LabelFrame(self, text='Sub Total',height=100)
        self.sub_total_frame2b.grid(column=2, row=5, columnspan=1, sticky='esw')

        self.sub_total_label2b = ttk.Label(self.sub_total_frame2b, text='0')
        self.sub_total_label2b.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Cinnamon Donut Input ----------------------------------------------------------

        self.donut3_entry = tk.Spinbox(self, from_=0, to=10, textvariable=var3, state='readonly')
        self.donut3_entry.grid(column=1, row=6)
        
        self.sub_total_frame3a = ttk.LabelFrame(self, text='Amount',height=100)
        self.sub_total_frame3a.grid(column=3, row=6, columnspan=2, sticky='esw')

        self.sub_total_label3a = ttk.Label(self.sub_total_frame3a, text='None')
        self.sub_total_label3a.grid(column=0, row=0)

        self.sub_total_frame3b = ttk.LabelFrame(self, text='Sub Total',height=100)
        self.sub_total_frame3b.grid(column=2, row=6, columnspan=1, sticky='esw')

        self.sub_total_label3b = ttk.Label(self.sub_total_frame3b, text='0')
        self.sub_total_label3b.grid(column=0, row=0)
        # -------------------------------------------------------------------------------
        
        ttk.Label(self, text='Donut Order Checker').grid(column=0, row=0, columnspan=8)
        ttk.Label(self, text='Max Order per donut type is 30 - Minimum is 5').grid(column=0, row=3, columnspan=8)
        ttk.Label(self, text='Chocolate Donuts - ${:.2f} each'.format(CHOCOLATE_PRICE)).grid(column=0, row=4, columnspan=1)
        ttk.Label(self, text='Caramel Donuts - ${:.2f} each'.format(CARAMEL_PRICE)).grid(column=0, row=5, columnspan=1)
        ttk.Label(self, text='Cinnamon Donuts - ${:.2f} each'.format(CINNAMON_PRICE)).grid(column=0, row=6, columnspan=1)

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)
    
if __name__ == '__main__':
    while True:
        root = tk.Tk()
        gui = DonutCalculator(root, "")
        root.mainloop()
        root.destroy()
