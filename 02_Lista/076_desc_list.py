def calculate_discounted_prices(prices, discount_rate):
    discounted_prices = [price * (1 - discount_rate) for price in prices]
    return discounted_prices
original_prices = [10.50, 25.00, 5.75, 12.20]
discount = 0.10
final_prices = calculate_discounted_prices(original_prices, discount)
print(f"Original prices: {original_prices}")
print(f"Prices with {discount*100}% discount: {final_prices}")