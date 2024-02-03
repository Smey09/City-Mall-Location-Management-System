from Entity import*
import datetime
import json

# def SaveShoppingMallToStorage(shoppingMallList : list):
#     shoppingMallList_Json = []
#     for shoppingMall in shoppingMallList:
#         shoppingMall_Json = dict()

#         # shoppingMall = ShoppingMall()
#         shoppingMall_Json["MallID"] = shoppingMall.MallID
#         shoppingMall_Json["MallName"] = shoppingMall.MallName
#         shoppingMall_Json["Province"] = shoppingMall.Province
#         shoppingMall_Json["District"] = shoppingMall.District
#         shoppingMall_Json["Commune"] = shoppingMall.Commune
#         shoppingMall_Json["MallFloor_amt"] = shoppingMall.MallFloor_amt
#         shoppingMall_Json["TotalShop_amt"] = shoppingMall.TotalShop_amt
#         shoppingMall_Json["RentedShop_amt"] = shoppingMall.RentedShop_amt

#         shoppingMallList_Json.append(shoppingMall_Json)

#     with open("JSON_DATA/ShoppingMallData.json", 'w') as f:
#         json.dump(shoppingMallList_Json, f)

# def LoadShoppingMallFromStorage():
#     with open("JSON_DATA/ShoppingMallData.json", 'r') as f:
#         shoppingMallList_Json = json.load(f)

#     shoppingMallList = []
#     for shoppingMall_Json in shoppingMallList_Json:
#         shoppingMallList_Json = dict()
#         shoppingMall = ShoppingMall()
        
#         shoppingMall.MallID = shoppingMall_Json["MallID"]
#         shoppingMall.MallName = shoppingMall_Json["MallName"]  
#         shoppingMall.Province = shoppingMall_Json["Province"]  
#         shoppingMall.District = shoppingMall_Json["District"] 
#         shoppingMall.Commune = shoppingMall_Json["Commune"]  
#         shoppingMall.MallFloor_amt = shoppingMall_Json["MallFloor_amt"]  
#         shoppingMall.TotalShop_amt = shoppingMall_Json["TotalShop_amt"]  
#         shoppingMall.RentedShop_amt = shoppingMall_Json["RentedShop_amt"]  

#         shoppingMallList.append(shoppingMall)

#     return shoppingMallList

def SaveShopToStorage(shopList : list):
    shopList_Json = []

    for shop in shopList:
        shop_Json = dict()

        # shop = ShopInMall()
        shop_Json["ShopID"] = shop.ShopID
        shop_Json["ShopName"] = shop.ShopName
        shop_Json["ShopFloor"] = shop.ShopFloor
        shop_Json["ShopSection"] = shop.ShopSection
        shop_Json["ShopSize"] = shop.ShopSize
        shop_Json["RentalPrice"] = shop.RentalPrice
        shop_Json["RentStatus"] = shop.RentStatus
        shop_Json["SellerID"] = shop.SellerID
        shop_Json["ProductType"] = shop.ProductType
        shopList_Json.append(shop_Json)

    with open("JSON_Data/ShopInMallData.json", 'w') as f:
        json.dump(shopList_Json, f)

def LoadShopFromStorage():
    with open("JSON_Data/ShopInMallData.json", 'r+') as f:
        shopList_Json = json.load(f)
    shopList = list()

    for shop_Json in shopList_Json:
        shop = ShopInMall()
        shop.ShopID = shop_Json["ShopID"]
        shop.ShopName = shop_Json["ShopName"]
        shop.ShopFloor = shop_Json["ShopFloor"]
        shop.ShopSection = shop_Json["ShopSection"]
        shop.ShopSize = shop_Json["ShopSize"]
        shop.RentalPrice = shop_Json["RentalPrice"]
        shop.RentStatus = shop_Json["RentStatus"]
        shop.SellerID = shop_Json["SellerID"]
        shop.ProductType = shop_Json["ProductType"]

        shopList.append(shop)

    return shopList
    
def SaveSellerToStorage(SellerList : list):
    SellerList_Json = []

    for Seller in SellerList:
        # Seller = Seller()
        
        rentUntilStr = datetime.datetime.strftime(Seller.RentUntil, '%Y-%m-%d')
        Seller_Json = dict()
        Seller_Json["SellerID"] = Seller.SellerID
        Seller_Json["SellerIDCardNumber"] = Seller.SellerIDCardNumber
        Seller_Json["SellerName"] = Seller.SellerName
        Seller_Json["SellerGender"] = Seller.SellerGender
        Seller_Json["PhoneNumber"] = Seller.PhoneNumber
        Seller_Json["RentUntil"] = rentUntilStr

        SellerList_Json.append(Seller_Json)

    with open('JSON_Data/SellerData.json', 'w') as f:
        json.dump(SellerList_Json, f)

def LoadSellerFromStorage():
    with open("JSON_Data/SellerData.json", 'r') as f:
        SellerList_Json = json.load(f)
    SellerList = []
    for Seller_Json in SellerList_Json:
        seller = Seller()
        seller.SellerID = Seller_Json["SellerID"]
        seller.SellerIDCardNumber = Seller_Json["SellerIDCardNumber"]
        seller.SellerName = Seller_Json["SellerName"]
        seller.SellerGender = Seller_Json["SellerGender"]
        seller.PhoneNumber = Seller_Json["PhoneNumber"]
        seller.RentUntil = datetime.datetime.strptime(Seller_Json["RentUntil"], '%Y-%m-%d')
        SellerList.append(seller)

    return SellerList

    


## Test ShoppingMall Data
# shoppingMall1 = ShoppingMall()
# shoppingMall1.MallID = 1
# shoppingMall1.MallName = 'LyhengMall'
# shoppingMall1.Province = 'Kandal'
# shoppingMall1.District = 'Takhmao'
# shoppingMall1.Commune = 'Takhmao'
# shoppingMall1.MallFloor_amt = 3
# shoppingMall1.TotalShop_amt = 30
# shoppingMall1.RentedShop_amt = 10
# shoppingMall1.ShoppingMall_description = "Great!!"

# shoppingMall2 = ShoppingMall()
# shoppingMall2.MallID = 2
# shoppingMall2.MallName = 'LyhengMall'
# shoppingMall2.Province = 'Kandal'
# shoppingMall2.District = 'Takhmao'
# shoppingMall2.Commune = 'Takhmao'
# shoppingMall2.MallFloor_amt = 3
# shoppingMall2.TotalShop_amt = 30
# shoppingMall2.RentedShop_amt = 10
# shoppingMall2.ShoppingMall_description = "Great!!"

# SaveShoppingMallToStorage([shoppingMall1, shoppingMall2])

# for shop in LoadShoppingMallFromStorage():
#     print(shop.MallID)

## Test Shop Data
# shop1 = ShopInMall()
# shop1.ShopID = 1
# shop1.ShoppingMallID = 1
# shop1.ShopFloor = 1
# shop1.ShopSection = 'a'
# shop1.ShopSize = "25x25"
# shop1.RentalPrice = 100
# shop1.RentStatus = False

# shop2 = ShopInMall()
# shop2.ShopID = 2
# shop2.ShoppingMallID = 2
# shop2.ShopFloor = 1
# shop2.ShopSection = 'a'
# shop2.ShopSize = "25x25"
# shop2.RentalPrice = 100
# shop2.RentStatus = True

# shop3 = ShopInMall()
# shop3.ShopID = 3
# shop3.ShoppingMallID = 1
# shop3.ShopFloor = 1
# shop3.ShopSection = 'a'
# shop3.ShopSize = "25x25"
# shop3.RentalPrice = 100
# shop3.RentStatus = True

# SaveShopToStorage([shop1, shop2, shop3])

# shoplist = LoadShopFromStorage()
# selectedList = [shop for shop in shoplist if shop.RentStatus == True]

# for shop in selectedList:
#     print(shop.ShopID)

# month = datetime.timedelta(days=31)
# Seller = Seller()
# Seller.SellerID = 1
# Seller.ShopID = 1
# Seller.SellerName = "Lyheng"
# Seller.ShopName = 'LyhengTech'
# Seller.SellerGender = 'M'
# Seller.PhoneNumber = '123'
# Seller.RentUntil = datetime.datetime.now() + month
# Seller.ProductType = 'Heavy'

# SaveRentedShopToStorage([Seller])

# for Seller in LoadRentedShopFromStorage():
#     print(Seller.SellerName)
