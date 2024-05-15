class BuyAndSellStock (object):

    def buyAndSellStock(self, prices):

        profit = 0 # Variable to store the maximum profit
        min = prices[0] # Variable to store the minimum price, initialized with the first price

        # Loop through the prices starting from the second price, saving the current price in the variable 'price'
        for price in prices[1:]:
            # Check if the current price is greater than the minimum price
            if price > min:
                # Calculate the profit and update the maximum profit, if necessary
                profit = max(profit, price - min)
            # If the current price is less than the minimum price, update the minimum price
            else:
                min = price

        # Return the maximum profit
        return profit
