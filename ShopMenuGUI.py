from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Features import ShopManagement, SellerManagement
from time import strftime
import datetime as dt

from Entity import ShopInMall, Seller
from DataToStorageManagement import (
    SaveShopToStorage,
    SaveSellerToStorage,
    LoadShopFromStorage,
)


class ShopMenuGui:
    def __init__(self, root: Tk, sellerData: list, shopData: list, shopId: int) -> None:
        self.root = root
        self._sellerManagement = SellerManagement(sellerData, shopData, shopId)

        lbig_title = Label(
            self.root,
            text="Manage Shop Information",
            font=("Times New Roman", 40, "bold"),
            background="DodgerBlue",
            foreground="MediumBlue",
        )
        # lbig_title.place(x=280, y=0)
        lbig_title.pack(padx=10)

        self.InitializeComponent()
        self.InitializeButton()
        # self.InitializeTreeview()
        self.sellerID_box.configure(state="disabled")

        if self._sellerManagement.GetShop().SellerID != -1:
            shop = self._sellerManagement.GetShop()
            seller = self._sellerManagement.GetSeller(shop.SellerID)

            self.sellerID_box.configure(state="normal")
            self.sellerID_box.insert(0, shop.SellerID)
            self.shopName_box.insert(0, shop.ShopName)
            self.productType_combobox.insert(0, shop.ProductType)
            self.sellerName_box.insert(0, seller.SellerName)
            self.sellerIDCardNumber_box.insert(0, seller.SellerIDCardNumber)
            self.gender_combobox.insert(0, seller.SellerGender)
            self.phoneNumber_box.insert(0, seller.PhoneNumber)
            self.rentUntil_box.insert(
                0, dt.datetime.strftime(seller.RentUntil, "%Y-%m-%d")
            )

            self.register_btn.configure(state="disabled")

        else:
            self.rentUntil_box.insert(
                0, dt.datetime.strftime(dt.date(1, 1, 1), "%Y-%m-%d")
            )
            self.update_btn.configure(state="disabled")
            self.remove_btn.configure(state="disabled")

        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def InitializeComponent(self):
        self.add_frame = Frame(self.root)
        self.add_frame.pack(pady=20, padx=20)

        # Label for Seller
        SellerID_Lbl = Label(self.add_frame, text="Seller ID:", foreground="blue")
        SellerID_Lbl.grid(row=0, column=0)

        ShopName_Lbl = Label(
            self.add_frame, text="Shop Name:", foreground="blue", justify=RIGHT
        )
        ShopName_Lbl.grid(row=1, column=0)

        ProductType_Lbl = Label(
            self.add_frame, text="Product Type:", foreground="blue", justify=RIGHT
        )
        ProductType_Lbl.grid(row=2, column=0)

        SellerName_Lbl = Label(self.add_frame, text="Seller Name:", foreground="blue")
        SellerName_Lbl.grid(row=3, column=0)

        SellerIDCardNumber_Lbl = Label(
            self.add_frame, text="IDCard Number:", foreground="blue", justify=RIGHT
        )
        SellerIDCardNumber_Lbl.grid(row=4, column=0)

        SellerGender_Lbl = Label(self.add_frame, text="Gender:", foreground="blue")
        SellerGender_Lbl.grid(row=5, column=0)

        PhoneNumber_Lbl = Label(self.add_frame, text="Phone No:", foreground="blue")
        PhoneNumber_Lbl.grid(row=6, column=0)

        RentUntil_Lbl = Label(self.add_frame, text="Rent Until:", foreground="blue")
        RentUntil_Lbl.grid(row=7, column=0)

        # self.insert.pack(pady=20)

        # Entry Boxs

        self.sellerID_box = Entry(
            self.add_frame, justify="right", background="lightgray"
        )
        self.sellerID_box.grid(row=0, column=1)
        self.sellerID_box.configure(state="disabled")

        # self.shopName_box = Entry(self.add_frame,background='lightgray')
        # self.shopName_box.grid(row=1, column=1)

        self.shopName_box = Entry(self.add_frame, background="lightgray")
        self.shopName_box.grid(row=1, column=1)

        productTypeValues = ("Sell Big Products", "Sell Small Products", "Service")
        self.productType_combobox = ttk.Combobox(
            self.add_frame, background="lightgray", width=17, values=productTypeValues
        )
        self.productType_combobox.grid(row=2, column=1)

        self.sellerName_box = Entry(self.add_frame, background="lightgray")
        self.sellerName_box.grid(row=3, column=1)

        self.sellerIDCardNumber_box = Entry(self.add_frame, background="lightgray")
        self.sellerIDCardNumber_box.grid(row=4, column=1)

        genderValues = ("Male", "Female", "Unknown")
        self.gender_combobox = ttk.Combobox(
            self.add_frame, background="lightgray", width=17, values=genderValues
        )
        self.gender_combobox.grid(row=5, column=1)

        self.phoneNumber_box = Entry(self.add_frame, background="lightgray")
        self.phoneNumber_box.grid(row=6, column=1)

        self.rentUntil_box = Entry(self.add_frame, background="lightgray")
        self.rentUntil_box.grid(row=7, column=1)

    def InitializeButton(self):
        # Add Button
        self.register_btn = Button(
            self.root,
            text="Register Seller",
            font=("Comic Sans MS", 12, "bold"),
            height=2,
            width=15,
            foreground="blue",
            background="white",
            command=self.RegisterBtn,
        )
        self.register_btn.place(x=10, y=150)

        # Save Button
        self.update_btn = Button(
            self.root,
            text="Update Seller",
            font=("Comic Sans MS", 12, "bold"),
            height=2,
            width=15,
            foreground="blue",
            background="white",
            command=self.UpdateBtn,
        )
        self.update_btn.place(x=10, y=225)

        self.remove_btn = Button(
            self.root,
            text="Remove Seller",
            font=("Comic Sans MS", 12, "bold"),
            height=2,
            width=15,
            foreground="blue",
            background="white",
            command=self.RemoveBtn,
        )
        self.remove_btn.place(x=10, y=300)

        # Check Shop Button
        self.checkShop_btn = Button(
            self.root,
            text="Go Back to\nMain Menu",
            font=("Comic Sans MS", 12, "bold"),
            height=2,
            width=15,
            foreground="red",
            background="white",
            command=self.BackToMenuBtn,
        )
        self.checkShop_btn.place(x=10, y=450)

    def on_closing(self):
        msg_box = messagebox.askyesnocancel(
            "Exit Application", "Do you want to save?", icon="warning"
        )
        if msg_box is True:
            SaveSellerToStorage(self._sellerManagement.GetAllSeller())
            SaveShopToStorage(self._sellerManagement.GetAllShop())
            self.root.destroy()
        elif msg_box is False:
            self.root.destroy()
        elif msg_box is None:
            pass
        return msg_box

    def RegisterBtn(self):
        try:
            seller = Seller()
            seller.SellerIDCardNumber = self.sellerIDCardNumber_box.get()
            seller.SellerName = self.sellerName_box.get()
            seller.SellerGender = self.gender_combobox.get()
            seller.PhoneNumber = self.phoneNumber_box.get()
            seller.RentUntil = dt.datetime.strptime(
                self.rentUntil_box.get(), "%Y-%m-%d"
            )

            shop = ShopInMall()
            shop.ShopName = self.shopName_box.get()
            shop.ProductType = self.productType_combobox.get()

            self._sellerManagement.Register(seller, shop)
            self.register_btn.configure(state="disabled")
            self.update_btn.configure(state="normal")
            self.remove_btn.configure(state="normal")
        except ValueError as ve:
            messagebox.showwarning("Warning!!", ve)

    def UpdateBtn(self):
        try:
            seller = Seller()
            seller.SellerIDCardNumber = self.sellerIDCardNumber_box.get()
            seller.SellerName = self.sellerName_box.get()
            seller.SellerGender = self.gender_combobox.get()
            seller.PhoneNumber = self.phoneNumber_box.get()
            seller.RentUntil = dt.datetime.strptime(
                self.rentUntil_box.get(), "%Y-%m-%d"
            )

            shop = ShopInMall()
            shop.ShopName = self.shopName_box.get()
            shop.ProductType = self.productType_combobox.get()

            self._sellerManagement.Update(seller, shop)
        except ValueError as ve:
            messagebox.showwarning("Warning!!", ve)

    def RemoveBtn(self):
        try:
            seller = Seller()
            seller.SellerID = int(self.sellerID_box.get())
            seller.SellerIDCardNumber = self.sellerIDCardNumber_box.get()
            seller.SellerName = self.sellerName_box.get()
            seller.SellerGender = self.gender_combobox.get()
            seller.PhoneNumber = self.phoneNumber_box.get()
            seller.RentUntil = dt.datetime.strptime(
                self.rentUntil_box.get(), "%Y-%m-%d"
            )

            self._sellerManagement.Delete(seller)
            self.sellerID_box.configure(state="normal")
            self.DeleteAllBox()
            self.sellerID_box.configure(state="disabled")
            self.register_btn.configure(state="normal")
            self.update_btn.configure(state="disabled")
            self.remove_btn.configure(state="disabled")
        except ValueError as ve:
            messagebox.showwarning("Warning!!", ve)

    def BackToMenuBtn(self):
        if self.on_closing() != None:
            from MainMenuGUI import MainMenuGui

            shopData = LoadShopFromStorage()

            root = Tk()
            root.title("Data Structure Assignment")
            root.configure(background="Cyan")
            # root.iconbitmap()
            root.geometry("1235x555+120+100")

            MainMenuGui(root, shopData)

            root.mainloop()

    def DeleteAllBox(self):
        self.sellerID_box.delete(0, END)
        self.shopName_box.delete(0, END)
        self.productType_combobox.delete(0, END)
        self.sellerName_box.delete(0, END)
        self.sellerIDCardNumber_box.delete(0, END)
        self.gender_combobox.delete(0, END)
        self.phoneNumber_box.delete(0, END)
        self.rentUntil_box.delete(0, END)
        self.rentUntil_box.insert(0, dt.datetime.strftime(dt.date(1, 1, 1), "%Y-%m-%d"))
