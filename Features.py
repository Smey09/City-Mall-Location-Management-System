# if __name__ == "__main__":
from Entity import * 

# class ShoppingMallManagement:
    # data = []
    # def __init__(self, shoppingMallList : list) -> None:
    #     self.data = shoppingMallList
    
    # def Add(self, shoppingMall : ShoppingMall):
    #     if shoppingMall.MallName == '' or shoppingMall.Province == '' or shoppingMall.District == '' or shoppingMall.Commune == '' or shoppingMall.MallFloor_amt == -1 or shoppingMall.TotalShop_amt == -1:
    #         raise ValueError("Please provide all the necessary information for a shopping mall.")

    #     findMall_Duplicate = [sMall for sMall in self.data if sMall.MallName == shoppingMall.MallName]
    #     if findMall_Duplicate != []:
    #         raise ValueError("This Mall already exist. Please enter another one.")

    #     if self.data == []:
    #         shoppingMall.MallID = 1
    #     else:
    #         data_length = len(self.data)
    #         shoppingMall.MallID = self.data[data_length - 1].MallID + 1

    #     self.data.append(shoppingMall)
        
    # def Update(self, shoppingMall : ShoppingMall):
    #     if shoppingMall.MallName == '' or shoppingMall.Province == '' or shoppingMall.District == '' or shoppingMall.Commune == '' or shoppingMall.MallFloor_amt == -1 or shoppingMall.TotalShop_amt == -1:
    #         raise ValueError("Please provide all the necessary information for a shopping mall.")
        
    #     findShopInData = [sMall for sMall in self.data if sMall.MallID == shoppingMall.MallID]
    #     if findShopInData == []:
    #         raise ValueError("The shopping mall doesn't exist.")
        
    #     shopInData = findShopInData[0]
    #     # shopInData = ShoppingMall()
    #     if shoppingMall.MallName != shopInData.MallName:
    #         findShop_Duplicate = [sMall for sMall in self.data if sMall.MallName == shoppingMall.MallName]
    #         if findShop_Duplicate != []:
    #             raise ValueError("This Mall name is already used. Please enter another one.")
            
    #     shopInData.MallName = shoppingMall.MallName
    #     shopInData.Province = shoppingMall.Province
    #     shopInData.District = shoppingMall.District
    #     shopInData.Commune = shoppingMall.Commune
    #     shopInData.MallFloor_amt = shoppingMall.MallFloor_amt
    #     shopInData.RentedShop_amt = shoppingMall.RentedShop_amt

    # def Delete(self, shoppingMall : ShoppingMall):
    #     findMallInData = [sMall for sMall in self.data if sMall.MallID == shoppingMall.MallID and sMall.MallName == shoppingMall.MallName]
    #     if findMallInData == []:
    #         raise ValueError("The shopping mall doesn't exist.")
        
    #     sMall = findMallInData[0]
    #     self.data.remove(sMall)

    # def Get(self, id : int) -> ShoppingMall:
    #     shoppingMall = [sMall for sMall in self.data if sMall.MallID == id][0]
    #     return shoppingMall
    
    # def GetAll(self):
    #     return self.data
    
class ShopManagement:
    data = []
    def __init__(self, shopList : list) -> None:
        self.data = shopList
        pass

    def Add(self, shop : ShopInMall):
        if shop.ShopFloor == -1 or shop.ShopSection == '' or shop.ShopSize == '' or shop.RentalPrice == 0:
            raise ValueError("Please provide all the necessary information")
        
        if shop.ShopName != '':
            findShop_duplicate = [sDupe for sDupe in self.data if sDupe.ShopName == shop.ShopName]
            if findShop_duplicate != []:
                raise ValueError("This Shop Name is already used. Please enter another one")
        
        if self.data == []:
            shop.ShopID = 1
        else:
            shop_amt = len(self.data)
            shop.ShopID = self.data[shop_amt - 1].ShopID + 1

        self.data.append(shop)
    
    def Update(self, shop : ShopInMall):
        if shop.ShopFloor == -1 or shop.ShopSection == '' or shop.ShopSize == '' or shop.RentalPrice == 0:
            raise ValueError("Please provide all the necessary information")
        
        findShopInData = [s for s in self.data if s.ShopID == shop.ShopID]
        if findShopInData == []:
            raise ValueError("The shopping mall doesn't exist.")
        
        shopInData = findShopInData[0]
        
        # if shopInData.ShopName != shop.ShopName and shopInData.ShopName != '':
        #     findShop_duplicate = [sDupe for sDupe in self.data if sDupe.ShopName == shop.ShopName]
        #     if findShop_duplicate != []:
        #         raise ValueError("This Shop Name is already used. Please enter another one")
        
        # shopInData = ShopInMall()
        shopInData.ShopFloor = shop.ShopFloor
        shopInData.ShopSection = shop.ShopSection
        shopInData.ShopSize = shop.ShopSize
        shopInData.RentalPrice = shop.RentalPrice
    
    def Delete(self, shop : ShopInMall):
        findShopInData = [s for s in self.data if s.ShopID == shop.ShopID]
        if findShopInData == []:
            raise ValueError("The shop doesn't exist.")
        
        foundShop = findShopInData[0]
        self.data.remove(foundShop)

    def Get(self, id : int) -> ShopInMall:
        shop = [s for s in self.data if s.ShopID == id][0]
        return shop

    def GetAll(self):
        return self.data
    
class SellerManagement:
    sellerData = []
    shopData = []
    shop = ShopInMall()
    def __init__(self, sellerList : list, shopList : list, shopId : int) -> None:
        self.sellerData = sellerList
        self.shopData = shopList
        self.shop = [s for s in shopList if s.ShopID == shopId][0]
        pass

    def Register(self, seller : Seller, shop : ShopInMall):
        if seller.SellerIDCardNumber == '' or seller.SellerName == '' or seller.SellerGender == '' or seller.PhoneNumber == '':
            raise ValueError("Please provide all the necessary information")
        
        if shop.ShopName == '' or shop.ProductType == '':
            raise ValueError("Please provide all the necessary information")
        
        findRented_Duplicate = [r for r in self.sellerData if r.SellerIDCardNumber == seller.SellerIDCardNumber ]
        if findRented_Duplicate != []:
            raise ValueError("This Seller already exist. Please enter a different seller.")

        if shop.ShopName != self.shop.ShopName:
            findShop_duplicate = [sDupe for sDupe in self.shopData if sDupe.ShopName == shop.ShopName]
            if findShop_duplicate != []:
                raise ValueError("This Shop Name is already used. Please enter another one")
        
        if self.sellerData == []:
            seller.SellerID = 1
        else:
            seller_amt = len(self.sellerData)
            seller.SellerID = self.sellerData[seller_amt - 1].SellerID + 1

        self.sellerData.append(seller)
        self.shop.SellerID = seller.SellerID
        self.shop.ShopName = shop.ShopName
        self.shop.ProductType = shop.ProductType
        self.shop.RentStatus = 'Yes'


    def Update(self, seller : Seller, shop : ShopInMall):
        if seller.SellerIDCardNumber == '' or seller.SellerName == '' or seller.SellerGender == '' or seller.PhoneNumber == '':
            raise ValueError("Please provide all the necessary information")
        
        if shop.ShopName == '' or shop.ProductType == '':
            raise ValueError("Please provide all the necessary information")
        
        findSellerInData = [sl for sl in self.sellerData if sl.SellerID == seller.SellerID and sl.SellerIDCardNumber == seller.SellerIDCardNumber]
        if findSellerInData == []:
            raise ValueError("This Seller doesn't exist")
        
        foundSeller = findSellerInData[0]
        if seller.SellerIDCardNumber != foundSeller.SellerIDCardNumber:
            findSeller_Duplicate = [sl for sl in self.sellerData if sl.SellerIDCardNumber == seller.SellerIDCardNumber]
            if findSeller_Duplicate != []:
                raise ValueError("This seller already exist. Please enter a different seller.")
            
        if shop.ShopName != self.shop.ShopName:
            findShop_duplicate = [sDupe for sDupe in self.shopData if sDupe.ShopName == shop.ShopName]
            if findShop_duplicate != []:
                raise ValueError("This Shop Name is already used. Please enter another one")
            
        foundSeller.SellerIDCardNumber = seller.SellerIDCardNumber
        foundSeller.SellerName = seller.SellerName
        foundSeller.SellerGender = seller.SellerGender
        foundSeller.PhoneNumber = seller.PhoneNumber
        foundSeller.RentUntil = seller.RentUntil
        self.shop.ShopName = shop.ShopName
        self.shop.ProductType = shop.ProductType

    def Delete(self, seller : Seller):
        findSellerInData = [sl for sl in self.sellerData if sl.SellerID == seller.SellerID and sl.SellerIDCardNumber == seller.SellerIDCardNumber]

        if findSellerInData == []:
            raise ValueError("This seller doesn't exist")
        
        foundSeller = findSellerInData[0]
        self.sellerData.remove(foundSeller)
        self.shop.SellerID = -1
        self.shop.ShopName = ''
        self.shop.ProductType = ''
        self.shop.RentStatus = 'No'

    def GetSeller(self, id : int) -> Seller:
        seller = [sl for sl in self.sellerData if sl.SellerID == id][0]
        return seller
    
    def GetAllSeller(self):
        return self.sellerData
    
    def GetShop(self):
        return self.shop
    def GetAllShop(self):
        return self.shopData