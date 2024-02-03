from DataToStorageManagement import SaveShopToStorage
from Entity import ShopInMall

shop1 = ShopInMall()
shop1.ShopID = 1
shop1.ShopName = ""
shop1.ShopFloor = 2
shop1.ShopSection = "C"
shop1.ShopSize = "30x30"
shop1.RentalPrice = ""
shop1.SellerID = 1
shop1.ProductType = "Service"

SaveShopToStorage([shop1])
