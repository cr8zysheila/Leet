stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_yesterday_2 = [10, 8, 7, 5, 2]

#need to consider a corner case where the prices go down all the way
# and the max profit is the min loss
def get_max_profit(stock_prices):
	if len(stock_prices) < 2:
		raise IndexError('Needs at least 2 prices')

	# this is to make sure the corner case of decreasing prices works
	# max_profit = 0
	max_profit = stock_prices[1] - stock_prices[0]
	min_price = stock_prices[0]

	for i in range(1, len(stock_prices)):
		price = stock_prices[i]
		profit = price - min_price
		max_profit = max(max_profit, profit)
		min_price = min(min_price, price)

	return max_profit

print get_max_profit(stock_prices_yesterday)
print get_max_profit(stock_prices_yesterday_2)
