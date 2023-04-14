#!/bin/python3

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

lastweek = [3, 7, 4, 5, 8, 4, 5, 6]

totalprice = 0

for x in prices:
	totalprice = totalprice + x

averageprice = totalprice/len(hairstyles)
print(averageprice)

new_prices = []

for x in prices:
	new_prices.append(x-5)

print(new_prices)

total_revenue = 0

for i in range(len(prices)):
	total_revenue = total_revenue + (prices[i]*lastweek[i])

print("Total revenue:", total_revenue)


cuts_under_30 = [hairstyles[x] for x in range(len(new_prices)) if new_prices[x] < 30]

print(cuts_under_30)
