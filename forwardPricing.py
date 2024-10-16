##inputs from user
price = float(input("Security price: ").replace("$",""))
riskFreeRate = float(input("Risk free rate, decimal terms: ").replace("%",""))
tenor = int(input("Tenor: "))
convention = int(input("N = 360/365: "))
##calculation + ouput
futuresPrice = price * ((riskFreeRate * (tenor/convention) + 1))
print("$" + str(futuresPrice))