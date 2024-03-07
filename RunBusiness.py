from Product import ProductClass
from time import sleep
import random

print("***Welcome to the Business Production Sim***")
print("")

business = ProductClass()
business.business_info()
business.display_business_info()

print("")
sleep(1)
print("***Business in year statement***")
print("")

net_profits = 0
stock = business.get_stock_level()
current_stock = business.get_stock_level()

# Loops through each month generating and showing stock, sales, and the current month
for month in range(1, 13):
    sleep(2)
    sales = random.randint(-10, 10)
    print("Month", month, ":")
    print("Manufactured: ", business.get_est_manufactured())
    print("Sold ", business.sales_each_month(sales))
    current_stock -= sales
    print("Stock Left:", current_stock)
    print("")
    monthly_revenue = business.sales_each_month(sales) * business.get_product_price()
    monthly_cost = business.sales_each_month(sales) * business.get_manufacturer_cost()
    monthly_profits = monthly_revenue - monthly_cost
    net_profits += monthly_profits

# Shows the Netprofits after 12 months have passed
print("Net Profits over 12 Months: $", net_profits)
