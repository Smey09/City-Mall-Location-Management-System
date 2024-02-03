from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Features import ShopManagement
from time import strftime
import datetime as dt

from Entity import ShopInMall
from DataToStorageManagement import (
    SaveShopToStorage,
    LoadShopFromStorage,
    LoadSellerFromStorage,
)


class MainMenuGui:
    def __init__(self, root: Tk, data: list) -> None:
        self.root = root
        self._shopManagement = ShopManagement(data)

        lbig_title = Label(
            self.root,
            text="Mall Location Management system at Phnom Penh",
            font=("Times New Roman", 40, "bold"),
            background="yellow",
            foreground="MediumBlue",
        )
        # lbig_title.place(x=150, y=0)
        lbig_title.pack(anchor="center")

        date = dt.datetime.now()
        time_label = Label(
            root,
            text=f"{date:%A, %B %d, %Y}",
            font=("times", 20, "bold"),
            background="DeepSkyBlue",
            foreground="FireBrick",
        )
        time_label.place(x=740, y=55)

        def my_time():
            time_string = strftime("%H:%M:%S %p")  # time format
            hours.config(text=time_string)
            hours.after(1000, my_time)  # time delay of 1000 milliseconds

        hours = Label(
            root,
            font=("times", 20, "bold"),
            background="DeepSkyBlue",
            foreground="FireBrick",
        )
        hours.place(x=109, y=55)

        my_time()

        self.InitializeComponent()
        self.InitializeButton()
        self.InitializeTreeview()

        self.shopFloor_box.configure(state="disabled")
        self.shopSection_box.configure(state="disabled")
        self.shopSize_box.configure(state="disabled")
        self.rentalPrice_box.configure(state="disabled")

        self.add_btn.configure(state="normal")
        self.save_btn.configure(state="disabled")
        self.update_button.configure(state="disabled")
        self.delete_btn.configure(state="disabled")
        self.checkShop_btn.configure(state="disabled")

        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def InitializeComponent(self):
        self.add_frame = Frame(self.root, background="LightSalmon")
        # self.add_frame.pack(pady=20, padx=20)
        self.add_frame.place(x=135, y=83)

        # Label for ShoppingShop
        ShopID_Lbl = Label(
            self.add_frame, text="Shop ID", foreground="blue", background="lightgray"
        )
        ShopID_Lbl.grid(row=0, column=0)

        ShopFloor_Lbl = Label(
            self.add_frame, text="ជាន់ទី", foreground="blue", background="lightgray"
        )
        ShopFloor_Lbl.grid(row=0, column=1)

        ShopSection_Lbl = Label(
            self.add_frame, text="ផ្នែក", foreground="blue", background="lightgray"
        )
        ShopSection_Lbl.grid(row=0, column=2)

        ShopSize_Lbl = Label(
            self.add_frame,
            text="ទំហំ​ [(m) x (m)]",
            foreground="blue",
            background="lightgray",
        )
        ShopSize_Lbl.grid(row=0, column=3)

        RentalPrice_Lbl = Label(
            self.add_frame, text="តម្លៃជួល", foreground="blue", background="lightgray"
        )
        RentalPrice_Lbl.grid(row=0, column=4)

        # self.insert.pack(pady=20)

        # Entry Boxs

        self.shopID_box = Entry(
            self.add_frame,
            justify="center",
            width=8,
            background="lightgray",
            borderwidth=3,
        )
        self.shopID_box.grid(row=1, column=0)
        self.shopID_box.configure(state="disabled")

        self.shopFloor_box = Entry(
            self.add_frame, background="lightgray", borderwidth=3
        )
        self.shopFloor_box.grid(row=1, column=1)

        self.shopSection_box = Entry(
            self.add_frame, background="lightgray", borderwidth=3
        )
        self.shopSection_box.grid(row=1, column=2)

        self.shopSize_box = Entry(self.add_frame, background="lightgray", borderwidth=3)
        self.shopSize_box.grid(row=1, column=3)

        self.rentalPrice_box = Entry(
            self.add_frame, width=15, background="lightgray", borderwidth=3
        )
        self.rentalPrice_box.grid(row=1, column=4)

    def InitializeButton(self):
        # Add Button
        self.add_btn = Button(
            self.root,
            text="Add New Shop",
            font=("Comic Sans MS", 12, "bold"),
            height=2,
            width=15,
            foreground="blue",
            background="white",
            command=self.AddBtn,
        )
        self.add_btn.place(x=50, y=580)

        # Save Button
        self.save_btn = Button(
            self.root,
            text="Save Shop",
            font=("Comic Sans MS", 12, "bold"),
            height=2,
            width=15,
            foreground="blue",
            background="white",
            command=self.SaveBtn,
        )
        self.save_btn.place(x=210, y=580)

        # Update Button
        self.update_button = Button(
            self.root,
            text="Update Shop",
            font=("Comic Sans MS", 12, "bold"),
            height=2,
            width=15,
            foreground="blue",
            command=self.UpdateBtn,
        )

        self.update_button.place(x=370, y=580)

        # Remone_One Selected
        self.delete_btn = Button(
            self.root,
            text="Delete Shop",
            font=("Comic Sans MS", 12, "bold"),
            height=2,
            width=15,
            foreground="FireBrick",
            background="white",
            command=self.DeleteBtn,
        )
        self.delete_btn.place(x=530, y=580)

        # Check Shop Button
        self.checkShop_btn = Button(
            self.root,
            text="Check\nShop Information",
            font=("Comic Sans MS", 12, "bold"),
            height=2,
            width=15,
            foreground="FireBrick",
            background="white",
            command=self.CheckShopBtn,
        )
        self.checkShop_btn.place(x=690, y=580)
        # Exit Button
        exit_button = Button(
            self.root,
            text="Exit",
            font=("Comic Sans MS", 12, "bold"),
            foreground="Brown",
            background="green",
            height=2,
            width=15,
            command=self.root.destroy,
        )
        exit_button.place(x=900, y=580)

    def InitializeTreeview(self):
        self.my_tree = ttk.Treeview(self.root)

        # Add the rowheight
        # root.configure('Treeview', rowheight=40)
        # Add Style

        style = ttk.Style()
        style.configure("Treeview", rowheight=40, background="CornflowerBlue")
        style.map("Treeview")

        # Place to the screen
        self.my_tree.place(x=10, y=143)

        # Define Our Columns
        self.my_tree["columns"] = (
            "Shop ID",
            "ឈ្មោះ",
            "ជាន់ទី",
            "ផ្នែក",
            "ទំហំ​ [(m) x (m)]",
            "តម្លៃជួល",
            "ត្រូវបានជួល",
            "ប្រភេទហាង",
        )

        # Formate Our Columns
        self.my_tree.column("#0", width=0, minwidth=30)
        self.my_tree.column("Shop ID", anchor=W, width=120)
        self.my_tree.column("ឈ្មោះ", anchor=CENTER, width=200)
        self.my_tree.column("ជាន់ទី", anchor=CENTER, width=80)
        self.my_tree.column("ផ្នែក", anchor=CENTER, width=160)
        self.my_tree.column("ទំហំ​ [(m) x (m)]", anchor=CENTER, width=120)
        self.my_tree.column("តម្លៃជួល", anchor=CENTER, width=120)
        self.my_tree.column("ត្រូវបានជួល", anchor=CENTER, width=120)
        self.my_tree.column("ប្រភេទហាង", anchor=CENTER, width=160)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("Shop ID", text="Shop ID", anchor=CENTER)
        self.my_tree.heading("ឈ្មោះ", text="ឈ្មោះ", anchor=CENTER)
        self.my_tree.heading("ជាន់ទី", text="ជាន់ទី", anchor=W)
        self.my_tree.heading("ផ្នែក", text="ផ្នែក", anchor=CENTER)
        self.my_tree.heading(
            "ទំហំ​ [(m) x (m)]", text="ទំហំ​ [(m) x (m)]", anchor=CENTER
        )
        self.my_tree.heading("តម្លៃជួល", text="តម្លៃជួល", anchor=CENTER)
        self.my_tree.heading("ត្រូវបានជួល", text="ត្រូវបានជួល", anchor=CENTER)
        self.my_tree.heading("ប្រភេទហាង", text="ប្រភេទហាង", anchor=CENTER)

        # insert Shopping Mall data
        shopping_mall_data = self._shopManagement.GetAll()
        for shopping_mall in shopping_mall_data:
            shop_value = (
                shopping_mall.ShopID,
                shopping_mall.ShopName,
                shopping_mall.ShopFloor,
                shopping_mall.ShopSection,
                shopping_mall.ShopSize,
                shopping_mall.RentalPrice,
                shopping_mall.RentStatus,
                shopping_mall.ProductType,
            )

            self.my_tree.insert(
                parent="",
                index="end",
                iid=shopping_mall.ShopID,
                text="",
                values=shop_value,
            )

        self.my_tree.bind("<Double-1>", self.Treeview_Click)

    # def my_time(self):
    #     time_string = strftime('%H:%M:%S %p') # time format
    #     self.hours.config(text=time_string)
    #     self.hours.after(1000,self.my_time) # time delay of 1000 milliseconds

    def AddBtn(self):
        self.shopFloor_box.configure(state="normal")
        self.shopSection_box.configure(state="normal")
        self.shopSize_box.configure(state="normal")
        self.rentalPrice_box.configure(state="normal")

        self.shopID_box.configure(state="normal")
        self.DeleteAllBox()
        self.shopID_box.configure(state="disabled")

        self.save_btn.configure(state="normal")
        self.update_button.configure(state="disabled")
        self.delete_btn.configure(state="disabled")
        pass

    def SaveBtn(self):
        try:
            newShop = ShopInMall()
            newShop.ShopFloor = int(self.shopFloor_box.get())
            newShop.ShopSection = self.shopSection_box.get()
            newShop.ShopSize = self.shopFloor_box.get()
            newShop.RentalPrice = float(self.rentalPrice_box.get())

            self._shopManagement.Add(newShop)
            self.InitializeTreeview()
            self.DeleteAllBox()
            self.CloseAllBox()
            self.save_btn.configure(state="disabled")
        except ValueError as ve:
            messagebox.showwarning("Warning!!", ve)

    def UpdateBtn(self):
        try:
            updated_shop = ShopInMall()
            updated_shop.ShopID = int(self.shopID_box.get())
            updated_shop.ShopFloor = int(self.shopFloor_box.get())
            updated_shop.ShopSection = self.shopSection_box.get()
            updated_shop.ShopSize = self.shopFloor_box.get()
            updated_shop.RentalPrice = float(self.rentalPrice_box.get())
            self._shopManagement.Update(updated_shop)
            self.InitializeTreeview()

            self.shopID_box.configure(state="normal")
            self.DeleteAllBox()
            self.shopID_box.configure(state="disabled")
            self.CloseAllBox()

            self.update_button.configure(state="disabled")
            self.delete_btn.configure(state="disabled")

        except ValueError as ve:
            messagebox.showwarning("Warning!!", ve)

    def DeleteBtn(self):
        try:
            deleted_shop = ShopInMall()
            deleted_shop.ShopID = int(self.shopID_box.get())
            deleted_shop.ShopFloor = int(self.shopFloor_box.get())
            deleted_shop.ShopSection = self.shopSection_box.get()
            deleted_shop.ShopSize = self.shopFloor_box.get()
            deleted_shop.RentalPrice = float(self.rentalPrice_box.get())
            self._shopManagement.Delete(deleted_shop)
            self.InitializeTreeview()

            self.shopID_box.configure(state="normal")
            self.DeleteAllBox()
            self.shopID_box.configure(state="disabled")
            self.CloseAllBox()

            self.update_button.configure(state="disabled")
            self.delete_btn.configure(state="disabled")
        except ValueError as ve:
            messagebox.showwarning("Warning!!", ve)

    def Treeview_Click(self, event):
        selected = self.my_tree.focus()
        # item = self.my_tree.selection()[0]
        values = self.my_tree.item(selected, "values")

        self.shopID_box.configure(state="normal")
        self.OpenAllBox()
        self.DeleteAllBox()

        self.shopID_box.insert(END, values[0])
        self.shopFloor_box.insert(END, values[2])
        self.shopSection_box.insert(END, values[3])
        self.shopSize_box.insert(END, values[4])
        self.rentalPrice_box.insert(END, values[3])
        self.shopID_box.configure(state="disabled")

        self.update_button.configure(state="normal")
        self.delete_btn.configure(state="normal")
        self.save_btn.configure(state="disabled")
        self.checkShop_btn.configure(state="normal")

    def OpenAllBox(self):
        self.shopFloor_box.configure(state="normal")
        self.shopSection_box.configure(state="normal")
        self.shopSize_box.configure(state="normal")
        self.rentalPrice_box.configure(state="normal")

    def CloseAllBox(self):
        self.shopFloor_box.configure(state="disabled")
        self.shopSection_box.configure(state="disabled")
        self.shopSize_box.configure(state="disabled")
        self.rentalPrice_box.configure(state="disabled")

    def DeleteAllBox(self):
        self.shopID_box.delete(0, END)
        self.shopFloor_box.delete(0, END)
        self.shopSection_box.delete(0, END)
        self.shopSize_box.delete(0, END)
        self.rentalPrice_box.delete(0, END)

        self.checkShop_btn.configure(state="disabled")

    def CheckShopBtn(self):
        if self.on_closing() != None:
            from ShopMenuGUI import ShopMenuGui

            seller_data = LoadSellerFromStorage()
            shop_data = LoadShopFromStorage()

            root = Tk()
            root.title("Data Structure Assignment")
            root.configure(background="Cyan")
            # root.iconbitmap()
            root.geometry("1300x555+120+100")
            ShopMenuGui(root, seller_data, shop_data, self.shopId)

            root.mainloop()

    def on_closing(self):
        if self.shopID_box.get() != "":
            self.shopId = int(self.shopID_box.get())
        msg_box = messagebox.askyesnocancel(
            "Exit Application", "Do you want to save?", icon="warning"
        )
        if msg_box is True:
            SaveShopToStorage(self._shopManagement.GetAll())
            self.root.destroy()
        elif msg_box is False:
            self.root.destroy()
        elif msg_box is None:
            pass
        return msg_box
