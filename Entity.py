import datetime

# class ShoppingMall:
#     MallID = int()
#     MallName = str()
#     Province = str()
#     District = str()
#     Commune = str()
#     MallFloor_amt = int()
#     TotalShop_amt = int()
#     RentedShop_amt = int()

#     def __init__(self) -> None:
#         self.MallName = ''
#         self.Province = ''
#         self.District = ''
#         self.Commune = ''
#         self.MallFloor_amt = -1
#         self.TotalShop_amt = -1
#         self.RentedShop_amt = -1
#         pass

class ShopInMall:
    ShopID = int()
    ShopName = str()
    ShopFloor = int()
    ShopSection = str()
    ShopSize = str()
    RentalPrice = float()
    RentStatus = str()
    SellerID = int()
    ProductType = str()

    def __init__(self) -> None:
        self.ShopName = ''
        self.ShopFloor = -1
        self.ShopSection = ''
        self.ShopSize = ''
        self.RentalPrice = 0
        self.RentStatus = 'No'
        self.SellerID = -1
        self.ProductType = ''
        pass

class Seller:
    SellerID = int()
    SellerIDCardNumber = str()
    SellerName = str()
    SellerGender = str()
    PhoneNumber = str() 
    RentUntil = datetime.date(1, 1, 1)

    def __init__(self) -> None:
        self.SellerIDCardNumber = ''
        self.SellerName = ''
        self.SellerGender = ''
        self.PhoneNumber = ''
        pass