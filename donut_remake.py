
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog as sd
from tkinter import messagebox as mg

CHOCOLATE_PRICE = float(2.50)
CARAMEL_PRICE = float(2.50)
CINNAMON_PRICE = float(1.20)

msg = ""

def reset():
    global choc_count, caram_count, cinna_count, total_cost, choc_total, caram_total, cinna_total
    choc_count = 0
    caram_count = 0
    cinna_count = 0

    choc_total = 0
    caram_total = 0
    cinna_total = 0

    total_cost = 0
        
        
class DonutCalculator(ttk.Frame):
    
    def __init__(self, master, exit_program, *args, **kwargs):
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.root = master
        self.init_window()
    
    def exit_program(self):
        print("YEEET MY YAH")

    def calculate_first(self, donut, price, count):
        global msg
        sub_total = 0
        count += donut
        if count < 5:
            msg = "Minimum of 5 Donuts"
            judge = False
            return judge, sub_total
            
        elif count  >= 30:
            msg = "Maximum of 30 Donuts"
            judge = False
            return judge, sub_total
            
        elif count >= 5 or count <= 30:
            sub_total = donut * price
            judge = True
            self.grand_total_label['text'] = "${:.2f}".format(total_cost)
            return judge, sub_total
        
    def calculate(self):
        global choc_count, caram_count, cinna_count, total_cost, choc_total, caram_total, cinna_total  
        judge = 0
        total = 0
        donut1 = int(self.donut1_entry.get())
        if donut1 != 0:
            judge, total = self.calculate_first(donut1, CHOCOLATE_PRICE, choc_count)
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
            judge, total = self.calculate_first(donut2, CARAMEL_PRICE, caram_count)
            if judge == True:
                caram_count += donut2
                caram_total += total
                self.sub_total_label2a['text'] = "Success!- Currently {} Donuts".format(caram_count)
                self.sub_total_label2b['text'] = "${:.2f}".format(total)
            else:
                self.sub_total_label2a['text'] = msg
        else:
            if caram_count > 0:
                self.sub_total_label2a['text'] = "Current Donuts: {}".format(caram_count)
            else:
                self.sub_total_label2a['text'] = "No Donuts Ordered"
            
        donut3 = int(self.donut3_entry.get())
        if donut3 != 0:
            judge, total = self.calculate_first(donut3, CINNAMON_PRICE, cinna_count)
            if judge == True:
                cinna_count += donut3
                cinna_total += total
                self.sub_total_label3a['text'] = "Success!-Currently {} Donuts".format(cinna_count)
                self.sub_total_label3b['text'] = "${:.2f}".format(total)
            else:
                self.sub_total_label3a['text'] = msg
        else:
            if cinna_count > 0:
                self.sub_total_label3a['text'] = "Current Donuts: {}".format(cinna_count)
            else:
                self.sub_total_label3a['text'] = "No Donuts Ordered"
        

        self.donut1_entry.set(0)
        self.donut2_entry.set(0)
        self.donut3_entry.set(0)
        
        if choc_count > 0 or caram_count > 0 or cinna_count > 0:
            self.message_label['text'] = "Ready to Write to order_book.txt"
            self.grand_total_label['text'] = "${:.2f}".format(choc_total + caram_total + cinna_total)

            
        

    def init_window(self):
        reset()
        self.root.title('Donut Order Calculator')
        self.root.option_add('*tearOff', 'FALSE')
        self.grid(column=0, row=0, sticky='nsew')

        # Separator helps order the info on the GUI -------------------------------------
        ttk.Separator(self, orient='horizontal').grid(column=0,row=2, columnspan=8, sticky='we')
        ttk.Separator(self, orient='vertical').grid(column=1,row=2, rowspan=4, sticky='ns')
        ttk.Separator(self, orient='vertical').grid(column=3,row=2, rowspan=4, sticky='ns')
        # -------------------------------------------------------------------------------

        # Middle Button - command=lambda: self.calculate("Chocolate Donuts")
        self.calculate_button = ttk.Button(self, text='Calculate', command=self.calculate)
        self.calculate_button.grid(column=0, row=7, columnspan=3)
        
        self.finish_button = ttk.Button(self, text='Process Orders')
        self.finish_button.grid(column=1, row=7, columnspan=3)

        self.calc_button = ttk.Button(self, text='Exit', command=self.exit_program)
        self.calc_button.grid(column=2, row=7, columnspan=3)
        
        # Message Label to inform user to use correct data type -------------------------
        self.message_frame = ttk.LabelFrame(self, text='Output',height=100)
        self.message_frame.grid(column=0, row=8, columnspan=8, sticky='nesw')
 
        self.message_label = ttk.Label(self.message_frame, text="No Action Detected")
        self.message_label.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Chocolate Donut Input ---------------------------------------------------------
        self.donut1_entry = ttk.Spinbox(self, from_=0, to=30, state='readonly')
        self.donut1_entry.set(0)
        self.donut1_entry.grid(column=0, row=4)
        
        self.sub_total_frame1a = ttk.LabelFrame(self, text='Output',height=100)
        self.sub_total_frame1a.grid(column=0, row=5, columnspan=1, sticky='esw')

        self.sub_total_label1a = ttk.Label(self.sub_total_frame1a, text='None')
        self.sub_total_label1a.grid(column=0, row=0)

        self.sub_total_frame1b = ttk.LabelFrame(self, text='Sub Total',height=100)
        self.sub_total_frame1b.grid(column=0, row=6, columnspan=1, stick='esw')

        self.sub_total_label1b = ttk.Label(self.sub_total_frame1b, text='0')
        self.sub_total_label1b.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Caramel Donut Input -----------------------------------------------------------
        self.donut2_entry = ttk.Spinbox(self, from_=0, to=30, state='readonly')
        self.donut2_entry.set(0)
        self.donut2_entry.grid(column=2, row=4)

        self.sub_total_frame2a = ttk.LabelFrame(self, text='Output',height=100)
        self.sub_total_frame2a.grid(column=2, row=5, columnspan=1, sticky='esw')

        self.sub_total_label2a = ttk.Label(self.sub_total_frame2a, text='None')
        self.sub_total_label2a.grid(column=0, row=0)

        self.sub_total_frame2b = ttk.LabelFrame(self, text='Sub Total',height=100)
        self.sub_total_frame2b.grid(column=2, row=6, columnspan=1, sticky='esw')

        self.sub_total_label2b = ttk.Label(self.sub_total_frame2b, text='0')
        self.sub_total_label2b.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Cinnamon Donut Input ----------------------------------------------------------
        self.donut3_entry = ttk.Spinbox(self, from_=0, to=30, state='readonly')
        self.donut3_entry.set(0)
        self.donut3_entry.grid(column=4, row=4)
        
        self.sub_total_frame3a = ttk.LabelFrame(self, text='Output',height=100)
        self.sub_total_frame3a.grid(column=4, row=5, columnspan=1, sticky='esw')

        self.sub_total_label3a = ttk.Label(self.sub_total_frame3a, text='None')
        self.sub_total_label3a.grid(column=0, row=0)

        self.sub_total_frame3b = ttk.LabelFrame(self, text='Sub Total',height=100)
        self.sub_total_frame3b.grid(column=4, row=6, columnspan=1, sticky='esw')

        self.sub_total_label3b = ttk.Label(self.sub_total_frame3b, text='0')
        self.sub_total_label3b.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Total Cost Output -------------------------------------------------------------
        self.grand_total_frame = ttk.LabelFrame(self, text='Total Cost',height=100)
        self.grand_total_frame.grid(column=0, row=9, columnspan=8, sticky='nesw')
 
        self.grand_total_label = ttk.Label(self.grand_total_frame, text='0')
        self.grand_total_label.grid(column=0, row=0)
        # -------------------------------------------------------------------------------
        
        ttk.Label(self, text='Donut Order Checker').grid(column=0, row=0, columnspan=8)
        ttk.Label(self, text='Max Order per donut type is 30, Min is 5 - Leave Blank if zero donuts is ordered').grid(column=0, row=1, columnspan=8)
        ttk.Label(self, text='Chocolate Donuts - ${:.2f} each'.format(CHOCOLATE_PRICE)).grid(column=0, row=3, columnspan=1)
        ttk.Label(self, text='Caramel Donuts - ${:.2f} each'.format(CARAMEL_PRICE)).grid(column=2, row=3, columnspan=1)
        ttk.Label(self, text='Cinnamon Donuts - ${:.2f} each'.format(CINNAMON_PRICE)).grid(column=4, row=3, columnspan=1)

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)
    

if __name__ == '__main__':
    root = tk.Tk()
    gui = DonutCalculator(root, "")
    root.mainloop()
    
