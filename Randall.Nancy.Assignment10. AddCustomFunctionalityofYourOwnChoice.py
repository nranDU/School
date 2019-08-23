"""Nancy Randall Assignment 10: Add Custom Functionality of Own Choice
Program written between dates 8/20/2019-8/22/2019. Program is designed to
import JSON data and output the stock distribution of closing prices as a pie chart. Also will print statement 
to demonstrate that the JSON data was added.
"""
import json
import matplotlib.pyplot as plt
from datetime import datetime

filePath = "C:/Users/thena/Documents/ICT 4370/Python Work/AllStocks.json"

#load all data into the variable f
with open(filePath) as f:
    dataSet = json.load(f)    

dataSet = reversed(dataSet)

#for creating IDs
currentPurchaseID = 0
currentInvestorID = 0


class Stock():
    #create stock attributes
    def __init__(self, stock_symbol):
        global currentPurchaseID
        currentPurchaseID += 1
        """Attributes of class Stock"""
        self.stock_symbol = stock_symbol
        self.dates = [] 
        self.prices = []
        self.openPrice = []
        self.volume = []
        self.high = []
        self.low = []
        
    #method of class Stock
    def calculation_equity(self):
        """Calculates the gains/loss of the stockholder"""
        original_cost = self.purchase_prices
        current_value = self.current_values
        num_shares = self.no_shares
        #(current value – purchase price) x number of shares
        worth = (current_value - original_cost) * num_shares
        return worth
        
    #method of class Stock
    def yearly_earnings(self):
        """Calculate percent yearly earning rate"""
        value = self.current_values
        price = self.purchase_prices
        m, d, y = self.purchase_dates.split('/')
        purc_date = datetime.date(int(y),int(m),int(d))
        today = datetime.date(2017,8,2)
        years = (today-purc_date).days / 365
        #((((current value – purchase price)/purchase price)/(current date – purchase date)))*100
        return (value - price)/price / years * 100
    
    #method of class Stock
    def percent_earnings_loss(self):
        """Calculates the yield/loss percentage"""
        original_cost = self.purchase_prices
        current_value = self.current_prices 
        num_shares = self.no_shares
        #(current value – purchase price) x number of shares
        percent_yield = (current_value - original_cost) * num_shares * 100
        return percent_yield

class Investor():
    #create attributes
    """Investor names, addresses, and phone numbers"""
    def __init__(self, firstName, lastName, address, phone_number):
        global currentInvestorID
        currentInvestorID += 1
        self.firstName = firstName.title()
        self.lastName = lastName.title()
        self.address = address.title()
        self.phone_number = phone_number
        self.investor_id = currentInvestorID
    
    def name(self):
        fullName = self.firstName.title() + " " + self.lastName.title()
        return fullName

class Bond(Stock):
    #create attributes
    """Inherits from the Stock class, with added coupon and yield attributes. Includes method to read 
    both the coupon and yield values"""
    def __init__(self, stock_symbol, no_shares, purchase_prices, 
                       current_values, purchase_dates,
                       coupon, bond_yield):
        super().__init__(stock_symbol, no_shares, purchase_prices, current_values, purchase_dates)
        self.coupon = coupon
        self.bond_yield = bond_yield
    #coupon and yield unique to Bond class so added here
    def describe_coupon(self):
        return self.coupon
    def describe_bond_yield(self):
        return self.bond_yield
        num_shares = stock_info['no_shares'][i]
        #(current value – purchase price) x number of share
        worth = (current_value - original_cost) * num_shares
        return worth   


stockPortfolio = []
stockSymbols = []

 #loop to work through json file
 #loop for checking stock, if not in list, add   
newStock = None
for stock in dataSet:
    if stock['Symbol'] not in stockSymbols:
        stockSymbols.append(stock['Symbol'])
        if newStock is not None:
            stockPortfolio.append(newStock)
        newStock = Stock(stock['Symbol'])
        newStock.dates.append(datetime.strptime(stock['Date'], '%d-%b-%y'))
        newStock.prices.append(stock['Close'])
        newStock.high.append(stock['High'])
        newStock.low.append(stock['Low'])
        newStock.volume.append(stock['Volume'])
        newStock.openPrice.append(stock['Open'])
        
    #still add dates and price if stock exists in portfolio
    else:
        newStock.dates.append(datetime.strptime(stock['Date'], '%d-%b-%y'))
        newStock.prices.append(stock['Close'])
        newStock.high.append(stock['High'])
        newStock.low.append(stock['Low'])
        newStock.volume.append(stock['Volume'])
        newStock.openPrice.append(stock['Open'])

stockPortfolio.append(newStock)        
        
#This is code for a line graph
#plot table
#plt.title('Stock Portfolio')
#plt.xlabel('Date')
plt.ylabel('Stock Symbol')
#for stock in stockPortfolio:
 #   plt.plot(stock.dates, stock.prices, label=stock.stock_symbol)


#data sample to show import of json data
for i in range(len(stockPortfolio)):
    s = stockPortfolio[i]
    print("Symbol: " + str(s.stock_symbol))
    print("Closing Price: " + str(s.prices[0]))
    print("Opening price: "+ str(s.openPrice[0]))
    print("Purchase Date: " + str(s.dates[0]))
    print("Volume: " + str(s.volume[0]))
    print("Price High: " + str(s.high[0]))
    print("Price Low: " + str(s.low[0]))
    print("\n\n\n\n")

    
#code from line graph  
#plt.legend()
#plt.show()

######################################################################################################
# added functionality

# get all the data that will be used in the pie chart: volumne values and closing values

#dictionary to store 2 lists by their names

s = {}

import numpy as np

#function for values and percentage
def func(pct, data):
    absolute = int(pct/100.*np.sum(data))
    return "{:.1f}%\n(closing: {:d})".format(pct, absolute)

closing = []

#grab the symbols and volume
for i in range(len(stockPortfolio)):
    s[stockPortfolio[i].stock_symbol] =  stockPortfolio[i].volume[0]
    closing.append(stockPortfolio[i].prices[0])
    
    
    
#pie chart code  
slices = list(s.values())
labels = list(s.keys())
colors = ['blue', 'red', 'yellow', 'green', 'purple', 'gray', 'orange', 'pink']
shadow = True
#add percentage to graph
autopct = '%1.1f%%'

plt.title("Stock value distribution", y = 1.4)


patches = plt.pie(slices, labels = labels, colors = colors, wedgeprops = {'edgecolor':'black'}
        ,autopct = lambda pct: func(pct, closing), radius = 1.0)


plt.show()




























