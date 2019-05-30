import time 
import tkinter
from tkinter import ttk
from tkinter import messagebox as msg

CHOCOLATE_PRICE = float(2.50)
CARAMEL_PRICE = float(2.50)
CINNAMON_PRICE = float(1.20)


          
        
class DonutCalculator(ttk.Frame):
    global info
    info = "No action"
    def __init__(self, master, goodbye, *args, **kwargs):
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.root = master
        self.init_window()
        self.goodbye = "Goodbye"

    def process(self):
        msg.showinfo("Test", "Some Message Box")
    
    def exit_prog(self):
        """Exits program."""
        print(self.goodbye)
        time.sleep(5)
        quit()
 
    def calculate(self):
        """Calculates the donut cost."""
        while True:
            try:
                donut1 = int(self.donut1_entry.get())
                donut2 = int(self.donut2_entry.get())
                donut3 = int(self.donut3_entry.get())
                print(donut1)
                if (donut1 >=5 and donut2 >= 5 and donut3 >= 5) and (donut1 < 30 and donut2 < 30 and donut3 < 30):
                    sub_total1 = donut1 * CHOCOLATE_PRICE
                    sub_total2 = donut2 * CARAMEL_PRICE
                    sub_total3 = donut3 * CINNAMON_PRICE
                    total = sub_total1 + sub_total2 + sub_total3
                    self.sub_total_label1['text'] = "${:.2f}".format(sub_total1)
                    self.sub_total_label2['text'] = "${:.2f}".format(sub_total2)
                    self.sub_total_label3['text'] = "${:.2f}".format(sub_total3)
                    self.grand_total_label['text'] = "${:.2f}".format(total)
                else:
                    raise ValueError or TypeError
                    
            except ValueError or TypeError:
                print("Oops incorrect data type")
                raise
            else:
                print("Ready to enter another number if needed")
                break
            finally:
                info = "Test"
                print("Read the reminder message")
                break
 
    def init_window(self):
        """Builds GUI."""
            

        
        self.root.title('Donut Order Calculator')
        self.root.option_add('*tearOff', 'FALSE')
        self.grid(column=0, row=0, sticky='nsew')

        # Menu ----------------------------------------
        self.menubar = tkinter.Menu(self.root)
        self.menu_file = tkinter.Menu(self.menubar)
        self.menu_file.add_command(label='Exit', command=self.exit_prog)
        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.root.config(menu=self.menubar)
        # ---------------------------------------------

        # Separator helps order the info on the GUI -------------------------------------
        ttk.Separator(self, orient='horizontal').grid(column=0,row=2, columnspan=8, sticky='we')
        ttk.Separator(self, orient='vertical').grid(column=1,row=2, rowspan=4, sticky='ns')
        ttk.Separator(self, orient='vertical').grid(column=3,row=2, rowspan=4, sticky='ns')
        # ttk.Separator(self, orient='horizontal').grid(column=0,row=6, columnspan=8, sticky='we')
        # -------------------------------------------------------------------------------

        # Middle Buttons
        self.exit_button = ttk.Button(self, text='Calculate', command=self.calculate)
        self.exit_button.grid(column=0, row=6, columnspan=3)

        self.finish_button = ttk.Button(self, text='Process Orders', command=self.process)
        self.finish_button.grid(column=1, row=6, columnspan=3)
        
        self.calc_button = ttk.Button(self, text='Exit', command=self.exit_prog)
        self.calc_button.grid(column=2, row=6, columnspan=7)
        
        # Message Label to inform user to use correct data type -------------------------
        self.message_frame = ttk.LabelFrame(self, text='Output',height=100)
        self.message_frame.grid(column=0, row=7, columnspan=8, sticky='nesw')
 
        self.message_label = ttk.Label(self.message_frame, text=info)
        self.message_label.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Chocolate Donut Input ---------------------------------------------------------
        default = tkinter.DoubleVar(value=0)
        self.donut1_entry = tkinter.Spinbox(self, from_=0, to=30, textvariable=default, state='readonly')
        self.donut1_entry.grid(column=0, row=4)
        
        self.sub_total_frame1 = ttk.LabelFrame(self, text='Sub Total',height=100)
        self.sub_total_frame1.grid(column=0, row=5, columnspan=1, sticky='we')

        self.sub_total_label1 = ttk.Label(self.sub_total_frame1, text='0')
        self.sub_total_label1.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Caramel Donut Input -----------------------------------------------------------
        self.donut2_entry = ttk.Entry(self, width=5)
        self.donut2_entry.insert(0, 0)
        self.donut2_entry.grid(column=2, row=4)

        self.sub_total_frame2 = ttk.LabelFrame(self, text='Sub Total',height=100)
        self.sub_total_frame2.grid(column=2, row=5, columnspan=1, sticky='we')

        self.sub_total_label2 = ttk.Label(self.sub_total_frame2, text='0')
        self.sub_total_label2.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        # Cinnamon Donut Input ----------------------------------------------------------
        self.donut3_entry = ttk.Entry(self, width=5)
        self.donut3_entry.insert(0, 0)
        self.donut3_entry.grid(column=4, row=4)
        
        self.sub_total_frame3 = ttk.LabelFrame(self, text='Sub Total',height=100)
        self.sub_total_frame3.grid(column=4, row=5, columnspan=1, sticky='we')

        self.sub_total_label3 = ttk.Label(self.sub_total_frame3, text='0')
        self.sub_total_label3.grid(column=0, row=0)
        # -------------------------------------------------------------------------------
        
        # Total Cost Output -------------------------------------------------------------
        self.grand_total_frame = ttk.LabelFrame(self, text='Total Cost',height=100)
        self.grand_total_frame.grid(column=0, row=8, columnspan=8, sticky='nesw')
 
        self.grand_total_label = ttk.Label(self.grand_total_frame, text='0')
        self.grand_total_label.grid(column=0, row=0)
        # -------------------------------------------------------------------------------

        
        ttk.Label(self, text='Donut Order Checker').grid(column=0, row=0, columnspan=8)
        ttk.Label(self, text='Max Order per donut type is 30, Min is 5').grid(column=0, row=2, columnspan=8)
        ttk.Label(self, text='Chocolate Donut Quantity').grid(column=0, row=3, sticky='e')
        ttk.Label(self, text='Caramel Donut Quantity').grid(column=2, row=3, sticky='w')
        ttk.Label(self, text='Cinnamon Donut Quantity').grid(column=4, row=3, sticky='w')
         

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)



 
if __name__ == '__main__':
    root = tkinter.Tk()
    tkinter.Label(root, text="First").grid(row=0)
    gui1 = DonutCalculator(root, "")
    root.mainloop()
    
