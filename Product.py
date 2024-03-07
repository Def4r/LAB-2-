#This is the product class. This is were all of the class were we initialze all of the business information needed to run the code 

import random
from UserChecking import userI, userII, userIII

class ProductClass:
    
    def __init__(self, name="", code=0, sales_price=0, manufacturer_cost=0, stock_level=0, est_manufactured_monthly=0):
        self.__name = name
        self.__code = code
        self.__sales_price = sales_price
        self.__manufacturer_cost = manufacturer_cost
        self.__stock_level = stock_level
        self.__est_manufactured_monthly = est_manufactured_monthly
    
    def get_est_manufactured(self):
        return self.__est_manufactured_monthly
    
    def get_stock_level(self):
        return self.__stock_level

    def get_product_price(self):
        return self.__sales_price

    def get_manufacturer_cost(self):
        return self.__manufacturer_cost

    def business_info(self):
        self.__name = input("What is the name of your product? :")
        self.__code = userI("What is the code for your product? :", 100, 1000)
        self.__sales_price = userII("How much would you price your products? CAD ONLY $", 0)
        self.__manufacturer_cost = userII("How much does it cost to make your product? CAD ONLY $", 0)
        self.__stock_level = userII("How much do you currently have in your stock? :", 0)
        self.__est_manufactured_monthly = userIII("How much do you manufacture every month. This is an estimate. :", 0)

    def display_business_info(self):
        print("")
        print("Product Name:", self.__name)
        print("Product Code:", self.__code)
        print("")
        print("Product Price: $", self.__sales_price, "CAD")
        print("Product Manufacturer Cost: $", self.__manufacturer_cost, "CAD")
        print("")
        print("Amount of Product in Stock:", self.__stock_level, "Units")
        print("Estimated Amount Manufactured:", self.__est_manufactured_monthly, "Units")
        print("")

    def sales_each_month(self, random_sales):
        sales_monthly = self.__est_manufactured_monthly + random_sales
        return sales_monthly


    

        


